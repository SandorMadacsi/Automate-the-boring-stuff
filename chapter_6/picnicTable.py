

def printPicnic(dictItems, leftWidth, rightWidth):
    print('picnic items'.upper().center(leftWidth + rightWidth,'='))
    for k, v in dictItems.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
        

picnicItems = {'sandwiches' : 4, 'fizzy drinks' : 5, 'mixed salad': 3, 'garlic bread': 7, 'falafel': 12}
printPicnic(picnicItems, 12,5)
printPicnic(picnicItems, 20,6)