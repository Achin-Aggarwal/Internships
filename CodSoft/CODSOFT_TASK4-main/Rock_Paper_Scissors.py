import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0
    tie_count = 0
    history = []
    
    rounds = int(input("Enter the number of rounds you want to play: "))
    
    for _ in range(rounds):
        print("\n--- Rock-Paper-Scissors Game ---")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        else:
            tie_count += 1
        
        history.append((user_choice, computer_choice, result))
        
        print(f"\nScore: You {user_score} - {computer_score} Computer")
        print(f"Ties: {tie_count}")
    
    print("\nGame Over!")
    print(f"Final Score: You {user_score} - {computer_score} Computer")
    print(f"Total Ties: {tie_count}")
    
    print("\nGame History:")
    for i, (user, computer, result) in enumerate(history, start=1):
        print(f"Round {i}: You chose {user}, Computer chose {computer}. Result: {result.capitalize()}")

if __name__ == "__main__":
    play_game()
