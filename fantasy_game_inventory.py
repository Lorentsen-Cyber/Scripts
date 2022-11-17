from re import I

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,
'arrow': 12}

def display_inventory():
    inventory_count = 0
    print('Inventory: ')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        inventory_count += v
    print('Total numbers of items', str(inventory_count))

def addToInventory(loot):
    count = 0
    for i in loot:
        inventory.setdefault(i, '1')
    
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        count += int(v)
    print('Total numbers of items', str(count))

addToInventory(loot)
