birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (Leave blaank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birtday of ' + name)

    else:
        print('I do not have birtday information for ' + name)
        print('What is their birthday? ')
        bday = input()
        birthdays[name] = bday
        print('Birthday dataset updated')

