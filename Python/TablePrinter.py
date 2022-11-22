tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    count = 0
    for i in tableData:
        for j in i:
            if len(j) >= colWidths[count]:
                colWidths[count] = len(j)
        count += 1
    count = 0
    #print(range(tableData[0]))
    for j in range(tableData[0]):
        for i in range(tableData):
            print(tableData[j][i].rjust(colWidths[i]), end=' ')   
        print()



    #print(colWidths)

printTable()