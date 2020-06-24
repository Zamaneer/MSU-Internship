###########################################################
#  Exercise #3 - Nabil Zaman, 6/24/20
#
#  Four functions:
#    1, Leap year: Checks if a year is a leap year
#    2. Rotate: Takes a specified amount of letters at  
#       the end of a string and puts them to its front
#    3. Digit Count: Counts the number of even digits,
#       odd digits, and zeroes in a number
#    4, Float check: Checks if a string is a float
#
###########################################################

# imports

# constants


# LEAP YEAR FUNCTION
def leap_year(year):
    year = int(year)
    
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return True
    else: 
        return False


# ROTATE FUNCTION
def rotate(s,n):
    
    if n <= len(s):
        s = s[-n:] + s[:(len(s) - n)]
    else:
        print("Invalid!")

    return s


# DIGIT COUNT FUNCTION
def digit_count(num):
    num = map(int, str(int(num)))  
    zeroes = evens = odds = 0
    
    for digit in num:
        if (digit == 0):
            zeroes += 1
        elif (digit % 2 == 0) and (digit != 0):
            evens += 1
        else:
            odds += 1
    
    return [evens, odds, zeroes]
        

# FLOAT CHECK FUNCTION
def float_check(num):
    alphas = [digit for digit in num if digit.isdigit() == False]
    
    if (0 <= alphas.count(".") < 2)\
        and ((len(alphas)) - alphas.count(".") == 0):
            
        return True
    else:
        return False

 
# MAIN FUNCTION       
def main():
    print(leap_year("1896"))
    print(rotate('abcdefg', 3))
    print(rotate('abcdefg', 8))
    print(digit_count(1234567890123))
    print(digit_count(123400.345))
    print(float_check('1234'))
    print(float_check('123.45'))
    print(float_check('123.45.67')) 
    print(float_check('34e46')) 
    print(float_check('.45')) 
    print(float_check('45.'))
    print(float_check('45..'))


if __name__ == '__main__':
    main()