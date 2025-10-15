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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

index_sigh = {
    "0":"water",
    "1":"milk" ,
    "2":"coffee"
}

def cal_quarter(num_of_quarter):
    """ calculate quarter takes number of quarter"""
    return 0.01 * int(num_of_quarter)


def cal_dimes(num_of_dimes):
    """ calculate dimes takes number of  dimes"""
    return 0.05 * num_of_dimes


def cal_nickel(num_of_nickel):
    """ calculate nickel  and return total $ from nickel"""
    return 0.10 * num_of_nickel


def cal_pennies(num_of_pennies):
    """Calculate the total amount from pennies that it's takes"""

    return 0.25 * num_of_pennies


def hot_bavrage(menu_list):
    """Print the list of the manu """
    for names in menu_list:
        print(names)


def report_list(report_call):
    """takes the latest data of resources and print the names and left over in ml """
    for lists in report_call:
        print(f"{lists} : {report_call[lists]}")


def calculate_transaction(quarter, dimes, nickel, pennies):
    """Calculate the coins that the user input and return the total amount """
    total_user_coin = cal_quarter(quarter) +  cal_dimes(dimes) + cal_nickel(nickel) + cal_pennies(pennies)
    return total_user_coin

def compare_price(selected_drink, user_amount):
    """Takes user coins and compare with the price of selected drink and return True or False. """
    if MENU[selected_drink]["cost"] <=user_amount:
        return True
    else:
        return False


def compare_resources(new_resources, selected_drink):
    """ Takes new Resources and selected drink name and check that all are there or not and return boolen value list"""
    check_list = []
    for i in new_resources:
        if i in MENU[selected_drink]["ingredients"]:
            if resources[i] >= MENU[selected_drink]["ingredients"][i]:
                check_list.append(True)
            else:
                check_list.append(False)
        else:
            check_list.append(True)

    return check_list


def deduct_resources(rec,drink):
    """Takes current resources and selected drink and return a temp_resources list."""
    temp_resource ={
        "water":0,
        "milk":0,
        "coffee":0
    }
    for i in rec:
        if i in MENU[drink]:
            new_item = rec[i] - MENU[drink][i]
            temp_resource[i] = new_item
        else:
            temp_resource[i] = rec[i]
    return temp_resource
esp = "espresso"
print(deduct_resources(resources,esp))

def we_donot_have(lists_of_compare,current_resources):
    """Takes list of compare and current resource and return the text message when call"""
    places = []
    place_holder = 0
    text_return = ""
    for i in lists_of_compare:
        if i == False:
            places.append(place_holder)
            place_holder += 1
        else:
            place_holder += 1
    for x in places:
        text_return += f"{index_sigh[str(x)]} = {current_resources[index_sigh[str(x)]]}, "


    return text_return


def make_coffee(lists_of_bool):
    unique = True
    for i in lists_of_bool:
        if not i:
            unique = i
    return unique


def cal_change(selected_drink,user_amount):
    """Takes chooesn drink and user coin and return the change """
    change = user_amount - MENU[selected_drink]["cost"]
    return round(change,2)
total_profit = 0
current_resources = resources
def working():
    global total_profit
    chosen_drink = ""
    global current_resources
    user_coin = 0
    get_drink = False
    while not get_drink:
        select_drink = input(f"What do you like to take today? We have espresso, latte and cappuccino : ").lower()
        if select_drink =="off":
            return print("\nThe Coffee machine is off for now.")
        elif select_drink == "espresso":
            chosen_drink = "espresso"
            get_drink = True
        elif select_drink == "latte":
            chosen_drink = "latte"
            get_drink = True
        elif select_drink == "cappuccino":
            chosen_drink = "cappuccino"
            get_drink = True
        elif select_drink == "report":
            report_list(current_resources)
            get_drink = False
        elif select_drink == "profit":
            print(f"As of this moment we have total: {total_profit} profit.")


    resources_check = compare_resources(current_resources,chosen_drink)
    making_coffee = make_coffee(resources_check)
    if making_coffee == False:
        print(f" Sorry we donot have enough {we_donot_have(resources_check,current_resources)} ")

    elif making_coffee == True:
        num_quarter = int(input("Insert coin of quarter(0.01): "))
        num_dimes = int(input("Insert  coin of  dimes(0.05): "))
        num_nickel = int(input("Insert coin of nickel(0.10): "))
        num_pennies = int(input("Insert coin of pennies(0.25): "))
        user_coin = calculate_transaction(num_quarter, num_dimes, num_nickel, num_pennies)
        transaction =  compare_price(chosen_drink,user_coin)
        if transaction == False:
            print(f"it's not enough, Here is your refund: {user_coin}")
        else:
            change = cal_change(chosen_drink,user_coin)
            total_profit += MENU[chosen_drink]["cost"]

            if change == 0:
                print(f"Here you go your {chosen_drink} ")
            else:
                print(f"Here you go your {chosen_drink} and your {change} euro change. ")


    working()
# working()
