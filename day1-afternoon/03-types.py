#!/usr/bin/env python3

a_string = "42"

an_int = 42

a_float = 42

# Booleans
truthy = True
falsish = False

# Lists
a_list = { 1, 2, 3, 4 }
print(a_list)
a_list[3] = 4000
print(a_list)

another_list = a_list # only giving it another name, not a different list
a_list = 4000
print(a_list)
print(another_list)
# OR
another_list = list(a_list) # making a copy of the original list

a_tuple = { 1, True, "Seven" }
# lists are homogenous and tuples are inhomogenous.

# Dictionary
a_dict = { 'a': 1. "b": 5}

for value in an_int, a_float, a_string, truthy, a_list, a_tuple:
    print( value, type(value))