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

def chrCheck(text):

    global textStatus

    for char in text:
        if char.isalpha():
            textStatus = "go"
        elif char.isdigit():
            textStatus = "go"
        elif char == " ":
            textStatus = "go"
        else:
            textStatus = "no-go"
            break
    
    if textStatus == "no-go":
        return True
    elif textStatus == "go":
        return False


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
                    sleep(1)
                    print()
                    print()
                    spclPrint("ERROR: Invalid input.", "red")
                    sleep(0.1)
                    spclPrint("Input not recognised.", "red")
                    print()
                    print()
                    sleep(3)
                
            if answer == "YES":
                break
            else:
                pass
        
        elif chrCheck(plainText):
            sleep(1)
            print()
            print()
            spclPrint("ERROR: Invalid input type.", "red")
            sleep(0.1)
            spclPrint("Only accepts digits and alpha characters", "red")
            print()
            print()
            sleep(3)

        else:
            plainText = plainText.lower()
            plainText = plainText.replace(" ", "")
            break