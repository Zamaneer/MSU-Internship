#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:40:49 2020

@author: nabilz
"""
# imports

# constants
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

def is_alpha(string):
    for i in string:
        if (i not in ASCII_LOWERCASE) and (i not in ASCII_UPPERCASE):
            return False
    
    return True

def is_digit(string):
    for i in string:
        if (i not in DECIMAL_DIGITS):
            return False
        
    return True


def find_chr(string, find):
    for index,letter in enumerate(string):
        if (find == letter):
            return index
        
    return -1

def replace_chr(string, find, replace):
    for index,letter in enumerate(string):
        if (letter == find):
            string = string[:index] + replace + string[index + 1:]
        
    return string


def to_lower(string):
    for letter in string:
        if (letter in ASCII_UPPERCASE):
            index = find_chr(ASCII_UPPERCASE, letter)
            string = replace_chr(string, letter, ASCII_LOWERCASE[index])
    
    return string

def to_upper(string):
    for letter in string:
        if (letter in ASCII_LOWERCASE):
            index = find_chr(ASCII_LOWERCASE, letter)
            string = replace_chr(string, letter, ASCII_UPPERCASE[index])
    
    return string

def find_str(string, find):
    matches = 0
    
    for i in range(len(string)):
        if matches == len(find):
            return (i-len(find))
        if string[i] == find[i]:
            matches += 1
            print("Found match")
    
    return -1
        