tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)

    for i in tableData:
        for j in i:
            count = -1
            count += 1
            if len(j) >= colWidths[count]:
                colWidths[count] = len(j)
        
    print(colWidths)

printTable()