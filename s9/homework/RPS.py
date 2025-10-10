

### >>>>>>>>>>>>>> I already wrote a rock paper scissors game a while ago <<<<<<<<<<<


import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojis = {ROCK: "🪨", PAPER: '📄', SCISSORS: '✂️'}
choices = (tuple(emojis.keys()))

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scssorrs? (r,p,s): ").lower()
        if user_choice not in choices:
            print("Invalid Choice")
            continue
        else:
            return user_choice
        
    
def display_choices(user_choice, computer_choice):
        
        print(f"You chose {emojis[user_choice]}")
        print(f"computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            print("TIE")
        elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
            print("You win")
        else: 
            print("You lose sucka")


def play_game():  
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Do you want to continue, n for no:").lower()
        if should_continue == 'n':
            break


play_game()