# Ask user for a number
# Ask user for a second number
# Ask user for an operation: +, -, *, /
# Calculate result
# Output result
print("Welcome to calculator!")

print("What is the first number?")
num1 = int(input())

print("What is the second number?")
num2 = int(input())

print("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
op = input()

if op == '1':
    output = num1 + num2
elif op == '2':
    output = num1 - num2
elif op == '3':
    output = num1 * num2
elif op == '4':
    output = num1 / num2

print(f"The result is {output}")
