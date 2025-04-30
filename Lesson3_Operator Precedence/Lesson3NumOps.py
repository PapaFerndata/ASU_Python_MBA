# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:35:09 2025

@author: ferna
"""

print("power operator:   **")

print("2**4+ ", 2**4)

print("-3**2 = ", -3**2)

print("3**-2 = ", 3**-2) 

print()

print("Unary and bitwise operators:     -       ~     ")

print("-2=",-2)

print('~2=',~2, 'bitwise inversion')

print()

print("Shifting operators:    >>    <<")

print('100>>3=',100>>3)

print('     same as:  100  // (2**3)=',100//(2**3))

print('100<3=', 100<3)

print('vs')

print('100<<3=',100<<3)

print()

print('Bianary bitwise operators:      |         &       ^  ')

print('3|0=',3|0)

print('3^3=', 3^3)

print('3&0=', 3&0)

print()

print('Comparisons     >     >=     <      <=     ==    in  not in')

print('5>2?', 5>2)

print('5==3?', 5==3)

print('5<=4?', 5<=4)

print('2 in (1, 2, 3)?', 2 in (1,2,3))

print('5 not in (1,2,3)?',5 not in (1,2,3))

print()

print('Boolean operations: AND OR NOT')

print('5 > 2 AND 5 == 2?', (5 > 2) and (5 == 2))

print('5>2 or 5==2?', (5>2) or (5==2))

print('5 NOT ==2?', not (5==2))

print()

a = 0

b = 1

print(a,b)

a , b = 0, 1
print ( "You can do multiple assignment: " , a, b)

a , b = b, a+b
print ("RBS Expressions are evaluated before any of the assign ents take place.\
The RHIS expr essions ar e evaluated from left to r ight : " , a, b)

print ()

import math

var1 = 2
var2 = 3

#round(x):round to the nearest integer 
print(round (var1/var2)) 

# fLoor(x): the Largest integer Less than or equaL to x
print(math.floor(var1/var2))

# ceiL(x): the smaLLest integer greater than or equaL to x
print(math. ceil(var1/var2))

# potv (x., y): x raised to the potver y
print ( pow(var1, var2))

# fabs (x): absoLute value of x
print(abs (var1 - var2))

# sqrt ( x) : square root of x
print(math.sqrt(var1))

print()

print ('#test')

var1 =5
var2 =2
var3 =6

var4 =math.sqrt(pow(var1,var2))

var5 =pow(var1-var2, var3)

print(var4, var5)

print()
