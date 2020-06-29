

    ###########################################################
    #  Project #4
    #
    #  1. Take a file containing GDP data and extract max/min
    #     GDP changes over the period of data contained in file
    #  2. Find years and GDP values associated with those values
    #  3. Print as table to terminal
    #
    ###########################################################


def open_file():
    '''Repeatedly prompt until a valid file name allows the file to be opened.'''
    valid_file = False
    
    while not valid_file:
        file = input("Enter a file name: ")
        
        # Error checking
        try:
            fp = open(file)
            valid_file = True
        except FileNotFoundError:
            print("Please enter a valid file name!")
            
    return fp
 

   
def find_min_percent(line):
    '''Find the min percent change in the line; return the value and the index.'''
    min_change = min_change_index= 10000.00
    
    for n in range(0, 100, 1):
        # Sets index as a function of the first entry and column difference
        index = 79+(12*n)
        
        # Breaks loop at encounter with "", or the end of the list
        try:
            entry = float(line[index:index+12].strip())
        except ValueError:
            break

        # Minimum setter: Replaces minimum and records index found
        if entry < min_change:
            min_change = entry
            min_change_index = index
                     
            
    return min_change, min_change_index
        
    

def find_max_percent(line):
    '''Find the max percent change in the line; return the value and the index.'''
    max_change = max_change_index = 0
    
    for n in range(0, 100, 1):
        index = 79+(12*n)
        
        # Breaks loop at encounter with "", or end of list
        try:
            entry = float(line[index:index+12].strip())
        except ValueError:
            break
        
        # Maximum setter: Replaces maximum and records index found
        if entry > max_change:
            max_change = entry
            max_change_index = index
                     
            
    return max_change, max_change_index



def find_gdp(line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    
    # Adjusts for entry start differences in different lines
    # Returns gdp (or any parameter needed given a line and the index)
    index -= 3
    gdp = float(line[index:index+12].strip())
    return gdp

   
     
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''    
    min_tril_gdp = min_val_gdp * (10**-3)
    max_tril_gdp = max_val_gdp * (10**-3)
    
    print("\nGross Domestic Product")
    print("\n{:<10s}{:>8s}{:>6s}{:>18s}".format("min/max", "change", "year", "GDP (trillions)"))
    print("\n{:<10s}{:>8.1f}{:>6.0f}{:>18.2f}".format("min", min_val, min_year, min_tril_gdp))
    print("\n{:<10s}{:>8.1f}{:>6.0f}{:>18.2f}".format("max", max_val, max_year, max_tril_gdp))
    return



def main():  
    # File input and read lines in file                  
    fp = open_file()
    lines = fp.readlines()
    
    # Find min/max gdp change values
    min_v, min_v_index = find_min_percent(lines[8])
    max_v, max_v_index = find_max_percent(lines[8])
    
    # Find corresponding years
    min_y = find_gdp(lines[42], min_v_index)
    max_y = find_gdp(lines[42], max_v_index)
    
    # Find corresponding gdp values
    min_v_gdp = find_gdp(lines[43], min_v_index)
    max_v_gdp = find_gdp(lines[43], max_v_index)

    # Print to terminal
    display(min_v, min_y, min_v_gdp, max_v, max_y, max_v_gdp)
    
    
    

# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
