'''
Design a Python program called “Perfect Guess Game” in which the computer randomly selects a number within a given range, and the user has to guess
 that number.
 📌 Objective
The goal of the game is for the user to correctly guess the randomly generated number in the minimum number of attempts.
⚙️ Game Rules
The program generates a random number between a specified range (e.g., 1 to 100).
The user is prompted to enter their guess.
After each guess, the program provides feedback:
If the guess is lower than the number → display “Too low”
If the guess is higher than the number → display “Too high”
The user continues guessing until the correct number is guessed.
Once guessed correctly:
Display a congratulatory message 🎉
Show the total number of attempts taken
'''
# _________________________________________________________________________________________________________________________________________________________________________


import random

# generate a random number between 1 to 100
n=random.randint(1,100)
print("WELCOME TO PERFECT GUESS GAME ! 🎯 ")

guess=None
guesses=0
while(guess!=n):
    guess=int(input("Enter your guess please 💭 : "))
    guesses+=1
    if guess==n:
        print("hooray ! you guessed it right 🎊")
    elif(guess>n):
        print("go lower ⬇️")
    else:
        print("Go higher ⬆️")    

print(f"You guessed the number in {guesses} attempts.")

