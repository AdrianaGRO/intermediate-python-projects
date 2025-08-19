from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def main():
    while True:
        options = menu.get_items()
        user_choice = input(f"What would you like? ({options}): ").lower()
        if user_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
            print("Thank you for using the report section!")

        if user_choice in options:
            menu_item = menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(menu_item):
                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)
                  

           
main()