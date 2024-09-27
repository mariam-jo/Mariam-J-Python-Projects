# ENDG 233 F23
# Hardware Project
# Mariam Joseph
# main.py
# See corresponding project handout for further instructions.

import machine
import time

# Provided dictionary for morse code encoding.
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# These constants time values allow us to determine the length of time each on/off pulse will be transmitted.
TIME_UNIT = 0.1;
DOT = 1;
DASH = 3;
LETTER_SPACE = 3;
WORD_SPACE = 7;

output_string = "ENDG 233 is complete "

# Both LED pin and the GPIO pin are being sent the signal simultaneously. This allows you to test your code via the built-in LED
# while also remaining compatible with the grading decoder.

led_pin = machine.Pin('LED', machine.Pin.OUT)
output_pin = machine.Pin(16, machine.Pin.OUT)

# This provided function will send the data that represents a dot.
def dot():
    led_pin.on()
    output_pin.on()
    time.sleep(TIME_UNIT*DOT)
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT)

# This provided function will send the data that represents a dash.
def dash():
    led_pin.on()
    output_pin.on()
    time.sleep(TIME_UNIT*DASH)
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT)

# This provided function will send the data that represent a space between letters.
def letter_space():
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT*LETTER_SPACE)

# This provided function will send the data that represent a space between words.
def word_space():
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT*WORD_SPACE)


# Complete your code within the main function.
def main():    
    time.sleep(1) # Used to help with board timing
    fixed_string = output_string.upper()
    new_string = ''
    for x in fixed_string:
        if x in morse_code:
            new_string += morse_code[x] + 'l'
        elif x == ' ':
            new_string += 'w'
    print(new_string)
    
    for i in new_string:
        if i == '.':
           dot()
        elif i == '-':
            dash()
        elif i =='l':
            letter_space()
        elif i == 'w':
            word_space()
            
if __name__ == "__main__":
    main()
    
