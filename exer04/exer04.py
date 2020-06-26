#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    ###########################################################
    #  Exercise #4
    #
    #  A two part exercise on data input/output:
    #    1. Read data of individual weights and heights and
    #        - Get average
    #        - Get highest/lowest
    #        - Calculate BMI
    #        - Append to file
    #    2. Write output from 1 to another file
    #
    ###########################################################

# imports

# constants


def add_BMI(file):
    opened_file = open(file, "a+")
    
    for line in opened_file:
        line = line.strip()
        name = line[:12].strip
        try:
            height= float(line[12:24].strip())
            weight= float(line[24:36].strip())                       
        except ValueError:
            continue
        
        BMI = str(weight/height ** 2)
        line = "{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name, height, weight, BMI)
        
        opened_file.close()  
        
    return

def find_avg(file):
    opened_file = open(file, "r")
    weight_sum = height_sum = BMI_sum = 0
    
    for line, text in enumerate(opened_file, 0):
        text = text.strip()
        
        try:
            height_sum += float(text[12:24].strip())
            weight_sum += float(text[24:36].strip())
            BMI_sum += float(text[36:48].strip())
        except ValueError:
            continue
        
        entries = line
    
    opened_file.close()
    
    height_average = height_sum/entries
    weight_average = weight_sum/entries
    BMI_average = BMI_sum/entries
    
    
    return str(height_average), str(weight_average), str(BMI_average)



def find_max(file):
    opened_file = open(file, "r")
    max_height = max_weight = max_BMI = 0
    
    for line in opened_file:
        line = line.strip()
        try:
            height = float(line[12:24].strip())
            weight = float(line[24:36].strip())
            BMI = float(line[36:48].strip())
        except ValueError:
            continue
        
        if height > max_height:
            max_height = height
        
        if weight > max_weight:
            max_weight = weight
            
        if BMI > max_BMI:
            max_BMI = BMI
            
    return str(max_height), str(max_weight), str(max_BMI)


def find_min(file):
    opened_file = open(file, "r")
    min_height = min_weight = min_BMI = 10**7
    
    for line in opened_file:
        line = line.strip()
        try:
            height = float(line[12:24].strip())
            weight = float(line[24:36].strip())
            BMI = float(line[36:48].strip())
        except ValueError:
            continue
        
        if height < min_height:
            min_height = height
        
        if weight < min_weight:
            min_weight = weight
            
        if BMI < min_BMI:
            min_BMI = BMI
            
    return str(min_height), str(min_weight), str(min_BMI)

add_BMI("data (copy).txt")
print(find_avg("data (copy).txt"))
print(find_max("data (copy).txt"))
print(find_min("data (copy).txt"))


