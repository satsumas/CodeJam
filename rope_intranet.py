#!/usr/bin/python

"""
2010 Rount 1C
https://code.google.com/codejam/contest/619102/dashboard#s=p0
"""
import sys

lines = sys.stdin.readlines()

stripped_lines = []
for line in lines:
    line = line.strip('\n')
    stripped_lines.append(line)



"""
line 1: number of cases, T
line 2: number of wires in first case, N_1
lines (3, 3 + N_1): space separated pairs Ai, Bi
line N_1+1: number of wires in second case, N_2
lines (N_1 + 1, N_1 + 1 + N_2): space separated pairs Ai, Bi

"""
list_of_dicts = []

i = 1
while True:
    n = int(stripped_lines[i])
    dict = {}
    for j in range(i+1, i+n +1):
        dict[int(stripped_lines[j].split()[0])] = int(stripped_lines[j].split()[1])
    list_of_dicts.append(dict)
    if i + n + 1 < len(stripped_lines):
        i = i + 1 + n
    else:
        break

def number_intersections(my_dict):
    counter = 0
    for key in my_dict:
        for other_key in [x for x in my_dict if x != key]:
            if other_key < key:
                if my_dict[other_key] > my_dict[key]:
                    counter += 1
                else:
                    pass
            elif other_key > key:
                if my_dict[other_key] < my_dict[key]:
                    counter += 1
                else:
                    pass
    return counter
"""
for case in list_of_dicts:
    print number_intersections(case)
"""
f = open("rope_intranet_solutions.txt", "w")

for i in range(len(list_of_dicts)):
    content = "Case #%d: " % (i + 1) + str(number_intersections(list_of_dicts[i])/2) + "\n"
    f.write(content)

f.close()
