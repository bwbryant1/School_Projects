#!/usr/bin/env python
import sys

""" Debug Mode """
DEBUG = False   # prints useful information

"""     Set the key for the message     """
key_g = str(sys.argv[2])        # set global key to the third CLI argument
key_g = "".join(key_g.split())  # remove all spaces from the string
key_length = len(key_g)         # compute the string length of the global key
current_key_index = 0           # used to keep track of which character is being used from the key

""" Placeholder for new generated message   """
temp_string = ""                # This will hold the final computed string

"""     Handle the user input   """
def parse_arguments():          # This definition handles whether the user wants to encrpyt or decrypt
    for args in sys.argv:       # We loop over all of the arguments passed into CLI
        if(str(args) == "-e"):  # Checks if we find encryption mode
            
            if(DEBUG):
                print "found encrypt"
            
            return True         # Return True to the global "are we encrypting" boolean
        
        elif(str(args) == "-d"):# Checks if user wants decryption mode
            
            if(DEBUG):
                print "found decrypt"
        
            return False        # Assign False to the global "are we encrypting" boolean

encrypt = parse_arguments()     # This is the Global "are we encrypting" boolean


"""     Definition for shifting the letter in encrypt mode      """
def shift_letter_encrypt(character,key): 
    
    character_correct = 65      # ord("A") returns 65; This makes the shifting easier to understand

    switched_case = False       # If we switch a character in the message to UPPER case set this to true
                                ##      if we switched every letter in the message to upper case we can apply   
                                ##      the same math instead of having to deal with UPPER and LOWER case

    switch_key = False          # Similar to the message switch boolean
    
    if(DEBUG):
        print "shift_letter_encrypt(", character,",", key,")", "<< Function call"
    
    if(ord(character) > 90):            # ord("Z") is 90 which is the last UPPERcase alpha character we wish to deal with
                                        # ord("a") is 91
        character = character.upper()   # here we change the character to upper case
        switched_case = True            # we set our switched message boolean to True

    if(ord(key) > 90):                  # if the letter in the key is LOWERcase change to UPPERcase
        key = key.upper()

    shift_amount = ord(key) - character_correct         # Here we grab the shift value of the key
    old_character = ord(character) - character_correct  # Here we grab the shift value of the character
    new_character = old_character + shift_amount        # Here we actually shift the character
     
    if (new_character) > 25 :                           # this if statement controls the rotate or wrap around of the shifting
            new_character -= 26

    if(switched_case):                  # Now finally is we changed from LOWER to UPPER we need to change back to LOWER
        character = character.lower()
        return chr(new_character + 97)  # We will return a LOWERcase letter so the appropriate character correct is needed "97"
    
    return chr(new_character + 65)      # If we didnt change case we can just return the UPPERcase letter that has been shifted


"""      Definition for shifting letter in decrypt mode      """
def shift_letter_decrypt(character,key):
    
    character_correct = 65
    switched_case = False
    switch_key = False

    if(DEBUG):
        print "shift_letter_decrypt(",character,",",key,")","<< Function call"

    if(ord(character)> 90):
        character = character.upper()
        switched_case = True

    if(ord(key) > 90):
        key = key.upper()
   
    shift_amount = ord(key) - character_correct
    old_character = ord(character) - character_correct
    new_character = old_character - shift_amount

    if (new_character < 0):
       new_character += 26

    if(switched_case):
        character = character.lower()
        return chr(new_character + 97)

    return chr(new_character + 65)

""" MAIN """
while(1):
    
    try:
        message = raw_input()
    except KeyboardInterrupt:
        print ""
        print "Goodbye Dr.Gourd! >>", "Team Bowser Rules! <<"
        exit(0)

    if message != "":
        for each_character in message:
            if each_character.isalpha():
                
                if encrypt:
                    each_character = shift_letter_encrypt(each_character,key_g[current_key_index])
                elif not encrypt:
                    each_character = shift_letter_decrypt(each_character,key_g[current_key_index])

                if(current_key_index + 1 == key_length):    
                    current_key_index = 0
                    if(DEBUG):
                        print "reset index"
                else:
                    current_key_index += 1
                    if (DEBUG):
                        print "added one to index: ", current_key_index
                if(DEBUG):
                    print ""
                    print "subsititued current character with >> " , each_character
                    print ""
                temp_string += each_character
    
            else:
                each_character = each_character
                temp_string += each_character

        print temp_string
    
    elif message == "":
        print "No message entered!"
        exit(0)

    """     Cleanup     """
    temp_string = ""
    current_key_index = 0

"""     End of File     """
