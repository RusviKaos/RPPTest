#Other data types

# complex - complex numbers, imaginary numbers

# long - Only in Python 2 - replaced by int in Python 3

# bytes and bytearray - sequence of int(0-255), sequence of strings(chars?)

#touple (like list but can not change values)
#apparently very common
t = (3,4,1,"M")
print(t)
# t[0] = 2   'tuple' object does not support item assignment

#set and frozenset - like lists 
lst = [3,2,3,1,5,5,6,4]#Unsorted list with duplicates
set_a = set(lst)#Converted to set, sorted and without duplicates
print(set_a)