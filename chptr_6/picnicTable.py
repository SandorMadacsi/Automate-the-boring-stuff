def printPicnic(picnicItems, lWidth, rWidth):
    print('PICNIC ITEMS'.center(lWidth + rWidth, '-'))
    for k, v in picnicItems.items():
        print(k.ljust(lWidth,",") + str(v).just(rWidth))

items = {'apple': 10, 'chocolate:': 8, 'meat': 22}

printPicnic(items, 20, 5)