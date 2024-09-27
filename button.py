pip install RPi.GPIO

import RPi.GPIO as GPIO # import pi GPIO library

def button_callback (channel):
    print("Button was pushed") #should be able to put code here to take input

GPIO.setwarnings(False) #ignore warning
GPIO.setmode(GPIO.BOARD) #use phyiscal pin numbering
#print(GPIO.getmode()) - tells you the numbering of the board
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin 10 to be an input pin
# inital value pulled low (off)

#test the status of the switch
#while(GPIO.input(10) == GPIO.LOW:print("LOW")
#while(GPIO.input(10) == GPIO.HIGH:print("HIGH")


GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) #set up rising, connect to event

#what does the following code do???
message = input("Press enter to quit\n\n") #run until somebody pressed center

GPIO.cleanup() #clean up
#while True: #run forever
 #   if GPIO.input(10) == GPIO.HIGH:
  #      print("Button was pushed!")
        #reads the port and outputs the state
        #this is where we put the code to run the rest of the program
        #instead of printing button was pushed