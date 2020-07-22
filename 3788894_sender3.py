import radio
import random

from random import seed
from random import randint
from microbit import *
seed(1)
radio.on()
radio.config(address = 23456789)

without_error = "110010101001"
length = len(without_error)
without_error_reversed = ''.join(reversed(without_error))

single_error = "011010101110"
length = len(single_error)
single_error_reversed = ''.join(reversed(single_error))

double_error = "011111001000"
length = len(double_error)
double_error_reversed = ''.join(reversed(double_error))

send_rand = [without_error,single_error,double_error]
stepper=0
while True:
    if button_a.was_pressed():


        radio.send(send_rand[stepper])
        stepper=stepper+1
        if stepper==3:
            stepper=0
    received = radio.receive()
    #if received != None:
     #   radio.send(without_error)