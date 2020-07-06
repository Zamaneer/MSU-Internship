

    ###########################################################
    #  Exercise #8.2B
    #
    #     Source code for created Time class and testing 
    #
    ###########################################################


# TIME CLASS SOURCE CODE
class Time(object):
    
    __hour = [i for i in range(24)]
    
    __mins = [i for i in range(60)]
    
    __secs = [i for i in range(60)]
    
    def __init__(self, hour = 0, minute = 0, sec = 0 ):
        
        '''Construct a Time using three integers '''
        
        self.__hour = hour
        self.__minute = minute
        self.__sec = sec
        
    def __repr__(self):
        
        '''Return a string to formally represent a Time'''
        
        rep_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__minute, self.__sec)

        return rep_str
    
    def __str__(self):
        
        '''Return a human-readable string representation of a Time'''
        
        hum_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__minute, self.__sec)

        return hum_str
    
    def from_str(self, time_str):
        
        '''Convert a string in form hh:mm:ss to a Time'''
        
        hour, minute, sec = [int(i) for i in time_str.split(":")]
        
        self.__hour = hour
        self.__minute = minute
        self.__sec = sec
               

# TIME CLASS TESTING
def main():
    A = Time( 12, 25, 30 )
    
    print( A )
    print( repr( A ) )
    print( str( A ) )
    print()
    
    B = Time( 2, 25, 3 )
    
    print( B )
    print( repr( B ) )
    print( str( B ) )
    print()
    
    C = Time( 2, 25 )
    
    print( C )
    print( repr( C ) )
    print( str( C ) )
    print()
    
    D = Time()
    
    print( D )
    print( repr( D ) )
    print( str( D ) )
    print()
    
    D.from_str( "03:09:19" )
    
    print( D )
    print( repr( D ) )
    print( str( D ) )

if __name__ == "__main__":
    main()


