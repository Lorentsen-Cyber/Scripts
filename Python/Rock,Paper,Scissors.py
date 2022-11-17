#Rock,Paper,Scissors

import random,sys


# Scores
wins = 0
losses = 0
ties = 0

# Main game loop
while True:
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    # Player input loop
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playermove = input()
        #quitting the program
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or 'p' or 's' :
            break


    #Display player pick
    if playermove == 'r':
        print('ROCK vs...')
    elif playermove == 'p':
        print('PAPER vs...')
    elif playermove == 's':
        print('SCISSOR vs...')


    #Display computer pick
    RandomNumber = random.randint(1, 3)
    if RandomNumber == 1:
        computermove = 'r'
        print('ROCK')
    if RandomNumber == 2:
        computermove = 'p'
        print('PAPER')
    if RandomNumber == 3:
        computermove = 's'
        print('SCISSORS')


    #Display game and update scoring
    if playermove == computermove:
        print('It is a tie')
        ties = ties + 1
    elif playermove == 'r' and computermove == 's':
        print('You win!')
        wins = wins + 1
    elif playermove == 'p' and computermove == 'r':
        print('You win!')
        wins = wins + 1
    elif playermove == 's' and computermove == 'p':
        print('You win!')
        wins = wins + 1
    elif playermove == 'r' and computermove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playermove== 'p' and computermove == 's':
        print('You lose!')
        losses = losses + 1
    elif playermove== 's' and computermove == 'r':
        print('You lose!')
        losses = losses + 1
