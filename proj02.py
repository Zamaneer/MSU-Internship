#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:50:04 2020

@author: nabilz
"""

end_program = False
end_alignment = False


# MAIN LOOP
while end_program == False:
    
    print("Enter 'quit' to end the program")
    error = "Please enter a valid input!"
    
    # Sequences input
    seq_A_str = (input("Enter DNA sequence A: ")).upper()
    seq_B_str = (input("Enter DNA sequence B: ")).upper()
    
    # Main loop ender
    if seq_A_str == "QUIT" or seq_B_str == "QUIT":
        end_program = True
        continue
    
    # User instructions 
    print("""
Codes:
    
    "a" - Add an indel. 
        Input in form "a(sequence)(index)"
        Example: aB2 = Add indel on sequence B before the current index 2
        
    "d" - Delete an indel
        Input in form "d(sequence)(index)"
        Example: aA5 = Delete indel on sequence A at index 5
        
    "s" - Score the present alignment
    
    "q" - Stop the process


              """)
              
    print("DNA Sequence A: " + seq_A_str)
    print("DNA Sequence B: " + seq_B_str)
    
    # SEQUENCE LOOP (AFTER USER HAS ENTERED SEQUENCES)         
    while end_alignment == False:
        
        # Variables for later use
        lengthA = range(len(seq_A_str))
        lengthB = range(len(seq_B_str))
        
        # Action input
        user_action_str = (input("Enter action desired: ")).lower()
        
        
        # Add indel function
        if user_action_str[0] == "a":
            sequence = user_action_str[1]
            try:
                index = int(user_action_str[2])
            except ValueError:
                print(error)
                continue
            
            if sequence == "a":
                seq_A_str = seq_A_str[:index] + "-" + seq_A_str[index:]
            elif sequence == "b":
                seq_B_str = seq_B_str[:index] + "-" + seq_B_str[index:]
            else:
                print(error)
                continue
            
            print("Sequence A: " + seq_A_str)
            print("Sequence B: " + seq_B_str)
                
        
        # Delete indel function
        elif user_action_str[0] == "d":
            
            sequence = user_action_str[1]
            try:
                index = int(user_action_str[2])
            except ValueError:
                print(error)
                continue
            
            if sequence == "a" and seq_A_str[index] == "-":
                seq_A_str = seq_A_str[:(index)] + seq_A_str[(index+1):]
            elif sequence == "b" and seq_B_str[index] == "-":
                seq_B_str = seq_B_str[:(index)] + seq_B_str[(index+1):]
            else:
                print(error)
                continue
            
            print("Sequence A: " + seq_A_str)
            print("Sequence B: " + seq_B_str)
        
        # Compare sequences function
        elif user_action_str[0] == "s":
            matches = mismatches = 0
            lengthA = range(len(seq_A_str))
            lengthB = range(len(seq_B_str))
            comp_A_str = comp_B_str = ""
            
            # Find the bigger sequence and set it as the range to be used
            if lengthA[-1] > lengthB[-1]:
                comp_range = lengthA
            elif lengthA[-1] < lengthB[-1]:
                comp_range = lengthB
            else:
                comp_range = lengthA
            
            # Comparison loop 
            for i in comp_range:
                letter_A = seq_A_str[i]
                letter_B = seq_B_str[i]
                
                # Add indels wherever needed to compensate for blanks                    
                if letter_A.isalpha() == True and letter_B == "":
                    seq_B_str += "-"
                    
                elif letter_B.isalpha() == True and letter_A == "":
                    seq_A_str += "-"
                
                # Finding matches and mismatches    
                if letter_A == letter_B:
                    matches += 1
                    comp_A_str += letter_A
                    comp_B_str += letter_B
                
                elif letter_A != letter_B:
                    mismatches += 1
                    comp_A_str += letter_A.lower()
                    comp_B_str += letter_B.lower()
                    
            print("Sequence A: " + comp_A_str + "\nSequence B: " + comp_B_str)
            print("Matches: " + str(matches) + "\nMismatches: " + str(mismatches))
        
        # Quit function
        elif user_action_str[0] == "q":
            end_alignment = True
            continue
        
        # Bad input
        else:
            print(error)
            
        
        
