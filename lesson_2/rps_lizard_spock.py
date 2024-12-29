import random

VALID_CHOICES = {'r': 'rock', 'p': 'paper', 'sc': 'scissors',
                 'l': 'lizard', 'sp': 'spock'}
CPU_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['scissors', 'rock']
}
VICTORS_VERB = {
    ('rock', 'scissors'): 'crushes',
    ('rock', 'lizard'): 'crushes',
    ('paper', 'rock'): 'covers',
    ('paper', 'spock'): 'disproves',
    ('scissors', 'paper'): 'cuts',
    ('scissors', 'lizard'): 'decapitates',
    ('lizard', 'paper'): 'eats',
    ('lizard', 'spock'): 'poisons',
    ('spock', 'rock'): 'vaporizes',
    ('spock', 'scissors'): 'smashes'
}

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

def player_wins(choice, computer_choice):
    return computer_choice in WINNING_COMBOS[choice]


def declare_winner(choice, computer_choice):
    prompt(f"You chose: {choice}, the computer chose: {computer_choice}.")
    print()

    if choice == computer_choice:
        declare, victor = ("It was a tie!"), 'tie'
    elif player_wins(choice, computer_choice):
        declare, victor = (
            (f"You win! {choice} {VICTORS_VERB[(choice, computer_choice)]} "
             f"{computer_choice}."), 'user')
    else:
        declare, victor = (
            (f"The CPU wins! {computer_choice} "
             f"{VICTORS_VERB[(computer_choice, choice)]} {choice}."), 'cpu')

    return (declare, victor)

def play_again():

    prompt("Would you like to play again? Enter (y/n)")
    answer = input()

    while answer.casefold() not in ['y', 'yes', 'n', 'no']:
        prompt("Invalid response. Please enter y or n.")
        answer = input()
    if answer.casefold() in ['n', 'no']:
        return False

    return True

def run_game():
    prompt("Welcome to Rock, Paper, Scissors, Lizard, Spock!\n")

    response = True
    while response:
        user_wins = 0
        cpu_wins = 0
        while user_wins < 3 and cpu_wins < 3:
            choice_key = get_user_choice()

            user_choice = VALID_CHOICES.get(choice_key)

            cpu_choice = random.choice(CPU_CHOICES)

            declaration, winner = declare_winner(user_choice, cpu_choice)
            prompt(declaration)

            if winner == 'cpu':
                cpu_wins += 1
            elif winner == 'user':
                user_wins += 1

            print(f"Score==> You: {user_wins} // CPU: {cpu_wins}")
            print()

        if user_wins == 3:
            prompt("You are the Grand Winner!")
        else:
            prompt("You lost. The computer is the Grand Winner!")

        response = play_again()

run_game()