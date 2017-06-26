#!/usr/bin/python

import sys,os,base64,binascii,hashlib

'''=======================================================================
Description:  
Program Name: password_cracker.py
Author:       Brandon Bryant
Version:      1.0 (Written for Python 2.7.11+)
Release Date: 10/09/2016
======================================================================='''



def main():
	find_hash()

def find_hash():
	hash1 = {"Jkirk.zip":"9aeaed51f2b0f6680c4ed4b07fb1a83c"}
	hash2 = {"Lmccoy.zip":"172346606e1d24062e891d537e917a90"}
	hash3 = {"Cchapel.zip":"fa5caf54a500bad246188a8769cb9947"}

	alpha = "abcdefghijklmnopqrstuvwxyz"
	
	file = open("passwords.txt","wb+")	
	
	for _0 in alpha:
		for _1 in alpha:
			for _2 in alpha:
				for _3 in alpha:
					for _4 in alpha:
					
						hashed = hashlib.md5(_0+_1+_2+_3+_4).hexdigest()
						if hashed == (hash1['Jkirk.zip']):
							print "pass: "+_0+_1+_2+_3+_4, str(hash1.items())+"\n"
							
							file.write(str("pass: "+_0+_1+_2+_3+_4+ " "+ str(hash1.items())+"\n"))
						if hashed == (hash2['Lmccoy.zip']):
							print "pass: "+_0+_1+_2+_3+_4, str(hash2.items())+"\n"
							
							file.write(str("pass: "+_0+_1+_2+_3+_4+ " "+ str(hash2.items())+"\n"))
						if hashed == (hash3['Cchapel.zip']):
							print "pass: "+_0+_1+_2+_3+_4, str(hash3.items())+"\n"
							
							file.write(str("pass: "+_0+_1+_2+_3+_4 + " "+str(hash3.items())+"\n"))
	file.close()


if __name__ == "__main__":
    main()
