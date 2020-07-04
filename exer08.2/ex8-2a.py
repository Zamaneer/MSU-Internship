
    ###########################################################
    #  Exercise #8.2A
    #
    #     Demonstrations and testing for Date class
    #
    ###########################################################

import date

A = date.Date( 1, 1, 2014 )

print( A )
print( A.to_iso() )
print( A.to_mdy() )
print( A.is_valid() )
print()

B = date.Date( 12, 31, 2014 )

print( B )
print( B.to_iso() )
print( B.to_mdy() )
print( B.is_valid() )
print()

C = date.Date()

C.from_iso( "2014-07-04" )

print( C )
print( C.to_iso() )
print( C.to_mdy() )
print( C.is_valid() )
print()

D = date.Date()

D.from_mdy( "March 15, 2015" )

print( D )
print( D.to_iso() )
print( D.to_mdy() )
print( D.is_valid() )
print()

E = date.Date()

print( E )
print( E.to_iso() )
print( E.to_mdy() )
print( E.is_valid() )
print()


# Testing __init__ function behavior for erroneous input
F = date.Date(13, 40, 2017)

print(F)
print(F.to_iso())
print(F.is_valid())
# to_mdy causes IndexError, uncomment at your own risk!
#print(F.to_mdy())
print()


# Testing from_iso and from_mdy for strings with spaces 
G = date.Date()

G.from_iso(" 2014  - 07-04")
print(G.is_valid())
print(G)
G.from_mdy("January   5,    2020")
print(G.is_valid())
print(G)
print()


# Testing from_iso and from_mdy for erroneous input
H = date.Date()

H.from_iso("2014-50-10")
print(H)
print(H.is_valid())

H.from_mdy("January   60, 0")
print(H)
print(H.is_valid())

set = [i for i in range(25)]
print(set)
print(int("08"))