import pyinputplus as pip

def addsUpToTen(numbers):
    numberslist = list(numbers)
    for i, digit in enumerate(numberslist):
        numberslist[i] = int(digit)
    if sum(numberslist) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)

response = pip.inputCustom(addsUpToTen)