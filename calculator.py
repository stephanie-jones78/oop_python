'''
PROBLEM STATEMENT:
    Create a calculator tool using OOP in Python. 
    The calculator should be able to perform addition, subtraction, mutliplication, and division based on user inputs.
'''

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return 'Cannot divide by zero.'
        return x / y

# creating calculator object
calc = Calculator()

# getting user inputs for calculations
try:
    x = float(input('Enter first number: '))
    operation = input('Enter operator (+, -, *, /): ')
    y = float(input('Enter second number: '))

    # perform operation based on user input
    if operation == '+':
        result = calc.add(x, y)
    
    elif operation == '-':
        result = calc.subtract(x, y)

    elif operation == '*':
        result = calc.multiply(x, y)

    elif operation == '/':
        result = calc.divide(x, y)
    
    else:
        result = 'Invalid operator entered.'

    # print the result
    if result % 1 == 0:
        result = int(result)
    print(f'Result: {result}')

except ValueError:
    print('Invalid input value. Please enter valid numbers.')
except Exception as e:
    print(f'An error occurred: {e}')