
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}
###################################  PROJECT (COFFEE MACHINE) ######################



def report():
    print(f"""
    water: {resources['water']}ml
    milk: {resources['milk']}ml
    coffee: {resources['coffee']}ml
    money: ${resources['money']}
    """)
    machine()

def stock_check(coffee_type):

    if int(resources['water']) < int(MENU[coffee_type]['ingredients']['water']):
        print("Not enough water")
    elif int(resources['milk']) < int(MENU[coffee_type]['ingredients']['milk']):
        print("Not enough milk")
    elif int(resources['coffee']) < int(MENU[coffee_type]['ingredients']['coffee']):
        print(" Not enough coffee")

def money_calcualtor(total, coffee_type):

     change = round(total - MENU[coffee_type].get('cost'), 2)
     if total > MENU[coffee_type].get('cost'):
        print(f"Here is ${change} in change")
        print(f"Here is your fresh {coffee_type} ☕. Enjoy!")
     elif total == MENU[coffee_type].get('cost'):
        print(f"Here is your fresh {coffee_type} ☕. Enjoy!")


def stock_update( coffee_type):
    resources["water"] = resources.get("water") - MENU[coffee_type].get('ingredients')['water']
    resources["milk"] = resources.get("milk") - MENU[coffee_type].get('ingredients')['milk']
    resources["coffee"] = resources.get("coffee") - MENU[coffee_type].get('ingredients')['coffee']
    resources["money"] += MENU[coffee_type].get('cost')

def machine():
    turn_off = False
    while turn_off == False:
            ############## BEGIN with ASKING TYPE OF COFFEE OR INQUIRY ##########
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type == 'turnoff':
            turn_off = True
        elif coffee_type == 'report':
            report()
        else:
            stock_check(coffee_type)
            print("Please insert the coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if total >= MENU[coffee_type].get('cost'):
                money_calcualtor(total, coffee_type)
                stock_update(coffee_type)
            else:
                print("Sorry that's not enough money. Money refunded.")
machine()