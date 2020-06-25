#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################
#  Project 3 (To be used with Project 3 library)
#
#  Tests functions in Project 3 library with originals in:
#  python docs. 
#    
###########################################################
# import 
import proj03library

# constants

def main():
    # IS ALPHA TEST
    string_alpha = "Aa1AA"
    library_alpha_test = proj03library.is_alpha(string_alpha)
    python_alpha_test = string_alpha.isalpha()
    print("IS ALPHA TEST")
    print("Test success: " + str((library_alpha_test == python_alpha_test)))
    print("String: " + string_alpha)
    print("Library is_alpha: " + str(library_alpha_test))
    print("Python isalpha: " + str(python_alpha_test))
    print("\n")
    
    
    # IS DIGIT TEST
    string_digit = "1aa"
    library_digit_test = proj03library.is_digit(string_digit)
    python_digit_test = string_digit.isdigit()
    print("IS DIGIT TEST")
    print("Test success: " + str((library_digit_test == python_digit_test)))
    print("String: " + string_digit)
    print("Library is_digit: " + str(library_digit_test))
    print("Python isdigit: " + str(python_digit_test))
    print("\n")
    
    
    # TO LOWER TEST
    string_lower = "STaR"
    library_lower_test = proj03library.to_lower(string_lower)
    python_lower_test = string_lower.lower()
    print("TO LOWER TEST")
    print("Test success: " + str((library_lower_test == python_lower_test)))
    print("String: " + string_lower)
    print("Library is_lower: " + str(library_lower_test))
    print("Python lower: " + str(python_lower_test))
    print("\n")
    
    
    # TO UPPER TEST
    string_upper = "staAr"
    library_upper_test = proj03library.to_upper(string_upper)
    python_upper_test = string_upper.upper()
    print("TO UPPER TEST")
    print("Test success: " + str((library_upper_test == python_upper_test)))
    print("String: " + string_upper)
    print("Library is_upper: " + str(library_upper_test))
    print("Python upper: " + str(python_upper_test))
    print("\n")
    
    
    # FIND CHR TEST
    string_findchr = "steered"
    char_findchr = "e"
    library_findchr_test = proj03library.find_chr(string_findchr, char_findchr)
    python_findchr_test = string_findchr.find(char_findchr)
    print("FIND CHR TEST")
    print("Test success: " + str((library_findchr_test == python_findchr_test)))
    print("String: " + string_findchr)
    print("Find: " + char_findchr)
    print("Library findchr: " + str(library_findchr_test))
    print("Python find: " + str(python_findchr_test))
    print("\n")
    
    
    
    # FIND STR TEST
    string_findstr = "wonton"
    to_findstr = "on"
    library_findstr_test = proj03library.find_str(string_findstr, to_findstr)
    python_findstr_test = string_findstr.find(to_findstr)
    print("FIND STR TEST")
    print("Test success: " + str((library_findstr_test == python_findstr_test)))
    print("String: " + string_findstr)
    print("Find: " + to_findstr)
    print("Library findstr: " + str(library_findstr_test))
    print("Python find: " + str(python_findstr_test))
    print("\n")
    
    
    
    # REPLACE CHR TEST
    string_rep = "banana"
    rep_char = "a"
    instead_char = "u"
    library_repchr_test = proj03library.replace_chr(string_rep, rep_char, instead_char)
    python_repchr_test = string_rep.replace(rep_char, instead_char)
    print("REPLACE CHR TEST")
    print("Test success: " + str((library_repchr_test == python_repchr_test)))
    print("String: " + string_rep)
    print("Find: " + rep_char)
    print("Replace with: " + instead_char )
    print("Library replace_chr: " + str(library_repchr_test))
    print("Python replace: " + str(python_repchr_test))
    print("\n")
    
    
    
    # REPLACE STR TEST
    string_rep = "banana"
    rep_str = "na"
    instead_str = "nuh"
    library_repstr_test = proj03library.replace_str(string_rep, rep_str, instead_str)
    python_repstr_test = string_rep.replace(rep_str, instead_str)
    print("REPLACE STR TEST")
    print("Test success: " + str((library_repstr_test == python_repstr_test)))
    print("String: " + string_rep)
    print("Find: " + rep_str)
    print("Replace with: " + instead_str )
    print("Library replace_str: " + str(library_repstr_test))
    print("Python replace: " + str(python_repstr_test))
    print("\n")


if __name__ == '__main__':
    main()


