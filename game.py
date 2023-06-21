import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    rounds = 3
    user_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        
        while True:
            user_choice = input("Your turn: ")
            if user_choice.isdigit() and int(user_choice) in range(1, 4):
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")

        user_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print("\nGame Over!")
    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    
    if user_score > computer_score:
        print("Congratulations, You won!")
    elif user_score < computer_score:
        print("Better luck next time, Computer won!")
    else:
        print("It's a tie!")

play_game()
