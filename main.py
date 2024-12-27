from menu import MENU, resources

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def turn_off_machine():
    return False

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins(quarters, dimes, nickles, pennies):
    return (quarters * QUARTERS) + (dimes * DIMES) + (nickles * NICKLES) + (pennies * PENNIES)

def check_transaction(user_paid, drink_price, profit):
    if drink_price > user_paid:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif user_paid > drink_price:
        profit += drink_price
        change = user_paid - drink_price
        print(f"Here is ${change} in change")
        return True
    else:
        profit += drink_price
        return True



working_machine = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
profit = 0

while working_machine:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        working_machine = turn_off_machine()
    elif user_input == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            print("Please insert coins.")
            quarters_number = int(input("How many quarters?: "))
            dimes_number = int(input("How many dimes?: "))
            nickles_number = int(input("How many nickles?: "))
            pennies_number = int(input("How many pennies?: "))
            user_paid = process_coins(quarters_number, dimes_number, nickles_number, pennies_number)
            print(user_paid)
            if check_transaction(user_paid, drink["cost"], profit):
                print(f"Here is your {user_input}, Enjoy!")

