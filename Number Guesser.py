import random

number = random.randint(1,20)

for guessestaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < number:
        print('Higher')
    elif guess > number:
        print('Lower')
    else:
        break

if guess == number:
    print('Good job, u got it in ' + str(guessestaken) + (' tryes !'))
else:
    print('Nope, Try again')

