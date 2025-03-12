# Simple Calculator Program

# user input
num1 = float(input("10 "))  
num2 = float(input("5")) 
operation = input("Enter an operation (+, -, *, /): ") 

# Perform the calculation based on user choice
if operation == '+': 
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':  
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':  
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':  #
    if num2 != 0:  
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

