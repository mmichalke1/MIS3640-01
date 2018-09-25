import time
# easy to do print(1+2+3) but what about print(1+2+...+100)

# Exercise 1
def iteration(n):
    sum=0
    for i in range(1, n+1):
        sum += i

    return sum
def iteration_odd(n):
    sum=0
    for i in range(1, n+1,2):
        sum += i

    return sum

print(iteration(10))
print(iteration(1000))
print(iteration_odd(1000))
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

# print(factorial(10))

def countdow(n):
    while n>-1:
        print(n)
        time.sleep(1)
        n = n-1
    print('Blastoff!')

# countdow(10)

def hello(n):
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in 'hello, world':
            count += 1
        print('Iteration ' + str(iteration +1) + '; count is: ' + str(count))
        iteration += 1



# Exercise 2
# 1. count =12
# 2. count = 24
# 3. count = 36
# 4. count = 48
# 5. count = 60

# 1. count = 12
# 2. count =12
# 3. count =12
# 4. count =12
# 5. count =12

# 1. 5 times
# 2. Iteration 4
# 3. Count = 12
# 4. count = 1

# rewrite exercise 1 with while loops
def iteration_while(n):
    sum=0
    count = 0
    while count < n+1:
        sum += count
        count += 1
    return sum

def iteration_odd_while(n):
    sum = 0
    count = 0
    while count < n+1:
        if count % 2 == 0:
            sum += 0
            count += 1
        else:
            sum += count
            count += 1
    return sum

print(iteration_while(10))
print(iteration_while(1000))
print(iteration_odd_while(1000))

# Exercise 3
import math
import pandas as pd

def mysqrt(a, x):
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y


def test_sqrt():
    table = pd.DataFrame(columns=['a', 'mysqrt', 'mathsqrt', 'diff'])
    table.a = range(1, 10)
    for index, row in table.iterrows():
        table.mysqrt[index] = mysqrt(table.a[index], (table.a[index]+1))
        table.mathsqrt[index] = math.sqrt(table.a[index])
    table['diff'] = table.mysqrt - table.mathsqrt
    print(table)

test_sqrt()
