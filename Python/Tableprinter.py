tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David', 'Just Fuck My Shit Up Fam'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    longest_list = 0
    for i in tableData:
        if len(i) > longest_list:
            longest_list = len(i)
    print(longest_list)

    #cal
    colWidths = [0] * len(tableData)
    count = 0
    for i in tableData:
        for j in i:
            if len(j) >= colWidths[count]:
                colWidths[count] = len(j)
        count += 1
    count = 0
    
    #prints the output in correct order
    for j in range(0, len(tableData[0])):
        for i in range(0, len(tableData)):
            #print(tableData[i][j].rjust(colWidths[i]), end=' ')
            count += 1

printTable()