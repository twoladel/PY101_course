import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

def declare_winner(choice, computer_choice):
    prompt(f"You chose: {user_choice}, the computer chose: {cpu_choice}.")
    if choice == computer_choice:
        prompt("It was a tie!")
    elif ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'paper' and computer_choice == 'rock') or
        (choice == 'scissors' and computer_choice == 'paper')):
        prompt(f"You win! {choice} beat {computer_choice}.")
    else:
        prompt(f"The computer wins! {computer_choice} beats {choice}.")

prompt("Welcome to Rock, Paper, Scissors!\n")

while True:
    prompt(f"Please choose one: {', '.join(VALID_CHOICES)}")
    user_choice = input()

    while user_choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        user_choice = input()

    cpu_choice = random.choice(VALID_CHOICES)

    declare_winner(user_choice, cpu_choice)

    while True:
        prompt("Would you like to play again? Enter (y/n)")
        answer = input()
        if answer.casefold() not in ['y', 'yes', 'n', 'no']:
            prompt("Invalid response. Please enter y or n.")
        else:
            break

    if answer.casefold() in ['n', 'no']:
        break