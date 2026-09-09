import resource

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
resources["Money"]= 0
is_game_over = False

def calculate_money(quarter,dime,nickle,penny):
    summation = 0
    summation = quarter * 0.25 + dime * 0.1 + nickle *0.05 + penny * 0.01
    return summation

def calculate_resources(selection, resource):
    resource["water"] -= MENU[selection]["ingredients"]["water"]
    resource["milk"] -= MENU[selection]["ingredients"]["milk"]
    resource["coffee"] -= MENU[selection]["ingredients"]["coffee"]
    resource["Money"] += MENU[selection]["cost"]

def check_resources(selection,resource):
    if resource["milk"] < MENU[selection]["ingredients"]["milk"] or resource["water"] < MENU[selection]["ingredients"]["water"] or resource["coffee"] < MENU[selection]["ingredients"]["coffee"]:
        return True
    return False

while not is_game_over:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "report":
        print(f" Water: {resources['water']}ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}gr")
        print(f" Money: ${resources['Money']}")
    else:
        is_game_over = check_resources(answer,resources)
        if is_game_over:
            print("Sorry there is not enough ingredients :( ")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            money_paid = calculate_money(quarters,dimes,nickles,pennies)
            money_required = float(MENU[answer]["cost"])
            change = money_paid - money_required
            print(f"Money paid: {money_paid}, required: {money_required}")
            print(f"Here is the change: ${change}")
            print(f"Here is your {answer}. Enjoy!")
            calculate_resources(answer,resources)
