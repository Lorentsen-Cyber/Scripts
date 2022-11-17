import random as ran
import time

#Var init
height = 28
width = 28
value = 0
#Takes the 'height' and 'width' var and defines a 2d list populated with 0's
currentState = [[ int(value) for i in range(width)]for j in range(height)]
n_neighbours = [[ int(value) for i in range(width)]for j in range(height)]
nextState = [[ int(value) for i in range(width)]for j in range(height)]


#Initalize's starting gameboard
def board_init():
    for i in range(height):
        for j in range(width):
            if ran.randint(0,1):
                currentState[i][j] = '[#]'
            else:
                currentState[i][j] = '[ ]'

def board_output():
    for i in range(height):
        print()
        for j in range(width):
            print(currentState[i][j], end='')

    print('\n\n\n\n')


    
def get_neighbours():
    for i in range(height):
        #print('1.')
        for j in range(width):
            #print('2.')
            if j != 0 and i != 0 and j != width-1 and i != height-1:
                #print('3.')
                #Get neighbours for middle fields
                if currentState[i-1][j-1] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i-1][j] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i-1][j+1] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i][j-1] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i][j+1] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i+1][j-1] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i+1][j] == '[#]':
                    n_neighbours[i][j] += 1 
                if currentState[i+1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
            #Finding the corners
            #Get neighbours for Top Left corner
            elif j == 0 and i == 0:
                if currentState[i][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j] == '[#]':
                    n_neighbours[i][j] += 1
            #Get neighbours for Top Right corner
            elif j == width-1 and i == 0:
                if currentState[i][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j] == '[#]':
                    n_neighbours[i][j] += 1
            #Get neighbours for Bottom Left corner
            elif j == 0 and i == height-1:
                if currentState[i-1][j] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i][j+1] == '[#]':
                    n_neighbours[i][j] += 1
            #Get neighbours for Bottom Right corner
            elif j == width-1 and i == height-1:
                if currentState[i-1][j] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i][j-1] == '[#]':
                    n_neighbours[i][j] += 1
            #finding the 4 sides of thr board
            #Get neighbours top side
            elif i == 0:
                if currentState[i][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i][j+1] == '[#]':
                    n_neighbours[i][j] += 1
            #Get neighbours bottom side
            elif i == height-1:
                if currentState[i][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i][j+1] == '[#]':
                    n_neighbours[i][j] += 1
            #Get neighbours left side
            elif j == 0:
                if currentState[i-1][j] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j+1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j] == '[#]':
                    n_neighbours[i][j] += 1
            #Get neighbours right side
            else:
                if currentState[i-1][j] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i-1][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j-1] == '[#]':
                    n_neighbours[i][j] += 1
                if currentState[i+1][j] == '[#]':
                    n_neighbours[i][j] += 1


def cal_next_state():
    for i in range(height):
        for j in range(width):
            if currentState[i][j] == '[#]' and n_neighbours[i][j] < 2:
                nextState[i][j] = '[ ]'
            elif currentState[i][j] == '[#]' and (n_neighbours[i][j] == 2 or n_neighbours[i][j] == 3):
                nextState[i][j] = '[#]'
            elif currentState[i][j] == '[#]' and n_neighbours[i][j] > 3:
                nextState[i][j] = '[ ]'
            elif currentState[i][j] == '[ ]' and (n_neighbours[i][j] == 3):
                nextState[i][j] = '[#]'
            else:
                nextState[i][j] = '[ ]'
    
    for i in range(height):
        for j in range(width):
            currentState[i][j] = nextState[i][j]
            n_neighbours[i][j] = 0


board_init()

while True:
    board_output()
    get_neighbours()
    cal_next_state()
    time.sleep(1)