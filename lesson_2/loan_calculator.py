import json

with open('loan_calc_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def messages(key):
    return MESSAGES[key]

def remove_commas(user_input):
    # Allow commas for loan total but remove them
    split_input = user_input.split(',')
    user_input = ''.join(split_input)
    return user_input

def invalid_number(user_input):
    try:
        num = float(user_input)
        if num < 0:
            raise ValueError(f"Please enter a positive number: {user_input}")
    except ValueError:
        return True
    return False

def calculate_loan_payment(loan_amount, loan_length, interest_rate):
    # Coerce to floats before calculations
    loan_amount = float(loan_amount)
    loan_length = float(loan_length)
    interest_rate = float(interest_rate)

    duration_in_months = loan_length * 12
    monthly_interest = (interest_rate / 100) / 12

    if monthly_interest == 0.0:
        monthly_payment = loan_amount / duration_in_months
        prompt(messages('no_interest').format(monthly_payment=monthly_payment))
    else:
        monthly_payment = loan_amount * (monthly_interest /
                        (1 - (1 + monthly_interest) ** (-duration_in_months)))

        prompt(messages('monthly_payment').format
               (monthly_payment=monthly_payment))

def another_calculation():

    prompt(messages('continue'))
    answer = input()
    if answer.lower()[0] == 'y':
        return True
    return False

print(messages('welcome'))

while True:
    prompt(messages('loan_total'))
    loan_total = input()
    remove_commas(loan_total)

    while invalid_number(loan_total):
        prompt(messages('invalid_loan'))
        loan_total = input()
        remove_commas(loan_total)

    prompt(messages('duration'))
    duration = input()

    while invalid_number(duration):
        prompt(messages('invalid_duration'))
        duration = input()

    prompt(messages('apr'))
    apr = input()

    while invalid_number(apr):
        prompt(messages('invalid_apr'))
        apr = input()

    calculate_loan_payment(loan_total, duration, apr)

    if not another_calculation():
        break