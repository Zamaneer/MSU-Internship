

    ###########################################################
    #  Project #5
    #
    #  1. Take a file containing AWI data
    #  2. Find income ranges, percents, and other data 
    #  3. Print to terminal, graph, provide options to user
    #     allowing them to use functions to analyze
    #
    ###########################################################
    
# imports
import pylab

# constants

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
    
    
def open_file():
    '''Asks user to input a year and opens the corresponding data file. Returns
       file (fp - file object) and year inputted (year_str - str)'''
    valid_file = False
    
    while not valid_file:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        
        # Checks for input error (year not in range)
        if 1990 <= int(year_str) <= 2015:
            
            # Checks for file not found error, opens otherwise
            try:
                yearfile_str = "year" + year_str + ".txt"
                fp = open(yearfile_str)
                valid_file = True
            except FileNotFoundError:
                print("Error in file name: " + yearfile_str + " Please try again")
        
        else:
            print("Error in year. Please try again.")
            
    return fp, year_str
    

    
def read_file(fp):
    '''Reads in file provided (fp) and returns list of lines in file (final_lines)'''
    final_lines = []
    file_lines = fp.readlines()[2:]  # Starts at 2 to disregard headers 
    
    for line in file_lines:
        new_sep = []
        sep_line = line.split()
        del sep_line[1]  # Delete "-" separating range
        
        # Remove commas, cast all values to floats, and build new line
        for number in sep_line:
            if number.isalpha() == False:
                number = float(number.replace(",",""))
            new_sep.append(number)
                
       
        final_lines.append(new_sep)  # Append new line to master list
              
    return final_lines
        


def find_average(data_lst):
    '''Returns the average income (average_income - float) calculated from data (data_lst)'''
    cumulative_income = 0
    
    # Find total income of all ranges 
    for line in data_lst:
        cumulative_income += line[5]
    
    # Find the total number of people across all ranges
    last_entry = data_lst[-1]
    cumulative_individuals = last_entry[3]
    
    # Calculate average income from previous
    average_income = cumulative_income/cumulative_individuals
    
    return average_income
    


def find_median(data_lst):
    '''Returns the median income (median_income - float) calculated from data (data_lst)'''
    MEDIAN_PERCENT = 50   # Percent of people below, above median
    
    median_tuple = get_range(data_lst, MEDIAN_PERCENT)
    median_income = median_tuple[2]  # Index 2 of tuple is income
    
    return median_income
    

    
def get_range(data_lst, percent):
    '''Given data (data_lst) and percent of people below income range (percent - float)
       returns a tuple containing the income range, cumulative percent, and average
       income (range_tuple). Returns nothing if invalid'''
    
    # Finding the first instance of line within percent
    for line in data_lst:
        if line[4] >= percent:
            salary_range = line[0], line[1]
            range_tuple = salary_range, line[4], line[6]
            return range_tuple
    
    return



def get_percent(data_lst,salary):
    '''Given data (data_lst) and income (salary - float) returns a tuple 
       with the percent of people below that income and the income range.
       Returns nothing if invalid.'''
   
    for line in data_lst:
        
        # If valid, find line with income in range and make tuple
        try:
            if line[0] <= salary <= line[1]:
                salary_range = line[0], line[1]
                percent_tuple = salary_range, line[4]
                return percent_tuple
            
        # Condition for last range between 50,000,000 and over
        except TypeError:
            salary_range = line[0], line[1]
            percent_tuple = salary_range, line[4]
            return percent_tuple
    
    return



def main():
    # Open file and read data
    fp, year = open_file()
    data = read_file(fp)
    
    # Determine year, average, and median
    avg = find_average(data)
    median = find_median(data)
    
    # Print data
    print("\n{:<4s}  {:<13s}  {:<13s}".format("Year", "Mean", "Median"))
    print("{:4s}  ${:<13,.2f} ${:<13,.2f}".format(year, avg, median))

    # Ask to plot and plot
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
    
         #determine x_vals, a list of floats -- use the lowest 40 income ranges
         x_vals = []
         for i in range(39):
             select_line = data[i]
             x_vals.append(select_line[0])
         #determine y_vales, a list of floats of the same length as x_vals
         y_vals = []
         for i in range(39):
             select_line = data[i]
             y_vals.append(select_line[4])

         do_plot(x_vals,y_vals,year)
    
    
    choice = " "
    while choice:    
        
        # Additional user actions
        choice = input("Enter a choice to get (r)ange, (p)ercent, or return to stop: ")
        
        # Choice is (r)ange, find percent incomes below level
        if choice == "r":
            input_percent = input("Enter a income percent level: ")
            
            if input_percent.isdigit() == True and 0 <= float(input_percent) <= 100:
                    input_percent = float(input_percent)
                    rangetofind = get_range(data, input_percent)
                    rangefound = rangetofind[2]
                    print("{:4.2f}% of incomes are below ${:<13,.2f}"\
                          .format(input_percent, rangefound))
            
            else:  # If input is not a percent value
                print("Error in percent. Please try again.")
            
                
        # Choice is (p)ercent, find where income lies 
        elif choice == "p":
            input_income = input("Enter an income value: ")
            
            if input_income.isdigit() == True and float(input_income) >= 0.01: 
                    input_income = float(input_income)
                    percent = get_percent(data, input_income)
                    percentfound = percent[1]
                    print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes."\
                          .format(input_income, percentfound))
                
            else:   # If input is not an income value
                print("Error: Income must be positive")
         
            
        # Choice is invalid, tell and reloop
        elif choice != "":
            print("Error in selection.")
            
            
            

if __name__ == "__main__":
    main()