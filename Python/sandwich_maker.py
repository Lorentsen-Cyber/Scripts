import pyinputplus as pyip

#Declaring the different choices in predefined list, 
# for ease of editing

Breads = ['wheat', 'white bread', 'sourdough']
Proteins = ['chicken', 'turkey', 'ham', 'tofu']
Cheese = ['cheddar', 'swiss', 'mozzarella']
Toppings= ['mayo', 'mustard', 'lettuce', 'tomato']

Order = []
Choice = {} 
Cost = []
counter = 0

while True:
    counter += 1
    #Prompt the "customer" for the type of bread they wish for
    bread_selection = pyip.inputMenu(Breads, lettered=True, prompt='\nWhat kinda bread do you want?\n')
    
    Choice.update({'Bread': bread_selection})
    
    #Prompt the "customer" for the type of protein they wish for
    protein_selection = pyip.inputMenu(Proteins, lettered=True, prompt=f'\nGreat choice, What kinda protein do u want on your {bread_selection} ?\n')
    
    Choice.update({'Protein': protein_selection})


    #Check wether they want cheese or not if they want cheese, present them the selection
    Yes_To_cheese = pyip.inputYesNo('\nAwesome, u want cheese with that? : yes/no\n')

    if Yes_To_cheese == 'yes':
        choose_a_cheese = pyip.inputMenu(Cheese, lettered=True, prompt='\nNice, which one?\n')
        Choice.update({'Cheeses': choose_a_cheese})

    toppings_or_no_toppings = pyip.inputYesNo('\nCool, u need some veggies or sauce on top? : yes/no\n')

    if toppings_or_no_toppings == 'yes':
        while True:
            choose_a_topping = pyip.inputMenu(Toppings, lettered=True, prompt='\nWhat u need?\n')
            Choice.update({'Toppings': choose_a_topping})
            
            continue_topping = pyip.inputYesNo('\nAnything else? : yes/no\n')
            if continue_topping == 'yes':
                continue
            else:
                break   

    multiple_sandwiches = pyip.inputYesNo('\nIs that all? : yes/no\n')

    if multiple_sandwiches == 'yes':
        break
    else:
        Order.append(Choice)
        print('All right')
        continue
print(Choice)
print(Order)
#print(counter)