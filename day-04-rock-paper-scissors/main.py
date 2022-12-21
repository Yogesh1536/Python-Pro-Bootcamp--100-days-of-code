rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
user = int(input())
if user == 0:
  print(rock)
elif user == 1:
  print(paper)
else:
  print(scissors)

print('Computrt choose:')
sys = random.randint(0,2)
if sys == 0:
  print(rock)
elif sys == 1:
  print(paper)
else:
  print(scissors)
if user == 0 and sys == 1:
  print('Computer wins the Game')
elif user == 1 and sys == 0:
  print('You wins the Game')
elif user == 0 and sys == 2:
  print('You wins the Game')
elif user == 2 and sys == 0:
  print('Computer wins the Game')
elif user == 1 and sys == 2:
  print('Computer wins the Game')
elif user == 2 and sys == 1:
  print('You wins the Game')
else:
  print('Match draw, Play again!')