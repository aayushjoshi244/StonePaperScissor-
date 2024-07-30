import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice, uwon, cwon):
    if user_choice == computer_choice:
        return "It's a tie!", uwon, cwon
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        uwon += 1
        return "You win!", uwon, cwon
    else:
        cwon += 1
        return "You lose!", uwon, cwon

def play_game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result, user_wins, computer_wins = determine_winner(user_choice, computer_choice, user_wins, computer_wins)
        print(result)
        print(f"So far, you have won {user_wins} games and the computer has won {computer_wins} games.")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()
