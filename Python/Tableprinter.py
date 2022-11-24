tableData = [['apples', 'oranges', 'cherries', 'banana', 'again'],
             ['Alice', 'Bob', 'Carol', 'David','Just Fuck My Shit Up Fam', 'twice'],
             ['dogs', 'cats', 'moose', 'goose', 'thrice']]
def printTable():
    longest_list = 0
    for e in tableData:
        if len(e) > longest_list:
            longest_list = len(e)
    
    #print(longest_list)

    #cal
    colWidths = [0] * len(tableData)
    count = 0
    for m in tableData:
        for n in m:
            if len(n) >= colWidths[count]:
                colWidths[count] = len(n)
        count += 1
    count = 0
        
    for i in tableData:
        extension = '#' * colWidths[count]
        for j in range((longest_list - len(i))):
            i.append(extension)
        count += 1
        
    #print(extension)
    #prints the output in correct order
    for j in range(0, longest_list):
        for i in range(0, len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]), end=' ')
        print('')

printTable()