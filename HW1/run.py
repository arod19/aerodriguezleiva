"""
Angel Rodriguez

Homework #1: Classic Ciphers

A command line python program that asks the user if he/she wants
to decrypt or encrypt a text file, giving several options for
different ciphers.

29 August 2018
"""


import argparse
from utilitybelt import change_charset

# program description
parser = argparse.ArgumentParser(description="encrypt or decrypt a file")

#first group, to either decrypt or encrypt
group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--decrypt", action="store_true")
group.add_argument("-e", "--encrypt", action="store_true")

#second group, to choose between the 5 ciphers
group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-c", "--caesar", action="store_true", help="Caesar cipher.")
group2.add_argument("-v", "--vigenere", action="store_true", help="Vigenere cipher.")
group2.add_argument("-s", "--substitution", action="store_true", help="Substitution cipher.")
group2.add_argument("-t", "--transpose", action="store_true", help="Tranposition cipher.")
#group2.add_argument("-t", "--transpose", action="store_true", help="Caesar cipher.")

# for the file
parser.add_argument("filename", type=str, help="file")



args = parser.parse_args()



with open(args.filename) as file:
    text = file.read()

#start of the Caesar cipher
def Caesar(command):

    shift = 3

#key, shift is 3
    if command == "d":
        shift = -3


    translated = ""

    for letter in text:
        #to deal with special symbols
        if letter.isalpha():
            number = ord(letter)
            number = number + shift

            #to deal with going "off" the alphabet, such as before A or after Z
            if letter.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif letter.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26

                    #algorithm
            translated += chr(number)
        else:
            translated += letter

            #output
    return translated

#Vigenere cipher
def Vigenere(command):
    #hello
    #dogdo
    #3

    #just to represent the key and how it compares to the plain text
    translated2 = ""
    lenK = (len(text) -1) - text.count(' ')
    dog = (   "dog" * (  int(lenK/3)   )     )

    if (len(dog) != lenK ):
        dog = dog + "d"

    if (len(dog) != lenK ):
        dog = dog + "o"

    i = 0

    for letter in text:

#algortihm
        shift = (  ord(dog[i]) -  ord(letter)     )
        if (command == "d"):
            shift = -shift
        #print(shift)
        i = i+1

        if (i==(len(text) - 1)):
            i=i-1

        for letter in text:
            number = ( 97 + shift         )

        #print(chr(number))
        translated2 += (chr(number))


    #print(number)
    return(translated2) #output

def Substitution(command):

    translated3 = ""

#key
    regular = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    scrambled = "LFWOAYUISVKMNXPBDCRJTQEGHZ"

    i=0

    for letter in text.upper():

        if (command =="d"):
            #algorithm
            if letter in regular:
                index = regular.find(letter)

                #print(index)
                translated3+=(scrambled[index])
        else:
            if letter in scrambled:
                index = scrambled.find(letter)

                #print(index)
                translated3+=(regular[index])

    return translated3 #output

def Transpose(command):
    def split(sequence, length):
        return [sequence[i:i + length] for i in range(0, len(sequence), length)]

        def encode():
            #algorithm
            key = 4321
            order = { int(value): number for number, value in enumerate(key) }
            translated4 = ""

            for index in sorted(order.keys()):
                for part in split(text, 4):
                    try:
                        translated4 += part[order[index]]
                    except IndexError:
                        continue
            return translated4


        return(encode()) #output

#Th3 m05t fun 0f th3m 4ll !
def LeetSpeak():

    translated5 = ""

#much like the substitution one, very easy to crack but the most fun definetely.
    regular = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    scrambled = "46<}3FG#!JX1MN0?QR$7UVWXYZ"

    i=0

    for letter in text.upper():


        if letter in regular:
            index = regular.find(letter)

            #print(index)
            translated5+=(scrambled[index])


    return translated5 #output


# what to do with user input

# if user wants to decrypt
if args.decrypt:
    if (args.caesar):
        print(Caesar("d"))
    elif (args.vigenere):
        print(Vigenere("d"))
    elif (args.substitution):
        print(Substitution("d"))
    elif (args.transpose):
        print(Transpose("d"))
    else:
        print(LeetSpeak())

else:
    # if user wants to encrypt
    if (args.caesar):
        print(Caesar("e"))
    elif (args.vigenere):
        print(Vigenere("e"))
    elif (args.substitution):
        print(Substitution("e"))
    elif (args.transpose):
        print(Transpose("e"))
    else:
        print(LeetSpeak())
