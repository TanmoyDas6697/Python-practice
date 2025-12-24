print("what is your first number? ")
num1 = float(input("Enter first number: "))
print("what's your operation? (+, -, *, /) ")
operation = input("Enter operation: ")
print("what is your second number? ")
num2 = float(input("Enter second number: "))

if operation == '+':
    result = num1 + num2
    print("The result is: ", result)
elif operation == '-':
    result = num1 - num2
    print("The result is: ", result)
elif operation == '*':
    result = num1 * num2
    print("The result is: ", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result is: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")