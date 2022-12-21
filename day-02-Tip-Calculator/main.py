#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator.")
bill = input("What was the total bill : $")
tip = input("What percentge tip would you like to give? 10,12 or 15 ?")
person = input("How many person to split the bill ?")
value = (int(bill)/ int(person) * ((int(tip)/100) + 1))
new_value = '{:.2f}'.format(value)
print("Each person should pay : $", new_value)