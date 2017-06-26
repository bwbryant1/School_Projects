#!/usr/bin/python
# -*- coding: utf-8 -*-
# Brandon Bryant
# for Team Bowser

import sys
import os
import math

# our main program which parses arguments and the passes them
#   to the appropriate 
def main_pro():

    offset = 0
    Byte_method = False
    interval = 0
    wrapper_file = ''
    hidden_file = ''
    interval = 1

    for arg in sys.argv:
        if arg == '-b':
            Byte_method = False

        if arg == '-B':
            Byte_method = True

        if arg[0:2] == '-o':
            offset = arg[2::]

        if arg[0:2] == '-i':
            interval = arg[2::]

        if arg[0:2] == '-w':
            wrapper_file = arg[2::]

        if arg[0:2] == '-h':
            hidden_file = arg[2::]

        if arg[0:2] == '-r':
            storing = False

        if arg[0:2] == '-s':
            storing = True

    if storing == True:
        run_encode(Byte_method, interval, offset, hidden_file,
                   wrapper_file)
    elif storing == False:
        run_decode(Byte_method, interval, offset, wrapper_file)


def run_encode( Byte_method, interva, offse,file_hidden,file_wrapper,):

    offset = int(offse)
    interval = int(interva)
    h = open(file_hidden, 'r')
    w = open(file_wrapper, 'r')
    statwrapper = os.stat(file_wrapper)
    stathidden = os.stat(file_hidden)
    hfilesize = stathidden.st_size  #calculate the hidden filesize
    wfilesize = statwrapper.st_size #calculate the wrapper filesize
    sentinel = '\x00\xff\x00\x00\xff\x00'

    if(Byte_method): # Do byte method encoding if 
        data_buff = "" # you are using Byte_method
        data_buff = w.read()
        data_buff_list = list(data_buff) # break the file into multiple bytes
        last_location = 0
        for x in xrange(0,hfilesize*interval-1,interval): #loop over each byte
            data_buff_list[offset + x] = (h.read(1))
            last_location = x
        for x in xrange(1,len(sentinel)+1):  # encode the sentinel
            data_buff_list[offset + last_location +(interval * x)] = sentinel[x-1]
        
        data_buff = ''.join(data_buff_list)
        sys.stdout.write(data_buff)

    elif not Byte_method: #run the bit method encoding
        w_con = w.read()
        h_con = h.read()
        byte_list_wrapper = list(w_con)
        byte_list_hidden = list(h_con)
        count = 0
        for curr_byte in byte_list_hidden:  # use nested for loops to loop over each bit in the hidden file
            for each_bit in format(ord(curr_byte),'08b'):
                if(int(each_bit) == 1):
                    byte_list_wrapper[offset + count] = chr(0b1 | ord(byte_list_wrapper[offset + count]))
                    count += 1
                elif(int(each_bit) == 0):
                    byte_list_wrapper[offset + count] = chr(0b0 & ord(byte_list_wrapper[offset + count]))
                    count += 1
        for curr_byte in sentinel:
            for each_bit in format(ord(curr_byte),'08b'):
                if(int(each_bit) == 1):
                    byte_list_wrapper[offset + count] = chr(0b1 | ord(byte_list_wrapper[offset + count]))
                    count += 1
                elif(int(each_bit) == 0):
                    byte_list_wrapper[offset + count] = chr(0b0 & ord(byte_list_wrapper[offset + count]))
                    count += 1

        data_buff = ''.join(byte_list_wrapper) # join the broken file into one string
        sys.stdout.write(data_buff) # output the string

def run_decode(
    Byte_method,
    interval,
    offset,
    file,
    ):
    f = open(file, 'r')  # open the file to be decoded
    f.seek(int(offset), 0) # seek to the beginning
    statfile = os.stat(file) # calculate the filesize
    filesize = statfile.st_size
    if Byte_method == True: # run Byte decoding mode 
        i = 0 
        file_tot = ''
        buff = ''
        sentinel = '\x00\xff\x00\x00\xff\x00'
        sb = 0
        buff_f = ''
        while i < filesize: 
            byte = f.read(0b1)  #read in one byte
            if byte == sentinel[sb:sb + 0b1]: #keep adding byte if they equal the next byte in sequence
                sb += 0b1
                buff += byte
            else:
                buff = '' #delete byte if sequence is wrong
                sb = 0

            f.seek(-0b1, 0b1)
            buff_f += byte
            if buff == sentinel: # break if sentinel was found

                # sys.exit()

                break
            f.seek(int(interval), 0b1)
            i = f.tell()
        sys.stdout.write(buff_f[0:len(buff_f) - 6:0b1]) # print out the last contents of the buffer minus the sentinel
    else:
        i = 0
        j = 0
        byte = 0
        sentinel = '\x00\xff\x00\x00\xff\x00'
        buff = ''
        index = 0
        sb = 0
        buff_f = ''
        while i < filesize:
            first_bit = ord(f.read(0b1)) & 0b1 # check the first_bit if it is 1 or 0
            f.seek(-0b1, 0b1)
            for x in range(8): # loop 8 times to extract 8 bit
                byte = byte << 0b1
                bit = f.read(0b1)
                f.seek(-1,1)
                f.seek(int(interval),1)
                if bit == '':
                    bit = ' '
                bit = ord(bit) & 0b1
                byte += bit
                i = f.tell()
                if x == 7 and first_bit == 0: # assert the bit if it needed to be off to begin with
                    byte = byte & 0b01111111
            buff_f += chr(byte)

            byte = 0
        for x in range(len(buff_f)):  # this is the loop to check for the sentinel
            if buff_f[x:x + 6] == sentinel:
                sys.stdout.write(buff_f[0:x]) 
                sys.exit() 
        # YOU WILL NOT GET ANY OUTPUT IF THE SENTINEL WAS NOT FOUND
        # Uncomment if you were expecting some output
        #sys.stdout.write(buff_f)


main_pro()
