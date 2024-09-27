from machine import Pin, SPI, ADC
import time
from ili9341 import Display, color565
from neopixel import Neopixel
from xglcd_font import XglcdFont
import random

def starter_sequence():
    display.draw_text(220,55,"Hello!", arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
    display.draw_text(200,240,"Ready to be productive?", arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
    time.sleep(5)
    display.clear()


    display.draw_text(random_comp[0], random_comp[1], random_comp[2], arcadepix, color565(255, 255, 255), background=0, landscape=True, rotate_180=True, spacing=1)
    time.sleep(3)
    display.clear


    soundSensor = ADC(28) # Pin where sensor device (Microphone) is connected

    baseline = 28000 # You may need to change this, but your mic should be reading around here as a baseline.

    while True:
        print(soundSensor.read_u16())

        # If we detect a spike in the waveform greater than a 10% deviation from our baseline, someone is probably talking.
        if soundSensor.read_u16() > baseline:
            strip.fill((255,0,0))
            display.draw_text(170,319,"Consider moving from this area.", arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
            display.draw_text(150,235,"It is a bit loud.", arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)

            strip.show() # Turn the light on if we're detecting a spike
            time.sleep(10)
            strip.fill((0,0,0))
            strip.show()
            time.sleep(1)
            display.clear()
            break
        else:
            strip.fill((0,255,0))
            display.draw_text(170,290,"Good sound level to study", arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)

            strip.show() # Turn the light on if we're detecting a spike
            time.sleep(10)
            strip.fill((0,0,0))
            strip.show()
            time.sleep(1)
            display.clear()
            break
        print('done')

def potent_reading(adc_value):
    global previous_display_text  # Use the global variable to keep track across function calls

    # Calculate the display text based on the adc_value as before
    if adc_value < 8181.625:
        display_text = '30 minutes'
        time_val = int(1800)
    elif adc_value < 16063.25:
        display_text = '1 hour'
        time_val = int(3600)
    elif adc_value < 23944.875:
        display_text = '1 hour and 30 minutes'
        time_val = int(5400)
    elif adc_value < 31826.5:
        display_text = '2 hours'
        time_val = int(7200)
    elif adc_value < 39708.125:
        display_text = '2 hours and 30 minutes'
        time_val = int(9000)
    elif adc_value < 47589.75:
        display_text = '3 hours'
        time_val = int(10800)
    elif adc_value < 55471.375:
        display_text = '3 hours and 30 minutes'
        time_val = int(12600)
    else:
        display_text = '4 hours'
        time_val = int(14400)

    # Clear the previous value by overwriting it with spaces
    # Assuming the maximum length of display_text does not exceed the length of "3 hours and 30 minutes"
    max_length_text = '3 hours and 30 minutes'
    spaces = ' ' * len(max_length_text)
    display.draw_text(50, 250, spaces, arcadepix, color565(0, 0, 0), background=0, landscape=True, rotate_180=True, spacing=1)

    # Now draw the new display text
    display.draw_text(50, 300, display_text, arcadepix, color565(255, 255, 255), background=0, landscape=True, rotate_180=True, spacing=1)

    # Update the previous display text variable
    previous_display_text = display_text
    return time_val

def potent_reading_continuous():
    display.draw_text(200,292,'Turn dial to set total time.', arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
    display.draw_text(180,305,'Hold button when time is set.', arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)

    confirmed = False
    last_adc_value = adc.read_u16()
    while not confirmed:
        adc_value = adc.read_u16()
        # The potent_reading function calculates the time based on adc_value and updates the LCD
        if adc_value != last_adc_value:
            time_val = potent_reading(adc_value)
            last_adc_value = adc_value

        if button.value() == 1:  # If the button is pressed, exit the loop
            confirmed = True
            time.sleep(0.2)  # Debounce delay
            display.clear()  # Optionally clear the display or proceed with your next steps

        time.sleep(1)
    return time_val

def end_sequence():
    
    pass

def break_sequence():
    global elapsed_time
    endtime_list = [12600, 10800, 9000, 7200, 5400, 3600, 1800, 0]
    strip.fill((255,191,0))
    strip.show()
     while True:
        update_timer()
        time.sleep(1)
        if elapsed_time in endtime_list:
            strip.fill((236,234,226))
            strip.show()
            break
        

#function to display countdown on timer
def update_timer():
    global start_time
    global elapsed_time
    #global time_val
    #start_time = time.time() + time_val
    elapsed_time = start_time - time.time()
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    timer_str = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    #display.clear(color565(0, 0, 0)) # Clear the display
    #space_time = ' ' *20
    #display.draw_text(70, 220, space_time, bigfont, color565(0, 0, 0), background=0, landscape=True, rotate_180=True, spacing=1)
    display.draw_text(70, 260, timer_str, bigfont, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1) # Display timer
    strip.fill((236,234,226))
    strip.show()
    return

#new function added to display timer and tasks when magnet is on
def magnet_on():
    global task
    global elapsed_time
    global time_val
    global time_set
    while True:
        #start_time = time.time() + time_val
        #print (time_val)
        update_timer()
        time.sleep(1)

        if button.value():
            task -= 1

        if switch.value() != 1:
            display.clear()
            time_val = elapsed_time
            strip.fill((0,0,0))
            strip.show()
            break

        if task == 0:
            display.clear()
            time_val = elapsed_time
            strip.fill((0,0,0))
            strip.show()
            break

        if elapsed_time == 0:
            display.clear()
            strip.fill((0,0,0))
            strip.show()
            time_set = 0
            break


        #task
        #change font for display number of tasks
        display.draw_text(190,235, "Number of Tasks", arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
        display.draw_text(140,163,str(task), bigfont, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)


complist = [[200,319,"Knowledge comes through failure"], [200,265,"Be proud of yourself!"], [200,311,"You are better than yesterday!"], [200,308,"Everything is going to be okay"], [200,300,"Clowning is always an option"], [200,255,"Hardwork pays off!"], [200,269,"Work now, play later!"], [200,212,"Keep going!"], [200,240,"You will survive!"], [200,243,"You're super hot!"], [200,242,"Mistakes Happen!"], [200,245,"You are so smart!"], [200,253,'You are doing great'], [200,225,"Don't give up!"], [200,250,"You can learn this!"]]
random_comp = random.choice(complist)

switch = Pin(2, Pin.IN, Pin.PULL_DOWN)
button = Pin(1, Pin.IN, Pin.PULL_DOWN)
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
display.clear(color565(0, 0, 0))
arcadepix = XglcdFont('Broadway17x15.c', 17, 15)
bigfont = XglcdFont('Dejavu24x43.c', 24, 43)
display.clear()

numpix = 8
strip = Neopixel(numpix, 1, 0, "GRB")
# strip = Neopixel(numpix, 0, 0, "GRBW")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
#colors = colors_rgbw

step = round(numpix / len(colors))
current_pixel = 0
strip.brightness(100)
strip.fill((0,0,0))
strip.show()

adc = ADC(Pin(26))
time_val = 0
elapsed_time = 0
starter_sequence()
time_set = 0
task = 0
start_time = time.time()

while True:
    if switch.value() == 1:  #magnet # Check if the button is pressed
        display.clear()
#         print (time_val)
        #start_time = time.time() + (time_val)
        start_time = time.time() + (30)
        #t = potent_reading_continuous()
        #start_time = time.time() + time_val #add 10 minutes to timer
        while True:
            magnet_on()
            break

        print('blahblabh')

    else:#no magnet
        print('haha')
        if time_set == 0:

            #potent_reading_continuous()
            time_val = potent_reading_continuous()
            time_set += 1

        display.draw_text(200,308,'Push the button to add tasks.', arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
        display.draw_text(180,298,'Before adding the last task,', arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
        display.draw_text(160,302,'put the magnet on the hand', arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
        display.draw_text(140,265,'and push the button.', arcadepix, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1)
        time.sleep(2)

        mag = switch.value()
        time.sleep(1)

        if mag != 1:
            while True:
                if button.value():
                    task += 1
                    #time.sleep(1)
                    display.clear()
                    display.draw_text(60,160,str(task), bigfont, color565(255, 255, 255), background = 0, landscape=True, rotate_180=True, spacing=1) #change font
                    break




    print(switch.value())
    time.sleep(0.1)  # Short delay to reduce CPU usage