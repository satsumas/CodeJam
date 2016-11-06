#!/usr/bin/python

"""
Problem:
https://code.google.com/codejam/contest/90101/dashboard#s=p0
"""

"""
A pattern is L tokens
A token is a letter or a group of letters in parentheses

L D N
D = no of words known in language
N = no of testcases, following the N words
L = word length


Output: how many words in the alien language match the pattern
"""
import sys
import re # Use regex


lines = sys.stdin.readlines()

stripped_lines = []
for line in lines:
    line = line.strip('\n')
    stripped_lines.append(line)

# Define the integers used to index the input file
L = int(stripped_lines[0].split()[0])

D = int(stripped_lines[0].split()[1])

N = int(stripped_lines[0].split()[2])

# Compile a list of know words in the language
known_words = []
for i in range(1, D + 1):
    known_words.append(stripped_lines[i])


# Use regex on the lines following the fist D+1 lines, incrememnt the 
# counter when a line matches one of the known words
f = open("alien_language_solutions.txt", "w")

for i in range(D +1, D + N + 1):
    counter = 0
    regexified = stripped_lines[i].replace('(', '[').replace(')', ']')
    regexified = '^' + regexified + '$' 
    for word in known_words:
        if re.match(regexified, word) != None:
            counter += 1
    content = 'Case #%d: %d \n' % (i - D, counter)
    f.write(content)

f.close()

