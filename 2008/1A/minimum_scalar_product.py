#!/usr/bin/python

"""
https://code.google.com/codejam/contest/32016/dashboard#s=p0
"""

import sys

lines = sys.stdin.readlines()

def min_scalar_product(string1, string2):
    new_list = []
    list1 = []
    list2 = []
    for i in string1.split():
        list1.append(int(i))
    for j in string2.split():
        list2.append(int(j))
    list1.sort()
    list2.sort()
    list2.reverse()
    for k in range(len(list1)): 
        new_item = list1[k]*list2[k]
        new_list.append(new_item)
    print "new_list = ", new_list
    print sum(new_list)
    return sum(new_list)

f = open("minimal_scalar_product_solutions.txt", "w")

for i in range(1, len(lines)):
    # Select lines in pairs from the input file format
    if 3*i <= len(lines):
        content = "Case #%d: " % (i) + str(min_scalar_product(lines[3*i - 1],lines[3*i])) + "\n"
        f.write(content)

f.close()
