
    ###########################################################
    #  Exercise #5
    #
    #  Exercise on grabbing data from a CSV file and putting
    #  it into tuples:
    #    1. Read csv file provided and:
    #        - Get total number of cases in states of interest
    #        - Get date when cases spike in such states
    #    2. Display
    #
    ###########################################################


# imports
import csv

# constants

def read_file(fp):
    '''Reads in file pointer and returns a list of lists (output_list) 
       based on the lines in the CSV document (here, the COVID info file)'''
    
    output_list = []
    
    # Sets reader on csv document and skips header line
    reader = csv.reader(fp)
    next(reader, None)
    
    # For line in csv doc, append to complete list of lines (output_list)
    for line_list in reader:
        output_list.append(line_list)
    
    return output_list

def get_totals(states,data):
    '''Takes in states of interest (states) and data from csv file (data)
       and returns a list of tuples showing total number of cases by state'''
    state_tuples = []
    
    for state in states:
        # Grab all cases numbers within state
        state_data = [line[3] for line in data if state in line]
        
        # Select last case number (cumulative total of all previous)
        tuple_data = state_data[-1]
        
        # Put into tuple with state name, append to list of other tuples
        state_tuple = state, tuple_data
        state_tuples.append(state_tuple)
    
    return state_tuples

def get_spike_dates(states,data):
    '''Takes in states of interest (states) and csv data (data) and returns
       list of tuples showing case spike date with number of cases by state'''

    spike_tuples = []
    
    for state in states:
        max_change = 0
        
        # Grabbing all dates with corresponding case numbers for state
        state_data = [[line[0],line[3]] for line in data if state in line]
        
        # Loop through length of state_data and:
        for i in range(len(state_data)):
            
            # Get two adjacent days to compare (before and after)
            before_list = state_data[i]
            try:
                after_list = state_data[i+1]
            except IndexError: # Ends loop where indexes end
                break
            
            # Get the number of cases on adjacent days and find change
            before_cases = before_list[1] 
            after_cases = after_list[1]
            change = int(after_cases) - int(before_cases)
            
            # If the change found is the greatest change, set spike date to 
            # 'after' date and spike cases to cases on after date
            if change > max_change:
                max_change = change
                spike_date = after_list[0]
        
        # Put spike date and number of cases into tuple with state, append
        spike_tuple = state, spike_date, str(max_change)
        spike_tuples.append(spike_tuple)        
            
    
    return spike_tuples # temoprary return value so main runs


def main():    
    
    # States of interest
    states = ['Michigan','New York','Arizona','Texas','California']
    
    # Initialize file 
    fp = open("covid-19-us-states.csv")
    file_data = read_file(fp)
    
    
    # Display "Total Coronavirus cases by state"
    state_totals = get_totals(states, file_data)
    if state_totals:  # if their values are not None
        print("\nTotal Coronavius cases by state\n")
        print("{:24s} {:10s}".format("State","#Cases"))
        for tup in state_totals:
            print("{:24s} {:2s}".format(tup[0],tup[1]))
            
    
    # Display "Date of coronavirus spike by state"
    state_spikes = get_spike_dates(states, file_data)
    if state_spikes:  # if their values are not None
        print("\nDate of Coronavius spike by State \n")
        print("{:24s} {:10s} {:>8s}".format("State","Date","#Cases"))
        for tup in state_spikes:
            print("{:24s} {:10s} {:>8s}".format(tup[0],tup[1],tup[2]))

if __name__ == "__main__":
    main()
