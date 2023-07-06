from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from CoffeeMachineArt import logo

cash = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

print(logo)

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to order? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        cash.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and cash.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
