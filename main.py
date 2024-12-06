Menu = {
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
Resources = {"water": 300,"milk": 200, "coffee": 100}
def print_menu():
    '''Prints the menu'''
    print(f"Menu: {Menu} ")

def choice(choice):
    '''Returns the choice of the user'''
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice

def turn_off(choice):
    '''Turns off the coffe machine'''
    if choice == "off":
        return False
    else:
        return True

def print_report(money):
    '''Prints report of all coffe machine resources'''
    print(f"Water: {Resources['water']}ml")
    print(f"Milk: {Resources['milk']}ml")
    print(f"Coffee: {Resources['coffee']}g")
    print(f"Money: ${money:.2f}")

def check_resources(drink):
    '''Returns True when order can be made, False if ingredients are insufficient.'''
    if drink in Menu:
        for ingredient in Menu[drink]["ingredients"]:
            if Resources[ingredient] < Menu[drink]["ingredients"][ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True
    else:
        print("Sorry, that item is not available.")
        return False

def process_coins():
    '''Calculates and returns the total coins inserted'''
    total = (
        int(input("How many quarters?: ")) * 0.25 +
        int(input("How many dimes?: ")) * 0.10 +
        int(input("How many nickles?: ")) * 0.05 +
        int(input("How many pennies?: ")) * 0.01
    )
    return total

def check_transaction(money, drink):
    '''Check if the payment is sufficient and returns the spare money or refund it'''
    if money >= Menu[drink]["cost"]:
        change = round(money - Menu[drink]["cost"], 2)
        print(f"Here is ${change} in change.")
    else:
        needed_money = round(Menu[drink]["cost"] - money, 2)
        print(f"Sorry that's not enough money. You need ${needed_money} more. Money refunded.")
        return False
    return change

def make_coffee(drink):
    '''If the resources are sufficient and the payment is sufficient, it makes the selected coffee'''
    for ingredient in Menu[drink]["ingredients"]:
        Resources[ingredient] -= Menu[drink]["ingredients"][ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!")

def coffee_machine():
    '''Main function of the machine'''
    money = 0
    machine_on = True
    while machine_on:
        user_choice = choice('')
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            print_report(money)
        else:
            if check_resources(user_choice):
                money = process_coins()
                if money >= 0:
                    if check_transaction(money, user_choice):
                        make_coffee(user_choice)

coffee_machine()




