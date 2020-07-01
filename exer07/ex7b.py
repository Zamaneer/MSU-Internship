
    ###########################################################
    #  Exercise #7B
    #
    #  1. Take files containing continent, country, and city
    #     names and put them into a nested dictionary with sets
    #  2. Print in a readable format to terminal
    #
    ###########################################################

def build_map( in_file1, in_file2 ):
    '''Builds nested dictionary containing information about continents,
       their countries, and their cities given files with that data (in_file1 
       and in_file2). Returns dictionary object (data_map)'''
    data_map = {}
    
    in_file1.readline()
    in_file2.readline()

    #READ EACH LINE FROM FILE 1
    for line in in_file1:

        # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        # Ignore empty strings
        if continent != "":
            # If current continent not in map, insert it 
            if continent not in data_map:
                data_map[continent] = {}
            # If country is not empty insert (continent is guaranteed to be in map)
            if country != "": 
            
                 # If current country not in map, insert it 
                 if country not in data_map[continent]:
                     data_map[continent][country] = set()

    #READ EACH LINE FROM FILE 2        
    for line in in_file2:

        # Split the line into two words
        countries_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            for continent in data_map:
                if country in data_map[continent]:
                    data_map[continent][country].add(city)
    return data_map

def display_map( data_map ):
    '''Displays information from data_map dictionary in a readable format
       Returns nothing.'''
    # Displays a sorted nested dictionary
    continents_list = sorted(list(data_map)) #sorted list of the continent keys
    # For each continent
    for continents in continents_list:
          print("{}:".format(continents)) #continents in continents_list
          countries_list = sorted(list(data_map[continents])) #sorted list of the countries keys in the continents
          # For each country
          for countries in countries_list:
                print("{:>10s} --> ".format(countries),end = '') #countries in countries_list
                cities = sorted(list(data_map[continents][countries])) #sorted list of the cities
                # For each city 
                for city in cities:  
                      #As long as not last city, add a comma and a space after the cities names
                      if city is not cities[-1]:
                         print('{}, '.format(city),end = '') # city in cities                      
                      # if it is the last, don't add a comma and a space.
                      else:
                         print('{}'.format(city)) # city in cities

def open_file():
    '''Prompts user to enter file name and returns a file object (in_file) of
       that file'''
    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()
