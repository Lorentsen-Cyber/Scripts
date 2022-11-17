
def comma(list):
    newlist = []
    for i in list:
        newlist.append(i + ',')
    newlist[-1] = list[-1]
    newlist[-1] = str('and ') + newlist[-1]

    for i in newlist:
        print(i ,end=" ")
    
        

comma(['apples', 'bananas', 'tofu', 'cats', 'dogs'])