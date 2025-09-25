"""
Write a Program to sort the Dictionary in Ascending and Descending 
by Key and Value
"""

d = {1: 22, 3: 13, 4: 8, 2: 11, 0: 27}
print("Original dictionary:", d)

""" ----------------- By Key --------------------------------- """

# Ascending order by Key
t = sorted(d.items())
print("Ascending order by Key:", dict(t))

# Descending order by Key
t = sorted(d.items(), reverse=True)
print("Descending order by Key:", dict(t))

""" --------------------By Value------------------------------- """

import operator

# Ascending order by Value
t = sorted(d.items(), key=operator.itemgetter(1))
print("Ascending order by Value:", dict(t))

# Descending order by Value
t = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print("Descending order by Value:", dict(t))
