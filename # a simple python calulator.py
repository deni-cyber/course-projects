# a simple python calulator
'''Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.'''

print('enter a number')
num1=eval(input())
print('enter a second number')
num2=eval(input())
print('enter a valid operation, eg +, -, /, x, etc')
operator=input()
if operator=='+':
    print(f'{num1} {operator} {num2} = {num1+num2}')
elif operator=='-':
    print(f'{num1} {operator} {num2} = {num1-num2}')
elif operator=='x':
    print(f'{num1} {operator} {num2} = {num1*num2}')
elif operator=='/':
    print(f'{num1} {operator} {num2} = {num1/num2}')
else:
    print('invalid operator')