import pyinputplus as pip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pip.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you. Have a nice day.')
