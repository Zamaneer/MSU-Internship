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


def add_BMI(read, write):
    """
    Writes previous data to specified file along with calculating BMI and
    addng that as well. 
    read : string
        File to be read and copied
    write : string
        FIle to be written and copied to

    Returns: None.
    
    """
    
    opened_file = open(read, "r")
    write_file = open(write, "w")
    
    
    for index, line in enumerate(opened_file):
        # Catches header and writes to file
        if index == 0:
            write_file.write("{:<12s}{:<12s}{:<12s}{:<12s}"\
                             .format("Name", "Height(m)", "Weight(kg)", "BMI"))
            continue
        
        # Extracts height, weight, name and calculates BMI
        line = line.strip()
        name = line[:12].strip()
        height = float(line[12:24].strip())
        weight = float(line[24:36].strip())
        
        BMI = (weight/(height ** 2))
        
        
        # Writes all parameters to file
        line = "\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
            .format(name, height, weight, BMI)
        write_file.write(line)
    
    
    write_file.write("\n\n")
    
    opened_file.close()
    write_file.close()
    
    return

def add_avg(file):
    """
    Appends the averages of values to file
    file : string
        File to have averages appended to 

    Returns: None

    """
    file.seek(0)
    height_sum = weight_sum = BMI_sum = 0
    
    for index, line in enumerate(file):
    # Sums up height, weight and BMI. Catches for header (ValueError)
        line = line.strip()
        try:
            height_sum += float(line[12:24].strip())
            weight_sum += float(line[24:36].strip())
            BMI_sum += float(line[36:].strip())
        except ValueError:
            continue
    
    entries = index - 1
    
    # Calculation of averages
    avg_height = height_sum/entries
    avg_weight = weight_sum/entries
    avg_BMI = BMI_sum/entries
    
    # Print averages in separate line to end of file
    line = "\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
        .format("Average", avg_height, avg_weight, avg_BMI)
    file.write(line)
    
    
    return



def add_max(file):
    """
    Appends the maximums of values to file
    file : string
        File to have maximums appended to 

    Returns: None

    """
    
    file.seek(0)
    max_height = max_weight = max_BMI = 0
    
    for line in file:
        # Finds height, weight and BMI. Catches for header (ValueError)
        line = line.strip()
        try:
            height = float(line[12:24].strip())
            weight = float(line[24:36].strip())
            BMI = float(line[36:48].strip())
        except ValueError:
            continue
        
        # Compares finds to previous maximums, replaces if greater
        if height > max_height:
            max_height = height
        
        if weight > max_weight:
            max_weight = weight
            
        if BMI > max_BMI:
            max_BMI = BMI
    
    # Prints results as separate maximum line 
    line = "\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
        .format("Max", max_height, max_weight, max_BMI)
    file.write(line)
    
    
    return 


def add_min(file):
    """
    Appends the minimums of values to file
    file : string
        File to have minimums appended to 

    Returns: None

    """
    
    file.seek(0)
    min_height = min_weight = min_BMI = 10**7
    
    for line in file:
        # Finds height, weight and BMI. Catches for header (ValueError)
        line = line.strip()
        try:
            height = float(line[12:24].strip())
            weight = float(line[24:36].strip())
            BMI = float(line[36:48].strip())
        except ValueError:
            continue
        
        # Compares finds to previous minimums, replaces if less
        if height < min_height:
            min_height = height
        
        if weight < min_weight:
            min_weight = weight
            
        if BMI < min_BMI:
            min_BMI = BMI
    
    # Prints results as separate minimum line
    line = "\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}"\
        .format("Min", min_height, min_weight, min_BMI)
    file.write(line)
            
    return 


def create_data(toread, towrite):
    """
    Strings all previous methods together and creates a new data file 
    based on the parameters (BMI, weight, height, name)
    toread : string
        File to read from (for use in add_BMI)

    towrite : string
        File to write to (use in all methods)
    
    Returns: None

    """
    
    add_BMI(toread, towrite)
    
    opened_file = open(towrite, "a+")
    add_avg(opened_file)
    add_max(opened_file)
    add_min(opened_file)
    opened_file.close()




def main():
    create_data("data.txt", "data (copy).txt")



if __name__ == '__main__':
    main()