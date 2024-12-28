import random

VALID_CHOICES = {'r': 'rock', 'p': 'paper', 'sc': 'scissors', 
                 'l': 'lizard', 'sp': 'spock'}
CPU_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f"==> {message}")

def declare_winner(choice, computer_choice):
    prompt(f"You chose: {user_choice}, the computer chose: {cpu_choice}.")

    if choice == computer_choice:
        prompt("It was a tie!")
    elif ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'paper' and computer_choice == 'rock') or
        (choice == 'scissors' and computer_choice == 'paper') or
        (choice == 'rock' and computer_choice == 'lizard') or
        (choice == 'paper' and computer_choice == 'spock') or
        (choice == 'scissors' and computer_choice == 'lizard') or
        (choice == 'spock' and computer_choice == 'scissors') or
        (choice == 'spock' and computer_choice == 'rock') or
        (choice == 'lizard' and computer_choice == 'spock') or
        (choice == 'lizard' and computer_choice == 'paper')):
        prompt(f"You win! {choice} beat {computer_choice}.")
    else:
        prompt(f"The computer wins! {computer_choice} beats {choice}.")

def play_again():

    prompt("Would you like to play again? Enter (y/n)")
    answer = input()

    while answer.casefold() not in ['y', 'yes', 'n', 'no']:
        prompt("Invalid response. Please enter y or n.")
    if answer.casefold() in ['n', 'no']:
        return False

    return True

prompt("Welcome to Rock, Paper, Scissors, Lizard, Spock!\n")

response = True
while response:
    prompt(f"Please choose one: {', '.join(VALID_CHOICES)}")
    choice_key = input()

    while choice_key not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice_key = input()

    user_choice = VALID_CHOICES.get(choice_key)

    cpu_choice = random.choice(CPU_CHOICES)

    declare_winner(user_choice, cpu_choice)

    response = play_again()