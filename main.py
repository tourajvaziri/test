# midterm review:
# python types (str - int - float - bool) type checking  3 is not '3' type conversion
# variable assignments
# branching  - condiational if elif else
# comparisions (int, sttring, float (abs(difference)< 0.0001, bool)
# sring operations (length index (zero based)  last index -1 ) slicing s[start:end]  'in' operation  split
# input from user
# iteration - for loop (range) range(5,40,10) and range(40, 5, -10) - while loop (break)
# Functions - build in functions - (maxm, abs) - define function - formal parameters - actual paramaetrsrss or arguments - returning functions ( None) - default paramater values
# scoping (Local and Global variables)
# Specifications
# Palindromes (how to write a fucntio)
# Modules (import)
# Files (open) 'w' 'r') close() \n new line
# collections (Tuple (), Set {}, List [], Dictionary {}) differneces   go voer the elements
# collections functions - lsit append remove vs pop
# Dictionary: add change , get value for a key, del d[k]
# Tesing - test cases - unit testing
# debugging (print stemente debug point)

s = 'myString'
i = 3
f = 4
b = True

ss = s + 'newstring'
sLength = len(s)
print(sLength)

for x in s:
    print(x)

string = 'myvalue1,myvalue2'
print(string.split(','))

float1 = 2 / 3
float2 = 2 / 3
print(2 / 3)
if (float1 == float2):
    print('equal')

if (abs(float1 - float2) < 0.0001):
    print('equal')

print(string[2:8])

for x in range(10):
    print(x)

x = 0
while (x < 10):
    print(x)
    x = x + 1


def function1(score):
  score = score + 1
  print('score is', score)

score = 100
function1(score)
print(score)

import myFunctions
from myFunctions import myCoolFunction

print(myCoolFunction())

file = open('fruits', 'r')

for line in file:
    print(line.strip())

file2 = open('fruits2', 'w')

file2.write('apple2')
file2.close()

list = [1, 2, 3, 4]
list.append(5)
list.pop(-1)

set = set()
if 'apple' in set:
    print(True)

tuple = (1, 2, 3)
tuple[1]

dictionary1 = dict()
dictionary1.update({'apple': 1})

if 'apple' in dictionary1:
    dictionary1['apple'] = dictionary1['apple'] + 1
