import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

prompt("Welcome to Rock, Paper, Scissors!\n")

# Add looping logic so play can continue! 
prompt(f"Please choose one: {', '.join(VALID_CHOICES)}")
choice = input()

while choice not in VALID_CHOICES:
    prompt("That's not a valid choice.")
    choice = input()

computer_choice = random.choice(VALID_CHOICES)

prompt(f"You chose: {choice}, the computer chose: {computer_choice}.")
# Abstract this to a determine winner function
if choice == computer_choice:
    prompt("It was a tie!")
elif ((choice == 'rock' and computer_choice == 'scissors') or
    (choice == 'paper' and computer_choice == 'rock') or
    (choice == 'scissors' and computer_choice == 'paper')):
    prompt(f"User wins! {choice} beat {computer_choice}.")
else:
    prompt(f"The computer wins! {computer_choice} beats {choice}.")
