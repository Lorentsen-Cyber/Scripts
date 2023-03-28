import pyinputplus as pyip
import time
#Declaring the different choices in predefined list, 
# for ease of editing

Breads = ['wheat', 'white bread', 'sourdough']
Proteins = ['chicken', 'turkey', 'ham', 'tofu']
Cheese = ['cheddar', 'swiss', 'mozzarella']
Toppings= ['mayo', 'mustard', 'lettuce', 'tomato']

Order = []
Choice = []
Cost = []
counter = 0

while True:
    counter += 1
    #Prompt the "customer" for the type of bread they wish for
    bread_selection = pyip.inputMenu(Breads, lettered=True, prompt='\nWhat kinda bread do you want?\n')
    print(Order)
    Choice.append(bread_selection)
    print(Order)    
    #Prompt the "customer" for the type of protein they wish for
    protein_selection = pyip.inputMenu(Proteins, lettered=True, prompt=f'\nGreat choice, What kinda protein do u want on your {bread_selection} ?\n')
    
    Choice.append(protein_selection)


    #Check wether they want cheese or not if they want cheese, present them the selection
    Yes_To_cheese = pyip.inputYesNo('\nAwesome, u want cheese with that? : yes/no\n')

    if Yes_To_cheese == 'yes':
        choose_a_cheese = pyip.inputMenu(Cheese, lettered=True, prompt='\nNice, which one?\n')
        Choice.append(choose_a_cheese)

    toppings_or_no_toppings = pyip.inputYesNo('\nCool, u need some veggies or sauce in that? : yes/no\n')

    if toppings_or_no_toppings == 'yes':
        while True:
            choose_a_topping = pyip.inputMenu(Toppings, lettered=True, prompt='\nWhat u need?\n')
            Choice.append(choose_a_topping)
            
            continue_topping = pyip.inputYesNo('\nAnything else? : yes/no\n')
            if continue_topping == 'yes':
                continue
            else:
                break   

    multiple_sandwiches = pyip.inputYesNo('\nAnything else? : yes/no\n')

    if multiple_sandwiches == 'yes':
        print(Order)
        Order.append(Choice)
        print(Order)
        continue
    elif multiple_sandwiches == 'no':
        print(Order)
        Order.append(Choice)
        print(Order)
        #print('All right')
        break
#Calculate cost of order


'''print(Order)
print( )
#Display order and price
for i in range(len(Order)):
    print(i, Order[i])
'''