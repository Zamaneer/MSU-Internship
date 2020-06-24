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
    
    # Main loop ender/bad input catcher
    if seq_A_str == "QUIT" or seq_B_str == "QUIT":
        end_program = True
        continue
    
    # User instructions 
    print("""
Codes:
    
    "a" - Add an indel. 

    "d" - Delete an indel
        
    "s" - Score the present alignment
    
    "q" - Stop the process
              """)
              
    
    # SEQUENCE LOOP (AFTER USER HAS ENTERED SEQUENCES)         
    while end_alignment == False:
        
        print("" + "\nSequence A: " + seq_A_str + "\nSequence B: " + seq_B_str)
        
        # Variables for later use
        lengthA = len(seq_A_str)
        lengthB = len(seq_B_str)
        
        # Action input
        user_action_str = (input("Enter action desired: ")).lower()
        
        
        # Add indel function
        if user_action_str[0] == "a":
            sequence = (input("Sequence to add indel: ")).lower()
            index = int(input("Index to add indel before: "))
            
            if sequence == "a" and index in range(lengthA):
                seq_A_str = seq_A_str[:index] + "-" + seq_A_str[index:]
            elif sequence == "b" and index in range(lengthB):
                seq_B_str = seq_B_str[:index] + "-" + seq_B_str[index:]
            else:
                print(error)
                continue
                
        
        # Delete indel function
        elif user_action_str[0] == "d":
            sequence = (input("Sequence to delete indel: ")).lower()
            index = int(input("Index to delete indel: "))
            
            if sequence == "a" and seq_A_str[index] == "-":
                seq_A_str = seq_A_str[:(index)] + seq_A_str[(index+1):]
            elif sequence == "b" and seq_B_str[index] == "-":
                seq_B_str = seq_B_str[:(index)] + seq_B_str[(index+1):]
            else:
                print(error)
                continue
        
        # Compare sequences function
        elif user_action_str[0] == "s":
            matches = mismatches = 0
            comp_A_str = seq_A_str
            comp_B_str = seq_B_str
            
            # Find the bigger sequence and set it as the range to be used
            # Add indels wherever needed to compensate for blanks  
            if lengthA < lengthB:
                comp_range = range(lengthB)
                comp_A_str += ("-" * (lengthB - lengthA))
            else:
                comp_range = range(lengthA)
                comp_B_str += ("-" * (lengthA - lengthB))

            
            # Comparison loop 
            for i in comp_range:
                letter_A = comp_A_str[i]
                letter_B = comp_B_str[i]
                
                # Finding matches and mismatches    
                if letter_A == letter_B and (letter_A.isalpha() == letter_B.isalpha()):
                    matches += 1
                    comp_A_str = comp_A_str[:i] + letter_A.lower() + comp_A_str[i+1:]
                    comp_B_str = comp_B_str[:i] + letter_B.lower() + comp_B_str[i+1:]
                
                else:
                    mismatches += 1
                    
                    
            print("Compared A: " + comp_A_str + "\nCompared B: " + comp_B_str)
            print("Matches: " + str(matches) + "\nMismatches: " + str(mismatches))
        
        # Quit function
        elif user_action_str[0] == "q":
            end_alignment = True
            continue
        
        # Bad input
        else:
            print(error)
            
            
        
        
