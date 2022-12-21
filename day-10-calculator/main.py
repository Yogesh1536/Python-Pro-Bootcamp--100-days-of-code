
from art import logo
from replit import clear
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operation_dict = {"+": add,"-":sub,"*":multiply,"/":divide}

def calculator():
  print(logo)
  num1 = float(input("Enter the first number\n"))
  for keys in operation_dict:
    print(keys)
  another = True
  while another:
    operator = input('select an operator: ')
    num2 = float(input("Enter the next number\n"))
    function = operation_dict[operator]
    answer = function(num1,num2)
    print(f'{num1}{operator}{num2} = {answer}')
    if input("Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == 'y':
      num1 = answer
  
    else:
      another = False
      clear()
      calculator()

calculator()
