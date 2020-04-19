## With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.

## If no arguments are provided, the function should return a random integer between 0 and 100.
## If only a max number is provided, the function should return a random integer between 0 and the max number.
## If only a min number is provided, the function should return a random integer between the min number and 100
## If both a min and max number are provided, the function should return a random integer between those 2 values.
## Here are a couple of important notes about using random.random() and rounding. (Create this function without using random.randInt() -- we are trying to build that method ourselves for this assignment!)

## random.random() returns a random floating number between 0.000 and 1.000
## random.random() * 50 returns a random floating number between 0.000 and 50.000
## random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
## round(num) returns the rounded integer value of num

import random
def randInt(min=0, max=100 ):
    return round(random.random() * (max - min) + min)

print(randInt(min = 10))
 