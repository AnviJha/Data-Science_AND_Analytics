import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice(user_history):
    # Simple AI: try to counter user's most frequent move
    # first move user not played priviously
    if not user_history:
        return random.choice(choices)
    # calculate the most common input user choose :set(user_history) → removes duplicates
    most_common = max(set(user_history), key=user_history.count)

    counter = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    return counter[most_common]

# read high score 
def load_high_score():
    try:
        with open("Hi_score.txt",'r') as f:
            return int(f.read())
    except:
        return 0
# save high score 
def save_high_score(score):
    with open("Hi_score.txt","w") as f:
        f.write(str(score))


def decide_winner(user, computer):
    if user == computer:
        return "draw"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    high_score = load_high_score()
    print(f"🏆 High Score: {high_score}")

    user_score = 0
    computer_score = 0
    rounds = int(input("Enter number of rounds: "))
    user_history = []

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        user = input("Enter rock, paper, or scissors: ").lower()

        # Input validation
        if user not in choices:
            print("❌ Invalid input! Try again.")
            continue   #continue skips the rest of the current iteration.and moves to the next loop iteration immediately
        
        # addign user history 
        user_history.append(user)

        computer = get_computer_choice(user_history)

        print(f"🤖 Computer chose: {computer}")

        result = decide_winner(user, computer)

        if result == "draw":
            print("⚖️ It's a draw!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")

    # Final Result
    print("\n===== FINAL RESULT =====")
    if user_score > computer_score:
        print("🏆 You won the game!")
    elif user_score < computer_score:
        print("💻 Computer won the game!")
    else:
        print("⚖️ Game is a draw!")

    
    # 🔥 Update high score
    if user_score > high_score:
        print("🔥 New High Score!")
        save_high_score(user_score)    



# starting point
# Replay system
while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break