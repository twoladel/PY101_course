import random

VALID_CHOICES = {'r': 'rock', 'p': 'paper', 'sc': 'scissors', 
                 'l': 'lizard', 'sp': 'spock'}
CPU_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f"==> {message}")

def get_user_choice():
    prompt("Please choose one: ")
    for key, value in VALID_CHOICES.items():
        print(f"Enter: {key} for {value}")
    key = input()

    while key not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        key = input()

    return key

def declare_winner(choice, computer_choice):
    prompt(f"You chose: {user_choice}, the computer chose: {cpu_choice}.")

    if choice == computer_choice:
        return (("It was a tie!"), 'tie')
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
        return ((f"You win! {choice} beat {computer_choice}."), 'user')
    else:
        return ((f"The CPU wins! {computer_choice} beats {choice}."), 'cpu')

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
    user_wins = 0
    cpu_wins = 0
    while user_wins < 3 and cpu_wins < 3:
        choice_key = get_user_choice()

        user_choice = VALID_CHOICES.get(choice_key)

        cpu_choice = random.choice(CPU_CHOICES)

        message, winner = declare_winner(user_choice, cpu_choice)
        prompt(message)
        
        if winner == 'cpu':
            cpu_wins += 1
        elif winner == 'user':
            user_wins += 1
    
    if user_wins == 3:
        prompt("You are the Grand Winner!")
    else:
        prompt("You lost. The computer is the Grand Winner!")

    response = play_again()