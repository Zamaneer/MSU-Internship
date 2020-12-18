#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:08:11 2020

@author: nabilz
"""
end = False

while (end == False):
    
    #USER INPUT
    input_phrase_str = input("Enter phrase to piglatinate: ")
    lower_phrase_str = input_phrase_str.lower()
    
    VOWELS = "aeiou"
    
    #LOGIC
    #Condition for word starting with a vowel (such as "away")
    if lower_phrase_str[0] in VOWELS:
        pig_latinate_str = lower_phrase_str +"way"
    
    #Condition for word starting with consonant (such as "consonant")
    elif (lower_phrase_str[0] not in VOWELS) \
        and (lower_phrase_str[0].isalpha() == True):
        
        #Method: Check each letter until vowel, slice, and append at end
        for letter in lower_phrase_str:
            if not (letter in VOWELS):
                pig_latinate_str=lower_phrase_str[1:]
                pig_latinate_str += letter
            else:
                break
        
        pig_latinate_str += "ay"
    
    #Bad input catcher
    else:
        print("Please enter a valid word!")
        continue
    
    print(pig_latinate_str)
    
    #REDO INPUT AND PROCESSING
    quit_str = input("Input 'quit' to stop: ")
    mod_quit_str = quit_str.lower()
    if mod_quit_str == "quit":
        end = True
        
    
