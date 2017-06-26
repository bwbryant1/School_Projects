"""
Credits = {"author_name": "Brandon Bryant", "date": "3/31/2017", "description": "A short program to perform bitwise operations on RGB values of pixels in a PNG","resources_used":"python 2.7,PIL"}
"""
import sys
import random as rand
from PIL import Image
DEBUG = False
#DEBUG = True

def main_pro():

	mode = "" #We will store bitwise operation here
	filename = "" #name of the PNG
	decrypt = False #This value is telling us whether we need to generate new keys or not. False makes new keys
	for arg in sys.argv: #here we are going to read the sys arguments
		if(arg == "keep_key"):
			decrypt = True
		if(arg == "or"):
			mode = arg
		if(arg == "and"):
			mode = arg
		if(arg == "xor"):
			mode = arg
		if(arg[len(arg)-4::].lower() == ".png" ): #This gets us our filename
			filename = arg
	if DEBUG: print mode,filename,gen_rand() #debug

	#This is the case/switch/if statement structure that calls our bitwise functions
	if mode == "xor" and filename != "":
		xor_op(filename,decrypt)
	elif mode == "or" and filename != "":
		or_op(filename,decrypt)
	elif mode == "and" and filename != "":
		and_op(filename,decrypt)
	else:
		print "ERROR: no mode and/or filetype detected"

def gen_rand():
	return rand.randint(0,255)
	#here we are returning a value 0-255 for bitwise

def open_img(filename): #this function gives us the necessary values to perform bitwise 
	img_old = Image.open(filename)
	img_new = Image.open(filename)
	img_orig_pix = img_old.load()
	img_new_pix = img_new.load()
	row, col = img_old.size
	return {'img_new':img_new,'img_orig_pix':img_orig_pix,'img_new_pix':img_new_pix, 'row':row, 'col':col}

def xor_op(file,decrypt):
	if DEBUG: print "Running XOR"
	img = open_img(file) #Open the image and get size, pixels, and Image file
	if not decrypt: #if decypt is true we will not make new keys
		with open("key_xor.txt", "w") as key_txt:
			for _int in xrange(0,3*img["col"] * img["row"]):
				key_txt.write(str(gen_rand()) + "\n") #this writes a randint to our key file
	key_txt = open("key_xor.txt") #here we open the new key file for reading
	key_txt.seek(0)
	for col in xrange(0,img["col"]):
		for row in xrange(0,img["row"]): #nested for loops gives us each pixel tuple to modify
			zero = img["img_orig_pix"][row,col][0] ^ int(key_txt.readline())
			one = img["img_orig_pix"][row,col][1] ^ int(key_txt.readline())
			two = img["img_orig_pix"][row,col][2] ^ int(key_txt.readline())
			img["img_new_pix"][row,col] =(zero,one,two) #here we use our new RGB values and overwrite the new tuple
	img["img_new"].save("encrypted_xor.png") #this saves our new XOR'd file
	if DEBUG: print 3*img["col"]*img["row"]

def and_op(file,decrypt): # same as above only with AND instead of XOR
	if DEBUG: print "Running AND"
	img = open_img(file)
	if not decrypt:
		with open("key_and.txt", "w") as key_txt:
			for _int in xrange(0,3*img["col"] * img["row"]):
				key_txt.write(str(gen_rand()) + "\n")
	key_txt = open("key_and.txt")
	key_txt.seek(0)
	for col in xrange(0,img["col"]):
		for row in xrange(0,img["row"]):
			zero = img["img_orig_pix"][row,col][0] & int(key_txt.readline())
			one = img["img_orig_pix"][row,col][1] & int(key_txt.readline())
			two = img["img_orig_pix"][row,col][2] & int(key_txt.readline())
			img["img_new_pix"][row,col] =(zero,one,two) 
	img["img_new"].save("encrypted_and.png")
	if DEBUG: print 3*img["col"]*img["row"]


def or_op(file,decrypt): # same as above only with OR instead of XOR
	if DEBUG: print "Running OR"
	img = open_img(file)
	if not decrypt:
		with open("key_or.txt", "w") as key_txt:
			for _int in xrange(0,3*img["col"] * img["row"]):
				key_txt.write(str(gen_rand()) + "\n")
	key_txt = open("key_or.txt")
	key_txt.seek(0)
	for col in xrange(0,img["col"]):
		for row in xrange(0,img["row"]):
			zero = img["img_orig_pix"][row,col][0] | int(key_txt.readline())
			one = img["img_orig_pix"][row,col][1] | int(key_txt.readline())
			two = img["img_orig_pix"][row,col][2] | int(key_txt.readline())
			img["img_new_pix"][row,col] =(zero,one,two) 
	img["img_new"].save("encrypted_or.png")
	if DEBUG: print 3*img["col"]*img["row"]


main_pro() #Run the main program!
