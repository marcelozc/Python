MENU = {
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

resources = {
    "water": 300, #300
    "milk": 200, #200
    "coffee": 100, #100
    "profit": 0
}


# TODO 1- reportar como está o nível dos recursos
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']:.2f}")


# TODO 2- verificar se os recursos são suficientes para o pedido
def check_resources(order):
    for key in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][key] > resources[key]:
            return (key)
    return True


# TODO 3- verificar se o pagamento é suficiente
def payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


# TODO 4- fazer o café
def making_coffee(order):
    for key in MENU[order]["ingredients"]:
        resources[key] -= MENU[order]["ingredients"][key]
    print(f"Here is your {order}. Enjoy!")


# TODO x- coffee machine
def coffee_machine():
    end = False
    while not end:
        order = input("What's your request? (espresso/latte/cappuccino): ").lower()

        if order == "report":
            report()

        elif order == "off":
            end = True

        elif order in ("espresso", "latte", "cappuccino"):
            check = check_resources(order)
            if check in ("water", "milk", "coffee"):
                print(f"Sorry there is not enough {check}")
            elif check:
                total_payment = payment()

                change = (total_payment - MENU[order]["cost"])
                if change == 0:
                    print("You don't have change to receive.")
                    resources["profit"] += MENU[order]["cost"]
                    making_coffee(order)

                elif change > 0:
                    print(f"Here is ${change:.2f} for the change.")
                    resources["profit"] += MENU[order]["cost"]
                    making_coffee(order)

                else:
                    print("That's not enough money! Try again.")

        else:
            print("Wrong command. Please try again.\n")


coffee_machine()