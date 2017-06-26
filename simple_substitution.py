#!/usr/bin/env python
"""
Credits = {"author_name": "Brandon Bryant", "date": "3/24/2017", "description": "A short program designed to encrypt and decrypt casesar and keyword ciphers","resources_used":"python 2.7"}
"""
import sys

for line in sys.stdin: #Let's take in the standard input
    stdin = line
    stdin = stdin.lower()
    break

def main_pro(): #Here we run the main program


    cipher = 0 #True is caesar False is Keyword #Casesar or Keyword cipher?
    operation = 0 #True is encrypt False is decrypt #Encrypt or Decrypt?
    key = str(sys.argv[3]).lower() #Make the string lowercase
    for arg in sys.argv: #loop through variables and set argument conditions
        if(arg == "c"):
            cipher = True
            #print "running cipher"
        if(arg == "k"):
            cipher = False
            #print "Running Keyword"
        if(arg == "enc"):
            operation = True
            #print "running enc"
        if(arg == "dec"):
            operation = False
            #print "running dec"
    #print "this is the key: " + key
    #print "stdin: "+ stdin

    if cipher: cipherRun(operation,key)
    if not cipher: keywordRun(operation,key)

def cipherRun(method,key):
    #print method,key
    out = ""
    if method: #encryption
        for char in stdin:
            if char.isalpha() != True:
		out = out + char
                continue
            _ord = ord(char)
            if _ord - int(key) < 97:
                _ord = _ord + 26
                _ord = _ord - int(key)
            else:
                _ord = _ord - int(key)
            out = out + chr(_ord)
    if not method:
        for char in stdin:
            if char.isalpha() != True:
                out = out + char
                continue
            _ord = ord(char)
            if _ord + int(key) > 122:
                _ord = _ord - 26
                _ord = _ord + int(key)
            else:
                _ord = _ord + int(key)
            out = out + chr(_ord)
    if method: #If we were encrypting lets write ciphertext
        with open("ciphertext.txt", 'w') as f:
            f.write(out)
            print "Made ciphertext.txt"
    else: #Else lets write the plaintext
        with open("plaintext.txt", 'w') as f:
            f.write(out)	
            print "Made plaintext.txt"

def keywordRun(method,key):
    #print method,key
    b = 'abcdefghijklmnopqrstuvwxyz'

    out = ""
    cont = False
    for _a in b:
        for _b in key:
            if _b == _a:
                cont = True
        if cont:
            cont = False
            continue
        out = out + _a

    cipAlpha = key + out
    #print cipAlpha
    #print b
    out = ""
    if True:
        for _a in stdin:
            if _a.isalpha() != True:
                out = out + _a
                continue
            if method:
                out = out + cipAlpha[b.find(_a)]
            else:
                out = out + b[cipAlpha.find(_a)]
            #print _a,
	

    if method:
        with open("ciphertext.txt", 'w') as f:
            f.write(out)
            print "Made ciphertext.txt"
    else:
        with open("plaintext.txt", 'w') as f:
            f.write(out)	
            print "Made plaintext.txt"


main_pro()
#Not my most concise code but I think it serves it's purpose :)
