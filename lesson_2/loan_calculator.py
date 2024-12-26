import json

with open('loan_calc_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def messages(key):
    return MESSAGES[key]

def remove_commas(user_input):
    # Allow commas but remove them
    split_input = user_input.split(',')
    user_input = ''.join(split_input)
    return user_input

def invalid_number(user_input):
    try:
        float(user_input)
    except ValueError:
        return True
    return False

def calculate_loan_payment(loan_total, duration, apr):
    
    loan_total = float(loan_total)
    duration = float(duration)
    apr = float(apr)

    duration_in_months = duration * 12
    monthly_interest = (apr / 100) / 12

    if monthly_interest == 0.0:
        monthly_payment = loan_total / duration_in_months
        prompt(messages('no_interest').format(monthly_payment=monthly_payment))
    else:
        monthly_payment = loan_total * (monthly_interest / 
                        (1 - (1 + monthly_interest) ** (-duration_in_months)))

        monthly_payment = round(monthly_payment, 2)
        prompt(messages('monthly_payment').format(monthly_payment=monthly_payment))

print(messages('welcome'))

prompt(messages('loan_total'))
loan_total = remove_commas(input())

while invalid_number(loan_total):
    prompt(messages('invalid_loan'))
    loan_total = remove_commas(input())

prompt(messages('duration'))
duration = remove_commas(input())

while invalid_number(duration):
    prompt(messages('invalid_duration'))
    duration = remove_commas(input())

prompt(messages('apr'))
apr = remove_commas(input())

while invalid_number(apr):
    prompt(messages('invalid_apr'))
    apr = remove_commas(input())

calculate_loan_payment(loan_total, duration, apr)