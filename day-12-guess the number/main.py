#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
number = random.randint(1,100)
gameover = 0
find = 0
def check_guess(guess,chance):
  if chance == 1:
    print( "You've run out of gusess, You lose.")
    global gameover
    gameover += 1
  elif guess == number:
    print( "You guessed a number, You win!")
    global find
    find += 1
  elif guess > number:
    print( "Too High")
  elif guess < number:
    print( "Too less")
  
print(logo)
print('Welcome to the number guessing game')
print('Im thinking of a number between 1 to 100.')
level = input("Choose the difficulty. Type 'easy' or 'hard': ")
def game_level():
  if level == "easy":
    return ([10,9,8,7,6,5,4,3,2,1,0])
  if level == "hard":
    return ([5,4,3,2,1,0])

for position in game_level():
  print(f'you have {position} attempts remining to guess the number')
  guessed_n  = int(input("Make a Guess: "))
  check_guess(guessed_n,position)
  if find == 1:
    break
  if gameover == 1:
    break
