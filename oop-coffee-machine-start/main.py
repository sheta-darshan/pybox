from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()

is_one = True
while is_one:  
    options = menu.get_items()
    order_input = input(f"what would you like to order {options}?\n")
    if order_input == "Off":
        is_one = False
    elif order_input == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_input)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofee_maker.make_coffee(drink)
        
