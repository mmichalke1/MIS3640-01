import math
import pandas as pd

def mysqrt(a, x):
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y

# print(mysqrt(9,4))

def test_sqrt():
    table = pd.DataFrame(columns=['a', 'mysqrt', 'mathsqrt', 'diff'])
    table.a = range(1, 10)
    for index, row in table.iterrows():
        table.mysqrt[index] = mysqrt(table.a[index], (table.a[index]+1))
        table.mathsqrt[index] = math.sqrt(table.a[index])
    table['diff'] = table.mysqrt - table.mathsqrt
    print(table)

test_sqrt()