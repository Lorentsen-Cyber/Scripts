# Character counter
import pprint
print('Write a centence from where to count the characters')
message = input()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print(count)
#pprint.pprint(count)