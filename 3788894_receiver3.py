import radio
from microbit import *

radio.on()
radio.config(address = 23456789)


def convert(string_sum):
    new_Str = ""
    for i in string_sum:
        new_Str = new_Str + i   #reference-https://www.geeksforgeeks.org/sum-of-list-with-string-types-in-python/
    return new_Str

def split(word):
    return [char for char in word]  #reference-https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

while True:

    received = radio.receive()
    if received != None:
        p0 = received[0:]
        sum_of_p0 = (sum(int(c) for c in p0))

        parity_bit_1 = int(received[1:2]) + int(received[3:4]) + int(received[5:6]) + int(received[7:8]) + int(received[9:10]) + int(received[11:])

        parity_bit_2 = int(received[2:3]) + int(received[3:4]) + int(received[6:7]) + int(received[7:8]) + int(received[10:11]) + int(received[11:])

        parity_bit_4 = int(received[4:5]) + int(received[5:6]) + int(received[6:7]) + int(received[7:8])

        parity_bit_8 = int(received[8:9]) + int(received[9:10]) + int(received[10:11]) + int(received[11:])

        if parity_bit_1 % 2 != 0 or parity_bit_2 % 2 != 0 or parity_bit_4 % 2 != 0 or parity_bit_8 % 2 != 0:
            if sum_of_p0 % 2 == 0:
                display.show(Image.SAD)
                sleep(2000)
                display.clear()
                radio.send("Resend")
            elif sum_of_p0 % 2 != 0:
                display.show(Image.CONFUSED)
                sleep(2000)
                display.clear()
                a = 0
                if parity_bit_1 % 2 != 0:
                    a += 1
                if parity_bit_2 % 2 != 0:
                    a += 2
                if parity_bit_4 % 2 != 0:
                    a += 4
                if parity_bit_8 % 2 != 0:
                    a += 8
                display.scroll("Bit # " + str(a)+" has an error")

                binary = split(received)
                if binary[a] == "0":
                    binary[a] = "1"
                else:
                    binary[a] = "0"

                binary_string = convert(binary)
                display.show(Image.HAPPY)
                sleep(2000)
                display.clear()
        else:
            display.show(Image.HAPPY)
            sleep(2000)
            display.clear()