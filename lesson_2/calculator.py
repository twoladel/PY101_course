import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number):
    try:
        int(number)
    except ValueError:
        return True

    return False

while True:

    prompt(MESSAGES['welcome'])

    prompt(MESSAGES['first_num'])
    num1 = input()

    while invalid_number(num1):
        prompt(MESSAGES['invalid_num'])
        num1 = input()

    prompt(MESSAGES['second_num'])
    num2 = input()

    while invalid_number(num2):
        prompt(MESSAGES['invalid_num'])
        num2 = input()

    prompt(MESSAGES['operation'])
    op = input()

    while op not in ['1', '2', '3', '4']:
        prompt(MESSAGES['invalid_op'])
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

    result = MESSAGES['result']
    formatted_result = result.format(output=output)

    prompt(formatted_result)

    prompt(MESSAGES['continue'])
    calc_on = input()
    if calc_on and calc_on[0].lower() != 'y':
        break
