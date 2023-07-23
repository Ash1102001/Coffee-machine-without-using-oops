Menu = {
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


def report (choice):
    if  choice == "espresso":
        water_remaining = int(resources["water"]) - int(Menu["espresso"]["ingredients"]["water"])
        coffee_remaining = int(resources["coffee"]) - int(Menu["espresso"]["ingredients"]["coffee"])
        choice_cost = float(Menu["espresso"]["cost"])
        
        if water_remaining > 0 and coffee_remaining > 0:
            resources["water"] = water_remaining
            resources["coffee"] = coffee_remaining
    

            amount_cal(choice_cost, choice)
            
        else:
             for key in resources:
                 if int(resources[key]) - int(Menu["espresso"]["ingredients"][key]) <= 0:
                     print(f"Sorry there is not enough {key}.")
        
    elif  choice == "latte":
        water_remaining = int(resources["water"]) - int(Menu["latte"]["ingredients"]["water"])
        milk_remaining = int(resources["milk"]) - int(Menu["latte"]["ingredients"]["milk"])
        coffee_remaining = int(resources["coffee"]) - int(Menu["latte"]["ingredients"]["coffee"])
        choice_cost = float(Menu["latte"]["cost"])
        
        if water_remaining > 0 and milk_remaining > 0 and coffee_remaining > 0:
            resources["water"] = water_remaining
            resources["milk"] = milk_remaining
            resources["coffee"] = coffee_remaining
    

            amount_cal(choice_cost, choice)
            
        else:
             for key in resources:
                 if int(resources[key]) < int(Menu["latte"]["ingredients"][key]):
                     print(f"Sorry there is not enough {key}.")
    
    elif  choice == "cappuccino":
        water_remaining = int(resources["water"]) - int(Menu["cappuccino"]["ingredients"]["water"])
        milk_remaining = int(resources["milk"]) - int(Menu["cappuccino"]["ingredients"]["milk"])
        coffee_remaining = int(resources["coffee"]) - int(Menu["cappuccino"]["ingredients"]["coffee"])
        choice_cost = float(Menu["cappuccino"]["cost"])
        
        if water_remaining > 0 and milk_remaining > 0 and coffee_remaining > 0:
            resources["water"] = water_remaining
            resources["milk"] = milk_remaining
            resources["coffee"] = coffee_remaining
    

            amount_cal(choice_cost, choice)
            
        else:
             for key in resources:
                 if int(resources[key]) - int(Menu["cappuccino"]["ingredients"][key]) <= 0:
                     print(f"Sorry there is not enough {key}.")
        
    

    
    elif choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Money: {Money}")
        
         
                 
def amount_cal(cost, choice):
    money_got = 0.0
    print("Please insert coins.")
    q = int(input("How many quaters?: "))
    d= int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p= int(input("How many pennies?: "))
    
    total_amount_received = (q*0.25 + d*0.10 + n*0.05 + p*0.01)
    
    if total_amount_received > cost:
       money_got = cost
       print(f"Here is ${round((total_amount_received - cost), 2)} in change")
       print(f"Here is your {choice} enjoy!")
       money_update(money_got)
       
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        
Money = 0.0
def money_update(money_got):
    global Money
    Money += money_got
    return Money
    
 

def start():
    
    var = True
    while var == True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            var = False
        else:
            report(choice)
        
     
start()
   
    
    
