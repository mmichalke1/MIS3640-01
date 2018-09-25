import webbrowser
def bmi_tester():
    w=float(input('Please enter your weight'))
    h=float(input('Please enter your height'))
    system=input('USA/Metric')
    if system == 'USA':
        bmi = float(703*(w/(h**2)))
    else:
        bmi = float(w/h)

    if bmi <= 18.5:
        print('underweight')
        webbrowser.open('https://www.mcdonalds.com/us/en-us.html')
    elif bmi >18.5 and bmi< 25:
        print('normal weight')
    elif bmi>=25 and bmi<30:
        print('Overweight')
    else:
        print('Obesity')

def compare(varA, varB):
    # varA = input('VarA equals...')
    # varB = input('VarB equals...')
    if isinstance(varA, str) or isinstance(varB, str):
        print('String is contained')
    elif varA > varB:
        print('VarA is bigger than VarB')
    elif varA == varB:
        print('VarA is equal to VarB')
    else:
        print('VarA is smalled than VarB')

a = 'hello'
b = 3
c = 5

# compare(a,b)
# compare(b,c)

# Recursion

def countdown(n):
    if n <= 0:
        print('blastoff!')
    else:
        print(n)
        countdown(n-1)

# countdown(5)

def fibonaci(n):
    if n == 1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonaci(n-2) + fibonaci(n-1)

print(fibonaci(10))
print(2)
