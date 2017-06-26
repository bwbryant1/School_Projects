#!/usr/bin/env python

#Coded by Philip DeFatta

import sys
import os

# Takes the inputed plain_text and places it into plain_text
plain_text = sys.stdin.read()

# Retrieves the file named key
the_file = open(sys.argv[1])

# Then reads the file and stores it into key
key = the_file.read()

#print key

# A funtion to XOR the plain_text and key
def xor_strings(plain_text, key):

    # Link: http://stackoverflow.com/questions/2612720/how-to-do-bitwise-exclusive-or-of-two-strings-in-python
    # Converts both the plain_text and the key into strings
    plain_text_string = str(plain_text)
    key_string  = str(key)

    # Create three byte arrays and input plain_text_string into one and key_string in the other
    b1 = bytearray(plain_text_string)
    b2 = bytearray(key_string)

    # Create a sepreate byte array to put the answer into
    b = bytearray(len(b1))

    # XOR each byte and put it into the answer bytearray
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]

    # Returns the answer
    return b[0:len(b)-1]

############### Main Loop ####################

# If the plain_text and the key are the same size then it will calculate the XOR 
if(len(plain_text) == len(key)):

    xor = xor_strings(plain_text, key)
    
    # prints the xor
    print xor

# If not it will print an error string
else:
    print "Sorry text and key differ in length"
