import pandas as pd
import numpy as np

# create a Series with an arbitrary list, the indexes will be 0...4
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])

print s
print s[0]

#Alternatively, you can specify an index to use when creating the Series.
s = pd.Series(
    [7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
    index=['A', 'Z', 'C', 'Y', 'E']
)

print s
print s['Y']

# The Series constructor can convert a dictonary as well, using the keys of 
# the dictionary as its index.
d = {
    'Chicago': 1000,
    'New York': 1300,
    'Portland': 900,
    'San Francisco': 1100,
    'Austin': 450,
    'Boston': None
}
cities = pd.Series(d)
print cities
print cities['Portland']

#You can use the index to select specific items from the Series
print cities[['Chicago', 'Portland', 'San Francisco']]

# you can use boolean indexing for selection
print cities[ cities < 1000 ]

print cities < 1000

print cities['Chicago']

# changing based on the index
cities['Chicago'] = 200

# You can check if an element is in a Series by using 'in' operator
if  'Seattle' in cities:
    print 'Seattle is in there'
else:
    print 'Seattle in NOT there'

# Mathematical operations can be done using scalars and functions
# divide city values by 3
ncities = cities / 3

print ncities

print np.square(cities)



