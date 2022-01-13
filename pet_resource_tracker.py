from __future__ import print_function
#scale and button imports
from gpiozero import Button
import RPi.GPIO as GPIO                # import GPIO
from hx711 import HX711                # import the class HX711
from time import sleep
from rpi_lcd import LCD

#api imports

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


GPIO.setmode(GPIO.BCM)                 # set GPIO pin mode to BCM numbering
GPIO.setwarnings(False)

lcd = LCD() #initializing screen

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)#red button setup, currently the state is up.
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#blue button
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)#yellow button
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)#green button
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


#setting up event detection to eliminate holding button or having the program miss the button press.
GPIO.add_event_detect(21, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING)
#GPIO.add_event_detect(13, GPIO.RISING)
GPIO.add_event_detect(20, GPIO.RISING)





hx = HX711(dout_pin=5, pd_sck_pin=6)
GPIO.setmode(GPIO.BCM);
onehx= HX711(dout_pin=5, pd_sck_pin=6);
twohx = HX711(dout_pin=23, pd_sck_pin=24);



def zero_scales():    
    err = onehx.zero();
    err = twohx.zero();
    set_calculate_ratio()#calling the ratio so it can be calculated again.

def set_calculate_ratio():
    scale_one_ratio= 10549/22.68 #used ike dollar for ratio
    scale_two_ratio= 10405/22.68

    onehx.set_scale_ratio(scale_one_ratio)
    twohx.set_scale_ratio(scale_two_ratio)
    
def set_max():
    max_food= converted_reading_1
    max_water= converted_reading_2
    #print('max food: ', max_food, 'max water: ' ,max_water)
    lcd.clear()
    string_food_max = str(max_food)#Converting to string to be able to print it on LCD
    string_water_max = str(max_water)#Converting to string to be able to print it on LCD
    message_food_max = "Max Food: " + string_food_max + " g"
    message_water_max = "Max Water: " + string_water_max + " g"
    lcd.text(message_food_max, 1)
    lcd.text(message_water_max, 2)
    sleep(2)
    lcd.clear()
    return(max_food, max_water)

running = False #setting state for upload_data()


def upload_data(channel):
    lcd.clear()
    #print(running, "test2")
    lcd.text('Initilizing Tracking...', 1)
    sleep(2)
    lcd.clear()
    running = True
    try:
        while running == True:
            GPIO.output(26, GPIO.HIGH)#turn on light
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            SERVICE_ACCOUNT_FILE = 'keys.json'

            creds = None
            creds = service_account.Credentials.from_service_account_file(
                    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

            # The ID and range of a sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1utan0_ss9NDG4OpndFdfr_vF4kjsgwJm2PpTewCRu7Q'


            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            
            #setting up rows
            today = date.today()
            d1 = today.strftime("%m/%d/%y")
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            
            row = [[d1, time, converted_reading_1, converted_reading_2, max_food,max_water]]
            
            #uploading rows
            request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range="Sheet1!A2", valueInputOption="USER_ENTERED",
                                      body={"values":row}).execute()
            #Exit the loop by making running False with green button.
            if not GPIO.input(21):
                running = False
                lcd.clear()
                lcd.text('Tracking ended', 1)
                sleep(2)
                lcd.clear()
                GPIO.output(26, GPIO.LOW)#turn on light

            sleep(10)
    except NameError:
                lcd.clear()
                lcd.text('Set maximum', 1)
                lcd.text('before tracking', 2)
                sleep(2)
                lcd.clear()
                GPIO.output(26, GPIO.LOW)#turn on light


GPIO.add_event_detect(13, GPIO.RISING, callback=upload_data,bouncetime=200)
        


#executing initial functions
zero_scales()
set_calculate_ratio()


try:
    i = True
    while i:
        converted_reading_1 = round(onehx.get_weight_mean(30))
        converted_reading_2 = round(twohx.get_weight_mean(30))
    
        string_reading_1 = str(converted_reading_1)#Converting to string to be able to print it on LCD
        string_reading_2 = str(converted_reading_2)#Converting to string to be able to print it on LCD
        
        lcd.clear()
        message_scale_1 = "Scale 1: " + string_reading_1 + " g"
        message_scale_2 = "Scale 2: " + string_reading_2 + " g"
        lcd.text(message_scale_1, 1)
        lcd.text(message_scale_2, 2)
        
        #if not GPIO.input(21):#this is another option to caputre the button input but it can be missed by the program.
        #GPIO.output(19, GPIO.HIGH)#turn on light
        if GPIO.event_detected(20):#this is a better solution because the program can detect a push even if it was working on something else.
            zero_scales()
            lcd.clear()
            lcd.text('Zeroing', 1)
            lcd.text('Successfull', 2)
            sleep(2)
            #GPIO.output(19, GPIO.LOW)#turn off light
            lcd.clear()
        if GPIO.event_detected(16):
            set_max()
            max_food= converted_reading_1
            max_water= converted_reading_2
            sleep(1)
except KeyboardInterrupt:
    print('interrupted!')
    lcd.clear()
    GPIO.output(26, GPIO.LOW)#turn on light
