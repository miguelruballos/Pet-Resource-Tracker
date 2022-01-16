from __future__ import print_function
#scale and button imports
import RPi.GPIO as GPIO                # import GPIO
from hx711 import HX711                # import the class HX711
from time import sleep
from rpi_lcd import LCD

#Google API imports
import os.path
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from datetime import date
from datetime import datetime


GPIO.setmode(GPIO.BCM)# set GPIO pin mode to BCM numbering
GPIO.setwarnings(False)

lcd = LCD() #initializing screen

lcd.text('Setting up ', 1)
lcd.text('Device .    ', 2)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)# init red button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)# init blue button
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)# init yellow button
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)# init green button
GPIO.setup(26, GPIO.OUT)# init yellow LED


#setting up event detection to eliminate holding button or having the program miss the button press.
GPIO.add_event_detect(21, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING)
GPIO.add_event_detect(20, GPIO.RISING)


#weight scale init
hx = HX711(dout_pin=5, pd_sck_pin=6)
onehx= HX711(dout_pin=5, pd_sck_pin=6);
twohx = HX711(dout_pin=23, pd_sck_pin=24);

lcd.text('Setting up ', 1)
lcd.text('Device . .   ', 2)

def zero_scales():
    lcd.clear()
    lcd.text('Set Zero:  ', 1)
    lcd.text('Set Ratio: ', 2)
    err = onehx.zero();
    err = twohx.zero();
    lcd.text('Set Zero: Sucess ', 1)
    lcd.text('Set Ratio: ', 2)
    sleep(2)
    set_calculate_ratio()#calling the ratio so it can be calculated again.

def set_calculate_ratio():
    #Calculate ratio with known weight(Ike dollar coin)
    scale_one_ratio= 10549/22.68 
    scale_two_ratio= 10405/22.68
    
    #Set Ratio
    onehx.set_scale_ratio(scale_one_ratio)
    twohx.set_scale_ratio(scale_two_ratio)
    
#    lcd.clear()
    lcd.text('Set Zero: Sucess', 1)
    lcd.text('Set Ratio:Sucess', 2)
    
def set_max():
    #init max variables from current weight reading
    max_food= converted_reading_1
    max_water= converted_reading_2
    
    #convert float to string
    string_food_max = str(max_food)
    string_water_max = str(max_water)
    
    #preparing LCD messsage with string variable
    message_food_max = "Max Food:  " + string_food_max + " g"
    message_water_max = "Max Water: " + string_water_max + " g"
    
    lcd.clear()
    lcd.text(message_food_max, 1)
    lcd.text(message_water_max, 2)
    sleep(2)
    #return(max_food, max_water)
    
    
#These LCD messages run outside of threaded loop to eliminate LCD conflicts with main Try loop.   
def message_disable_upload():
    lcd.clear()
    lcd.text('Tracking', 1)
    lcd.text('Disabled', 2)
    
    #turn off yellow light
    sleep(3)
def message_set_max_error():
    lcd.clear()
    lcd.text('Set Maximum', 1)
    lcd.text('before tracking', 2)
    sleep(3)
    
def message_enable_upload():
    lcd.clear()
    lcd.text('Tracking', 1)
    lcd.text('Enabled', 2)
    GPIO.output(26, GPIO.HIGH)
    sleep(3)

def upload_data(channel):
    running = True
    #Init counter for tracking number of loops ran
    count = 0
    try:
        while running == True:
            #Check if max variable exist before running upload code. Trigger exception.
            exception_error_check = max_water
            
            #Increment tracker by 1
            count += 1
            #Execute LCD message only once at the start
            if(count == 1):
                message_enable_upload()
            
            
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            #init json file located in same folder as program. Use for credentials.
            SERVICE_ACCOUNT_FILE = 'keys.json'
            creds = None
            creds = service_account.Credentials.from_service_account_file(
                    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

            # The ID of sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1utan0_ss9NDG4OpndFdfr_vF4kjsgwJm2PpTewCRu7Q'


            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            
            #set row dates
            today = date.today()
            d1 = today.strftime("%m/%d/%y")
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            
            #set up row format
            row = [[d1, time, converted_reading_1, converted_reading_2, max_food,max_water]]
            
            #uploading row
            request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range="Sheet1!A2", valueInputOption="USER_ENTERED",
                                      body={"values":row}).execute()              
            sleep(10)
            #Exit loop with Red Button Press
            if not GPIO.input(21):
                #Set running variable to false to exit upload loop
                running = False 
                GPIO.output(26, GPIO.LOW)
                message_disable_upload()
    
    except NameError:
        message_set_max_error()
        #turn off light
        GPIO.output(26, GPIO.LOW)
        running = False

#Init threaded event for upload
GPIO.add_event_detect(13, GPIO.RISING, callback=upload_data,bouncetime=200)

        
lcd.text('Setting up ', 1)
lcd.text('Device . . .', 2)

#executing initial functions
zero_scales()
set_calculate_ratio()

#init upload variable to flase
running = False



#Continuous loop to pull most recent weight reading and catch button press events. 
try:
    i = True
    while i:
        converted_reading_1 = round(onehx.get_weight_mean(30))
        converted_reading_2 = round(twohx.get_weight_mean(30))
    
        #convert float to string for LCD
        string_reading_1 = str(converted_reading_1)
        string_reading_2 = str(converted_reading_2)
        
        #preparing LCD messsage with string variable
        message_scale_1 = "Scale 1: " + string_reading_1 + " g"
        message_scale_2 = "Scale 2: " + string_reading_2 + " g"
        
        lcd.clear()
        lcd.text(message_scale_1, 1)
        lcd.text(message_scale_2, 2)
        
        if GPIO.event_detected(20):
            zero_scales()
            
        if GPIO.event_detected(16):
            set_max()
            max_food= converted_reading_1
            max_water= converted_reading_2
            
except KeyboardInterrupt:
    lcd.clear()
    GPIO.output(26, GPIO.LOW)#turn on light
