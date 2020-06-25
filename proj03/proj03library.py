#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################
#  Project 3 Library (To be used with Project 3)
#
#  Contains various functions dealing with strings:
#    is_alpha: Tells if string has all alphabetical characters
#    is_digit: Tells if string has all digit characters
#    find_char: Finds a character in string
#    find_str: Finds string in string
#    replace_chr: Replaces characters in strin
#    replace_str: Replaces strings in strings
#    
###########################################################
# imports

# constants
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"



def is_alpha(string):
    """
    Tells if a string has all alphabetical characters
    string:  The string to be assessed (str)
    Returns:  Truth of statement "string is totally alphabetical" (bool)
    """
    for i in string:
        if (i not in ASCII_LOWERCASE) and (i not in ASCII_UPPERCASE):
            return False
    
    return True



def is_digit(string):
    """
    Tells if a string has all digit characters
    string:  The string to be assessed (str)
    Returns:  Truth of statement "string is totally numeric" (bool)
    """
    for i in string:
        if (i not in DECIMAL_DIGITS):
            return False
        
    return True




def find_chr(string, find):
    """
    Finds a character within a string and returns index
    string:  The string to be scanned(str)
    find:  Character to be found in string, single element (str)
    Returns:  Lowest index where character is found in string (int) or
              -1 if character is not found within string
    """
    for index,letter in enumerate(string):
        if (find == letter):
            return index
        
    return -1



def replace_chr(string, find, replace):
    """
    Finds a letter in a string and replaces with another letter
    string:  The string to have letter replaced (str)
    find:  The letter to be replaced, single element (str)
    replace:  The replacement letter, single element (Str)
    Returns:  'string' where all instances of 'find' are replaced with 
              'replace' (str)
    """
    for index,letter in enumerate(string):
        if (letter == find):
            string = string[:index] + replace + string[index + 1:]
        
    return string




def to_lower(string):
    """
    Turns all uppercase letters in a string to lowercase
    string:  The string to be lowercased (str)
    Returns:  Original string with all letters lowercased (str)
    """
    for letter in string:
        if (letter in ASCII_UPPERCASE):
            index = find_chr(ASCII_UPPERCASE, letter)
            string = replace_chr(string, letter, ASCII_LOWERCASE[index])
    
    return string




def to_upper(string):
    """
    Turns all lowercase letters in a string to uppercase
    string:  The string to be uppercased (str)
    Returns:  Original string with all letters uppercased (str)
    """
    for letter in string:
        if (letter in ASCII_LOWERCASE):
            index = find_chr(ASCII_LOWERCASE, letter)
            string = replace_chr(string, letter, ASCII_UPPERCASE[index])
    
    return string




def find_str(string, find):
    """
    Finds a string within another string and returns lowest index of
    discovery, returns int
    string:  The string to be scanned(str)
    find:  String to be found in string, multiple elements (str)
    Returns:  Lowest index where string is found in string (int) or
              -1 if string is not found within string
    """
    matches = 0
    
    for i in range(len(string)):
        for letter in find:
            
            # Find matches between strings and count them
            if string[i + matches] == letter:
                matches += 1
            else:
                break
            
            # Stop and return lowest index if enough letters match
            if matches == len(letter):
                index = (i - matches) + 1
                return index
    
    # Else, return -1
    return -1 




def replace_str(string, find, replace):
    """
    Finds a string in a string and replaces with another string
    string:  The target string to have string replaced (str)
    find:  The string to be replaced, multiple elements (str)
    replace:  The replacement string, multiple elements (Str)
    Returns:  'string' where all instances of 'find' are replaced with 
              'replace' (str)
    """
    temp_string = ""
    index = 0
    
    while index != -1 :
        
        # Find lowest index of what is to be replaced in target string
        index = find_str(string, find)
        
        # If found,
        # 1. create new string up to already scanned with replacement
        # 2. slice old string to not include already scanned
        if index != -1: 
            temp_string += string[:index] + replace
            string = string[index+len(find):]
            
    # Add on all elements not added at end of loop and return modified    
    string = temp_string + string
    return string
        
        