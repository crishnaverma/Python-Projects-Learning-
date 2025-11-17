MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100}


def is_resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry we are out of stock for {item}")
            return False
    return True


def money_process():
    print("Insert the coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


machine_on = True

while machine_on:
    ask_user = input("What would you like? (espresso/latte/cappuccino) or Type 'menu' to see menu: ").lower()
    
    if ask_user == "off":
        machine_on = False
    
    elif ask_user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    
    elif ask_user in MENU:
        drink = MENU[ask_user]
        if is_resource_available(drink["ingredients"]):
            payment = money_process()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(ask_user, drink["ingredients"])
    elif ask_user == "menu":
        for drink, info in MENU.items():
             print(f"{drink.title()}: ${info['cost']}")

    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
