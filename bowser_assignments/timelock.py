#!/usr/bin/env python                                                                                         

#Coded By Philip DeFatta

import os
import sys
import time
import calendar
import hashlib

# epoch local time string
epoch = "2016-01-01 00:00:00"

# now local time string
now = "2016-04-27 12:06:34"

# List of functions that will convert local time to UTC for the epoch and now times
epochstring = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(epoch, "%Y-%m-%d %H:%M:%S"))))

nowstring = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.mktime(time.strptime(now, "%Y-%m-%d %H:%M:%S"))))

# Boolean variable set by the user to see whether they want to use inputed nowstring or the present now
use_nowstring = True

# Booolean variable to see if the epoch is going to have an error 
epoch_error = False

#function to check if the error is going to occur when switching to UTC if the hour is 20 or greater
def errorcheck(timestring1, timestring2): # Once it goes over 23 it adds an extra hour. This checks and compensates
                                          # for this and checks to see if one or both conversions has this problem
    # A pair of if and else statements to retrieve the hors of each inputed time 
    if(not(timestring1[11] == "0")):
        hour1 = timestring1[11:13]

    else:
        hour1 = timestring1[12]

    if(not(timestring2[11] == "0")):
        hour2 = timestring2[11:13]

    else:
        hour2 = timestring2[12]

    # Intialized the counter to 0
    counter = 0
    
    # Checks for the the error mention above and if found it increments the error counter 
    if((int(hour1)) >= 20):
        counter = counter + 1
        epoch_error = True

    if((int(hour2)) >= 20):
        counter = counter + 1
    
    # Returns the amount of errors found
    return counter

# A function that will take care of the double hashing
def double_md5_hash(sec):
    
    # Takes in the perameter and creates it into a string and uses hashlib.md5() to hash it the first time
    sec_string = str(sec)
    hash_mid = hashlib.md5(sec_string).hexdigest()

    # Takes the fist hash from above and creates it into a string and hashes it again
    hash_string = str(hash_mid)
    hash_full = hashlib.md5(hash_string).hexdigest()
    
    # Returns this double hash
    return hash_full

# A function that calculates the timelock code
def timelock_code(code):
    
    # creates a codestring based on the passsed argument and initalizes the index variables
    codestring = str(code)
    index = 0
    answer_size = 0
    answer = ""

    # while loop to search through string to find first two letters starting from the left 
    while(answer_size < 2):

        # Checks to see if the character is a letter and if it is it is going to add it to the answer string and increment
        # the answer size
        if(codestring[index].isalpha()): 
            str1 = codestring[index]
            str2 = answer
            answer = str2 + str1
            answer_size = answer_size + 1

        # increment the index of codestring to the right
        index = index + 1
    

    # start the index at the end of the codestring 
    index = len(code) - 1
    
    # while the answer_size is less than 4 it will add two numbers to the answer starting from the right of the codestring
    while(answer_size < 4):

        # if the character is not a letter then add it to the answer and incremnet the size of the answer
        if(not(code[index].isalpha())):
            str1 = codestring[index]                                                                          
            str2 = answer                                                                                      
            answer = str2 + str1 
            answer_size = answer_size + 1

        # move the index of the codestring to the left
        index = index - 1

    #compact the answer into one string with no spaces
    timecode = ''.join(answer)
    
    # return the time lock code
    return timecode

##################  MAIN LOOP  ##############################

# sees if there are any errors and stores it error
error = errorcheck(epoch,now)

# if to check if we are using the inputed now 
if(use_nowstring == False):
    
    # Takes the epoch time and converts and calculates time since standard epoch in 1970s 
    epochtime = time.strptime(epochstring, '%Y-%m-%d %H:%M:%S')
    timesince_epoch = calendar.timegm(epochtime)

    # Calculates time since standard epoch
    timesince_now = int(time.time())

    # Calculates the mod to subtract by to give a 60 second window for the time code
    mod = timesince_now % 60
    
    # Subtracts the two times since to get the time between the two
    since_epoch = timesince_now - timesince_epoch - mod
    
    # Adds an hour if the error occurs
    if(epoch_error):
        since_epoch = since_epoch + 3600
    
# else if to check if we are using the inputed now
elif(use_nowstring == True):

    # Takes the epoch time and converts and calculates time since standard epoch in 1970s
    epochtime = time.strptime(epochstring, '%Y-%m-%d %H:%M:%S')
    nowtime = time.strptime(nowstring, '%Y-%m-%d %H:%M:%S')
    timesince_epoch = calendar.timegm(epochtime)
    timesince_nowstring = calendar.timegm(nowtime)

    # Subtracts the two times since to get the time between the two
    since_epoch = timesince_nowstring - timesince_epoch

    # Calculates the mod to subtract by to give a 60 second window for the time code
    mod = since_epoch % 60

    # Adds an hour or two based on how many errors occur and subtracts mod
    if(error == 2):
        since_epoch = since_epoch - mod + 7200 
    elif(error == 1):
        since_epoch = since_epoch - mod + 3600
    else:
        since_epoch = since_epoch - mod

# Double hashes the since_epoch seconds
hash_crypt = double_md5_hash(since_epoch)

# Calculates a code based on the double hash
code = timelock_code(hash_crypt)

# Print the code found 
print code

