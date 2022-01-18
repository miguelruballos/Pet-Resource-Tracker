#scale and button imports
import RPi.GPIO as GPIO                # import GPIO
from hx711 import HX711                # import the class HX711
from time import sleep
from rpi_lcd import LCD

GPIO.setmode(GPIO.BCM)                 # set GPIO pin mode to BCM numbering
GPIO.setwarnings(False)

lcd = LCD() #init screen

lcd.text('Setting up ', 1)
lcd.text('Device   ', 2)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)#red button setup, currently the state is up.
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#blue button
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)#yellow button
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)#green button


GPIO.setup(19, GPIO.OUT)# Red Button init
GPIO.setup(26, GPIO.OUT)# Yellow Button init

#setting up event detection to eliminate holding button or having the loop miss the button press.
GPIO.add_event_detect(21, GPIO.RISING)
GPIO.add_event_detect(20, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING)
GPIO.add_event_detect(13, GPIO.RISING)

#initializing weight scales
hx = HX711(dout_pin=5, pd_sck_pin=6)
onehx= HX711(dout_pin=5, pd_sck_pin=6);
twohx = HX711(dout_pin=23, pd_sck_pin=24);


def zero_scales():
    lcd.clear()
    lcd.text('Set Zero:  ', 1)
    lcd.text('Set Ratio: ', 2)
    err = onehx.zero()
    err = twohx.zero()
    lcd.text('Set Zero: Sucess ', 1)
    lcd.text('Set Ratio: ', 2)

    sleep(2)
    set_calculate_ratio()#calling the ratio so it can be calculated again.
    

def set_calculate_ratio():
    scale_one_ratio= 10549/22.68 #used ike dollar for ratio
    scale_two_ratio= 10405/22.68

    onehx.set_scale_ratio(scale_one_ratio)
    twohx.set_scale_ratio(scale_two_ratio)
    lcd.text('Set Zero: Sucess', 1)
    lcd.text('Set Ratio:Sucess', 2)
    sleep(2)

def button_blue_press():
    lcd.clear()
    lcd.text('Button 1', 1)
    lcd.text('Pressed', 2)
    sleep(2)
    
def button_red_press():
    lcd.clear()
    lcd.text('Button 3', 1)
    lcd.text('Pressed', 2)
    sleep(2)
    
def button_green_press():
    GPIO.output(26, GPIO.HIGH)#turn on light
    
    lcd.clear()
    lcd.text('Green Light On', 1)
    sleep(2)
    lcd.clear()
    lcd.text('Button 4', 1)
    lcd.text('Pressed', 2)
    sleep(2)
    GPIO.output(26, GPIO.LOW)#turn off light
    lcd.clear()

#executing initial functions
zero_scales()

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
        
        
        if GPIO.event_detected(20):#this is a better solution because the program can detect a push even if it was working on something else.
            lcd.clear()
            lcd.text('Button 2', 1)
            lcd.text('Pressed', 2)
            sleep(2)
            zero_scales()
            

        if GPIO.event_detected(21):
            button_red_press()
    
        if GPIO.event_detected(16):
            button_blue_press()
            
        if GPIO.event_detected(13):
            button_green_press()
           
except KeyboardInterrupt:
    print('interrupted!')
    lcd.clear()
    GPIO.output(26, GPIO.LOW)#turn off light
