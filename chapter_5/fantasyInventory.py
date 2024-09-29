import pprint


inventory = {'rope': 4, 'torch': 8, 'gold': 32000}
dragonLoot = ['bronze coin', 'dagger' , 'gold']


def printInventory(inventory):
    totalItems = 0
    #pprint.pprint(inventory)
    print(" Inventory:  /n")
    for item,quantity in inventory.items():
        str_quantity = str(quantity)
        print(str_quantity + ' : ' + item)
        totalItems = totalItems + quantity

    print('Total number of items: ' + str(totalItems))
printInventory(inventory)


def addingToInventory(inventory, loot):
    for piece in loot:
        if(piece not in inventory):
            inventory[piece] = 1
        else:
            inventory[piece] = inventory[piece] + 1


addingToInventory(inventory,dragonLoot)
printInventory(inventory)
   