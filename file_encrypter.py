#!/usr/bin/env python

"""
Credits = {"author_name": "Brandon Bryant", "date": "4/30/2017", "description": "A short program to perform AES encyption and decryption on a binary file","resources_used":"python 2.7,PyCrypto,Dr.Mulmi's adapted code"}
"""
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
DEBUG = False
#DEBUG = True

# The block size for cipher object; must be 16 bytes (128 bit) for AES.
BLOCK_SIZE = 16

# Pad at the end, so all blocks, including the last one, are 128 bit long.
PAD_WITH = '#'

def main_pro():

	key = "" #We will store value of key here
	filename = "" #name of the file
	decrypt = False #This value is telling us whether we need to encrpyt or decrypt file

	if(sys.argv[1] == "dec"):
		decrypt = True
	if(len(sys.argv[2])) == 16 or 24 or 32: # This will get us our encrpytion key if its the right size
		key = sys.argv[2] # This will get us our encrpytion key if its the right size
		cipher = AES.new(key) #make the cipher object
	else:
		print "key is noy 16 || 24 || 32 bytes"
		sys.exit()
	if(sys.argv[3] != ''): #This gets us our filename
		filename = sys.argv[3]
	else:
		print "please put in a filename"
		sys.exit()

	if DEBUG: print decrypt,filename,key,cipher #debug

	#This is the case/switch/if statement structure that calls our functions
	if decrypt:
		dec_op(filename,cipher,key)
	else:
		enc_op(filename,cipher,key)

# Appends 'PAD_WITH' at the end of plaintext to make it long enough to fully fill all blocks.
def pad(plaintext):
	return plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH

def dec_op(filename,cipher,key):
	f = open(filename,"r")
	hash = f.read(64) #the first 64 bytes are the hash value of key
	new_hash = SHA256.new(key).hexdigest() #this hash value is the hash value of the key value at the command line
	if hash == new_hash: # we make sure the two hashes are the same
		if DEBUG:
			print hash
		ciphertext = f.read()
		f.close()
		filename = "".join(filename.split("_enc")) #we remove _enc from the filename if it exists
	        fn_out = filename.split(".")
	        fn_out = fn_out[0] + "_dec." + fn_out[1] #insert _enc into the filename
	        f = open(fn_out,"w")
		f.write(cipher.decrypt(ciphertext).rstrip(PAD_WITH)) #write out the decrypted content
		f.close()
		print "wrote file: " + fn_out
	else:
		print "key does not match encrypted material"

def enc_op(filename,cipher,key):
	hashed_key = SHA256.new(key).hexdigest() #make the hash value of the inputed key
	f = open(filename,"r") 
	file = f.read() #read in the plaintext
	f.close()
	ciphered = cipher.encrypt(pad(file)) #make the cipher text
	fn_out = filename.split(".")
	fn_out = fn_out[0] + "_enc." + fn_out[1] #append _enc to the filename
	f = open(fn_out,"w")
	f.write(hashed_key) #write the new hash value
	f.write(ciphered) #write the ciphertext
	f.close() #close file
	print "wrote file: " + fn_out

main_pro() # LET's GO
