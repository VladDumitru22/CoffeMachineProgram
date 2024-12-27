from menu import MENU, resources

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def turn_off_machine():
    return False

def report(profit):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins(quarters, dimes, nickles, pennies):
    return (quarters * QUARTERS) + (dimes * DIMES) + (nickles * NICKLES) + (pennies * PENNIES)

def check_transaction(user_paid, drink_price):
    if drink_price > user_paid:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(user_paid - drink_price, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    return True

def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


#Main Loop
working_machine = True
profit = 0

while working_machine:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        working_machine = turn_off_machine()
    elif user_input == "report":
        report(profit)
    elif user_input in MENU:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            print("Please insert coins.")
            quarters_number = int(input("How many quarters?: "))
            dimes_number = int(input("How many dimes?: "))
            nickles_number = int(input("How many nickles?: "))
            pennies_number = int(input("How many pennies?: "))
            user_paid = process_coins(quarters_number, dimes_number, nickles_number, pennies_number)
            print(user_paid)
            if check_transaction(user_paid, drink["cost"]):
                make_coffee(drink["ingredients"])
                profit += drink["cost"]
                print(f"Here is your {user_input}, Enjoy!")
    else:
        print("Invalid option. Please choose a valid drink.")