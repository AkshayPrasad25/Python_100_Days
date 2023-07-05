from CoffeeMachineArt import logo

CentralPerk = {
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

money_made = 0
available_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > available_resources[item]:
            print(f"We're out of {item}.")
            return False
    return True


def coin_adder():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def payment_status(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money_made
        money_made += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. {money_received} refunded.")
        return False


def serve_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        available_resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name} ☕️.")


is_on = True

print(logo)

while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {available_resources['water']}ml")
        print(f"Milk: {available_resources['milk']}ml")
        print(f"Coffee: {available_resources['coffee']}g")
        print(f"Money: ${money_made}")
    else:
        drink = CentralPerk[choice]
        if resource_check(drink["ingredients"]):
            payment = coin_adder()
            if payment_status(payment, drink["cost"]):
                serve_coffee(choice, drink["ingredients"])
