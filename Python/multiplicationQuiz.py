import pyinputplus as pip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for i in range(numberOfQuestions):
    # Picks 2 random integers for the question
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (i, num1, num2)

    try:
        pip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                            blockRegexes=[('.*', 'Incorrect!')],
                            timeout=8, limit=3)

    except pip.TimeoutException:
        print('Out of time! ')
    except pip.RetryLimitException:
        print('Out of tries! ')

    else:
        print('Correct! ')
        correctAnswers += 1

    time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

