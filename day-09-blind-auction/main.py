from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
dict = {}
person = True
while person:
  name = input("What is your name? ")
  bid = int(input("what is your bid? $"))
  dict[name] = bid
  nxt_person = input('Are ther any other biders? Type "yes" or "no"').lower()
  clear()
  if nxt_person == 'no':
    person = False
    max_key = max(dict,key = dict.get)
    max_value = max(dict.values())
    print(f'The winner is {max_key} with a bid of ${max_value}.')
