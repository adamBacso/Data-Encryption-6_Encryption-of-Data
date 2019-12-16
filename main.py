"""
File: Data Encryption 6_Encryption of Data

Patterson-cypher
"""

#
# IMPORT

import time
import os
import random

from termcolor import colored

#
# FUNCTIONS DEFINED

def sleep(x):
    time.sleep(x)

def clear():
    os.system('clear')

def title(x, y = ""):
    sleep(2)

    chrCount = len(x)

    clear()

    print()
    print()
    print((("~" * chrCount) + "~~~~").center(50))
    print(x.center(50))
    print(y.center(50))
    print((("~" * chrCount) + "~~~~").center(50))
    print()
    print()
    sleep(0.5)

def spclPrint(text, color = 'white'):

    for char in text:
        print(colored(char, color), end = "", flush = True)

        if char == " ":
            time.sleep(0.09)
        else:
            time.sleep(0.07)
    
    print()


#
# IPO

sleep(2)
clear()

while True:

    while True:
        title('Encryption of Data', 'Patterson-Cypher')
        spclPrint("Enter text to be encoded (no special characters,")
        spclPrint("e.g. punctuations, #, &, (), $, %, ...). Press")
        spclPrint("enter to Quit:")
        print()
        plainText = input()

        if plainText == "":

            while True:
                print()
                spclPrint("Warning!", "red")
                spclPrint("You are about to terminate the program.", "red")
                spclPrint("Do you wish to procede (yes/no):", "red")
                answer = input()
                answer = answer.upper()

                if answer in ['YES', 'NO']:
                    break
                else:
                    print()
                    print()
                    spclPrint("ERROR: Invalid input.", "red")
                    sleep(0.1)
                    spclPrint("Input not ")