#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("0. Quit")

        user_input = input("Enter your choice (1-3) or 0 to quit: ")

        if user_input == "0":
            print("\nThanks for playing! Final scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

        choices = ["rock", "paper", "scissors"]
        user_choice = choices[int(user_input) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nCurrent scores - You: {user_score}  Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != 'yes':
            print("\nThanks for playing! Final scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()


# In[ ]:




