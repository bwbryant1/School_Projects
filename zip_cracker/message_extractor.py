#!/usr/bin/python
'''=======================================================================
Description:  
Program Name: message_extractor.py
Author:       Brandon Bryant
Version:      1.0 (Written for Python 2.7.11+)
Release Date: 10/10/2016
======================================================================='''
from PIL import Image
import sys

image1 = Image.open("mountain (copy).png")
image2 = Image.open("DCIM_2837.png")

red1,green1,blue1 = image1.split()
red2,green2,blue2 = image2.split()

red_pixels = list(red1.getdata())
green_pixels = list(green2.getdata())
arr1 = []
arr2 = []

for _each in red_pixels:
	arr1.append(str(int(_each & 1)))
for _each in green_pixels:
	arr2.append(str(int(_each & 1)))

str1 = ''.join(arr1)
str2 = ''.join(arr2)

byte_arr = []
byte = result = ""     

output = str1

for a in output:
	if len(byte) < 8:
		byte += a
	else:
		byte_arr.append(byte)
		byte = a

for each_byte in byte_arr:                
	result += chr(int(each_byte,2))

print result




