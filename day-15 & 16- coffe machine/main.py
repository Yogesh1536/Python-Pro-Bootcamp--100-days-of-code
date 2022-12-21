MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1: show of report
def report():
    if choice == 'report':
        for i in resources:
            print(i, ":", resources[i])
        print('Money : $', money)


def flavour(cust_choice):
    return MENU[cust_choice]


def check_resourece_sufficient(item):
    if resources['water'] < item["ingredients"]['water']:
        print('Not enough water')
    elif resources['milk'] < item["ingredients"]['milk']:
        print('Not enough milk')
    elif resources['coffee'] < item["ingredients"]['coffee']:
        print('Not enough coffee')
        return "not available"
    else:
        return "available"


def reduce_resource(user_selected):
    global resources
    resources["water"] -= user_selected["ingredients"]["water"]
    resources['milk'] -= user_selected["ingredients"]['milk']
    resources['coffee'] -= user_selected["ingredients"]['coffee']


def check_amount(total, item):
    if total < item["cost"]:
        print('Sorry thats not enough money. Money refunded')
        return "insufficient"
    else:
        global money
        balance = (round(total - item['cost'],2))
        credit = total - balance
        money += credit
        print(f"Here is ${balance} in change.")
        print(f"Here is your {choice} enjoy!")
        return "sufficient"

money =0
ask_again = True
while ask_again:
    choice = input("What would you like? (espresso,latte,cappuccino): ")
    if choice == 'report':
        report()
    else:
        selected = flavour(choice)
        availability = check_resourece_sufficient(selected)
        if availability == 'available':
            print("Please insert coins.")
            quarters = 0.25 * int(input("how many quarters?: "))
            dimes = 0.10 * int(input("how many dimes?: "))
            nickles = 0.05 * int(input("how many nickels?: "))
            pennies = 0.01 * int(input("how many pennies?: "))
            coined = (quarters+dimes+nickles+pennies)
            money_needed = check_amount(coined, selected)
            if money_needed == 'sufficient':
                reduce_resource(selected)

