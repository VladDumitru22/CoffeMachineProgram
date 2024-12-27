from menu import MENU, resources

def turn_off_machine():
    return False

#def check_resources(water, milk, coffee):


working_machine = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

while working_machine:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        working_machine = turn_off_machine()
    elif user_input == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    #elif user_input == "espresso":
