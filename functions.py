# functions usually have () after them
# has a docstring (optional) that describes what it does
# Why functions? Helps to do task multiple times and allows us to change any part of it

# example of function call:
print(type(42))
a = type(42)
print(type(a))

message = "map"
new_message=""
for letter in message:
    if letter == ' ':
        new_message += ' '
    elif letter == '.':
        new_message += '.'
    else:
        new_message += chr(ord(letter)+2)
print(new_message)

def print_twice(name):
    print('first time')
    print(name)
    print('the second time')
    print(name)

# name = input('Please enter your name')
# print_twice(name)

def my_abs(number):
    if number < 0:
        print(-number)
    else:
        print(number)
my_abs(-2)

def give_a_break():
    return 'break'

print(give_a_break())

import math

def quadratic(a,b,c):
    dis = (b**2)-(4*a*c)
    if dis < 0:
        print('There is no real solution')
    else:
        dis = math.sqrt(dis)
        one, two = (-b + dis)/(2*a),(-b - dis)/(2*a)
        print('the answer is {},{}'.format(one,two))
        return one, two

quadratic(1,4,1)
