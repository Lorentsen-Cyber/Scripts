import time, sys

indent = 0
indentincreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        #time.sleep(0.1)

        if indentincreasing:
            indent = indent + 1
            if indent == 20:
                indentincreasing = False

        else:
            indent = indent - 1

            if indent == 0:
                indentincreasing = True

except KeyboardInterrupt:
    sys.exit()


