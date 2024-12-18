def prompt(message):
    print(f'==> {message}')


def invalid_number(number):
    try:
        int(number)
    except ValueError:
        return True

    return False

prompt("Welcome to calculator!")

prompt("What is the first number?")
num1 = input()

while invalid_number(num1):
    prompt("Hmmm... that doesn't look like a valid number.")
    num1 = input()

prompt("What is the second number?")
num2 = input()

while invalid_number(num2):
    prompt("Hmmm... that doesn't look like a valid number.")
    num2 = input()

prompt("What operation would you like to perform?\n"
      "1) Add 2) Subtract 3) Multiply 4) Divide")
op = input()

while op not in ['1', '2', '3', '4']:
    prompt("You must choose 1, 2, 3, or 4")
    op = input()

# convert str to int
num1 = int(num1)
num2 = int(num2)

match op:
    case '1':
        output = num1 + num2
    case '2':
        output = num1 - num2
    case '3':
        output = num1 * num2
    case '4':
        output = num1 / num2

prompt(f"The result is {output}")
