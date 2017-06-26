#!/usr/bin/python
# -*- coding: utf-8 -*-
# Brandon Bryant
import sys,os,base64,binascii,hashlib
def main():
	wrapper_file,output_folder = '',""
	for arg in sys.argv:
	        if arg[0:2] == '-w':
        	    wrapper_file = arg[2::]
	        if arg[0:2] == '-o':
        	    output_folder = arg[2::]		
	if (wrapper_file == '' or output_folder == ''):
		print "You must input a file to analysis and a folder name to output to"
		sys.exit()
	decode(wrapper_file,output_folder)
def decode(w,f):
	filetypes = []
        jpeg = {'header':"ffd8ff",'footer':"ffd9","filetype":".jpeg"}
	jpg = {'header':"ffd8ffe000104a46494600010101004800480000ffe100804578696600004d4d002a000000080004011a0005000000010000003e011b0005000000010000004601280003000000010002000087690004000000010000004e00000000000000480000000100000048000000010003a00100030000000100010000a0020004000000010000018ba003000400000001000002000",'footer':"2a45007fffd9","filetype":".jpg"}
	pdf = {'header':'25504446','footer':'454f460a',"filetype":".pdf"}
	gif = {'header':'47494638','footer':'5a00003b',"filetype":".gif"}
	png = {'header':'89504e47','footer':'49454e44ae426082',"filetype":".png"}
	docx = {'header':'504b0304','footer':'504b0506',"filetype":".docx"}
	filetypes.extend([jpeg,pdf,gif,png,docx,jpg])
	if os.path.exists(w):
                input_file = open(w,"r")
        else:
                sys.exit("file doesn't exist")
	if not os.path.exists(f):
		os.makedirs(f)
	data = input_file.read()
    	decoded = base64.b64decode(data)
	decoded = binascii.hexlify(decoded)
	i,begin,end = 0,0,0
	found_begin,found_end = False,False
	for filetype in filetypes:
		while(i < len(decoded)):
			if (decoded[i:i+(len(filetype["header"]))] == filetype["header"]) and not found_begin:
				begin = i
				found_begin = True
			if (decoded[i:i+(len(filetype["footer"]))] == filetype["footer"]) and not found_end:
				end = i+(len(filetype["footer"]))
				found_end = True
				break
			i = i+1
		if(filetype["filetype"]==".docx"):
			decoded_alt = binascii.unhexlify(decoded[begin:end+(2*18)])
		else:
                        decoded_alt = binascii.unhexlify(decoded[begin:end])			
		a = hashlib.md5()
		a.update(decoded_alt)
		a_md5 = a.hexdigest()
		file = open("./"+f+"/"+a_md5+filetype["filetype"],"w+")
		file.write(decoded_alt)
		file.close()
	        i,begin,end = 0,0,0
	        found_begin,found_end = False,False
main()
