num1 = int(input('Enter number'))
num2 = int(input('Enter number'))
operator = input('Enter any operator(+,-,/,*)')
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return 'division by zero error'
        return a / b
    else:
        return 'Operator not recognized'


print(calculate(num1,num2, operator))