
# creation of list
rivers_list = ['krishna', 'godavari', 'tunga', 'cauvery', 'ganga', 'godavari']

# iterating a list
for river in rivers_list:
    print river

# accesing an element in list
print 'rivers_list[0]={} rivers_list[1]={}'.format(
    rivers_list[0], rivers_list[1]
)

# accesing an element in list from the end
print 'rivers_list[-1]={} rivers_list[-2]={}'.format(
    rivers_list[-1], rivers_list[-2]
)

# number of times an element is present
print 'tunga is found {} times '.format(rivers_list.count('tunga'))
print 'moosi is found {} times '.format(rivers_list.count('moosi'))
print 'godavari is found {} times '.format(rivers_list.count('godavari'))

# appending an element
rivers_list.append('yamuna')
print rivers_list[-1]

# extending a list with another list
some_other_rivers = ['sutlej', 'ravi', 'narmada', 'mahanadi']
rivers_list.extend(some_other_rivers)
print rivers_list

# getting the index of an element
ind = rivers_list.index('cauvery')
print 'index of cauvery is {}'.format(ind)

# inserting at a specific location
rivers_list.insert(3,'gomti')
print rivers_list

# removing an element
rivers_list.remove('ravi')
print rivers_list

# popping out the last element
last = rivers_list.pop()
print rivers_list

# reversing a list
rivers_list.reverse()
print rivers_list

# sorting a list
rivers_list.sort()
print rivers_list

# min() gets the element with minimum value
min_elem = min(rivers_list)
print min_elem

# max() gets the element with maximum value
max_elem = max(rivers_list)
print max_elem

# cmp() for comparing two lists
ret = cmp(rivers_list,some_other_rivers)
print ret

# len() to get the length of list
len_rivers = len(rivers_list)
print len_rivers

# slicing a list
from_4_till_end = rivers_list[4:]
start_to_5 = rivers_list[:5]

print from_4_till_end
print start_to_5

#range() function can create a list of numbers
num_list = range(5)
print num_list

