import datetime
import os
from time import sleep
from os import system, name


def _copyright():
    __author__ = 'Edy-edu For HezCaSy Inc.'
    __copyright__ = 'Copyright (C) 2023 HezNom Cipher'
    __Version__ = 'Hez.1.0.23'
    __license__ = "Public Domain"
    now = datetime.datetime.now()
    print(f"Author:{__author__}\n{__copyright__}\nLicense:{__license__}\nVersion: {__Version__}\n{now}")


def main_header():  # Defines the header displays
    print("===================================HezNom Cipher===========================================")
    print("         ==    ==  ====== =======   ===       ==   = = = ===  ===          ===")
    print("         ==    ==  ==          =    ==  =     ==   ==     ==  == =       =  ==")
    print("         ========  =====      =     ==    =   ==   ==     ==  ==   =   =    ==")
    print("         ==    ==  ==        =      ==      = ==   ==     ==  ==     =      ==")
    print("         ==    ==  ======  =======  ==       ===   =========  ==            ==")
    _copyright()


main_header()  # calls the main_header function for execution


def _error():
    print("Invalid input!!! Type in a valid choice.")
    sleep(3)
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    main_prog()


def _continue():
    print("\nRun successfully!!\nWould you like to continue?(Type C or exit to quit)")
    ui2 = str(input("Choose here:"))
    if ui2 == 'C':
        main_prog()
    elif ui2 == 'exit':
        print("===========Exited HezNom Cipher Successfully!==========")
        pass
    else:
        _error()


def main_prog():  # main program body begins
    print("[+]What would you like to do:\n[+]Type E to encrypt\n[+]Type D to decrypt\n[+]Type exit to quit the program")
    ui1 = str(input("Choose here: "))
    if ui1 == 'E':
        def encryption():  # encryption function
            text = str(input("Enter your text: "))  # normal text
            key = int(input("Key: "))
            # key0 = str(key)
            # if len(key0) == 6:
            output = ""
            for char in text:  # for each character in the text entered,
                output += chr(ord(char) ^ key)  # ord finds the scode. chr turns scode back to character
                if len(output) == len(text):
                    print(output)
                    _continue()
        encryption()
    elif ui1 == 'D':
        def decryption():  # decryption  function
            cypher_text = input("Enter encrypted text:")
            key1 = int(input("Enter your key:"))
            # key00 = str(key1)
            # if len(key00) == 6:
            output1 = ""
            for char in cypher_text:
                output1 += chr(ord(char) ^ key1)
                if len(output1) == len(cypher_text):
                    print(output1)
                    _continue()
        decryption()
    elif ui1 == 'exit':
        def exit_program():
            print("===========Exited HezNom Cipher Successfully!==========")
            pass
        exit_program()
    else:
        _error()


if __name__ == "__main__":
    main_prog()
