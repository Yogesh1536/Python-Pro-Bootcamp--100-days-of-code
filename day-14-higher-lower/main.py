from game_data import data
import random
from art import logo,vs
from replit import clear

def Compare(first,secound,answer):
  global score
  if first['follower_count'] > secound['follower_count']:
    if answer == 'A':
      score += 1 
      return True
    else:
       print(f"Sorry, that's wrong final score is {score}")
       return False
  elif secound['follower_count'] > first['follower_count']:
    if answer == 'B':
      score += 1
      first = secound
      return True
    else:
        clear()
        print(f"Sorry, that's wrong final score is {score}")
        return False
  

print(logo)
score = 0



A = random.choice(data)
print(f"Compare A: {A['name']},a {A['description']}, from {A['country']}")
print(vs)
B = random.choice(data)
print(f"Compare B: {B['name']},a {B['description']}, from {B['country']}")
ans = input("Who has more followers?, Type 'A' or 'B': ")
continue_game = Compare(A,B,ans)
print(continue_game)
while continue_game:
  clear()
  print(logo)
  print(f"You are right, Current score {score}")
  A = B
  print(f"Compare A: {A['name']},a {A['description']}, from {A['country']}")
  print(vs)
  B = random.choice(data)
  print(f"Compare B: {B['name']},a {B['description']}, from {B['country']}")
  ans = input("Who has more followers?, Type 'A' or 'B': ")
  continue_game = Compare(A,B,ans)
