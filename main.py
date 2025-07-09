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
}

MONEY = 0
PROFIT = 0


# TODO Print a report of all the coffee machine resources
def report():
    print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {PROFIT} ")

# TODO Create a function that checks and subtracts coffee, milk, and water levels
def check_levels(a,b,c,d):
    leftover_a = resources["water"] - MENU[d]["ingredients"][a]
    leftover_b = resources["milk"] - MENU[d]["ingredients"][b]
    leftover_c = resources["coffee"] - MENU[d]["ingredients"][c]

    if leftover_a < 0:
        print(f"Sorry, there is not enough {a}")
        return False
    if leftover_b < 0:
        print(f"Sorry, there is not enough {b}")
        return False
    if leftover_c < 0:
        print(f"Sorry, there is not enough {c}")
        return False
    else:
        resources[a] = leftover_a
        resources[b] = leftover_b
        resources[c] = leftover_c
        # print(f"{a}: {resources[a]}")
        # print(f"{b}: {resources[b]}")
        # print(f"{c}: {resources[c]}")
        return True

# TODO Ask for money

def coins():
    total = 0
    print("Please insert coins...")
    q = int(input("How many quarters?:"))
    d = int(input("How many dimes?:"))
    n = int(input("How many nickles?:"))
    p = int(input("How many pennies?:"))

    quarters = (q * .25)
    dimes = (d * .10)
    nickles = (n * .05)
    pennies = (p * .01)
    global MONEY
    MONEY += quarters
    MONEY += dimes
    MONEY += nickles
    MONEY += pennies
    # global PROFIT
    # PROFIT += quarters
    # PROFIT += dimes
    # PROFIT += nickles
    # PROFIT += pennies
    return round(MONEY, 2)


# TODO Prompt reader asking them what they would like

off = False
while off == False:

    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        off = True
    if choice == "report":
        report()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_levels("water","milk","coffee",choice) is True:
            print(f"Cost: ${round(MENU[choice]["cost"],4)}")
            difference = coins() - MENU[choice]["cost"]
            print(f"${round(difference,3)}")
            if difference >= 0:
                PROFIT += (MONEY - difference)
                print(f"Here is your {choice}. Enjoy!")
                print(f"Your change is: ${round(difference,2)}")
                MONEY = 0
                print(f"Total profit: {round(PROFIT,3)}")
                print(MONEY)
            if difference < 0:
                print("Sorry that's not enough money. Money refunded.")
                MONEY = 0
                print(f"Total profit: {PROFIT}")
                print(MONEY)





