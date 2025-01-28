#! python3

import pyinputplus as pyip


extras = []

print("Welcome to the sandwitch maker!")

price = 0.0
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
price += 0.5
print(price)

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
price += 1


if pyip.inputYesNo(prompt="Do you need cheese?") == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    price += 0.3

if pyip.inputYesNo(prompt="Do you need mayo?") == 'yes':
    extras.append('Mayo')
    price += 0.1

if pyip.inputYesNo(prompt="Do you need mustard?") == 'yes':
    extras.append('Mustard')
    price += 0.1

if pyip.inputYesNo(prompt="Do you need lettuce?") == 'yes':
    extras.append('Lettuce')
    price += 0.1

if pyip.inputYesNo(prompt="Do you need tomato?") == 'yes':
    extras.append('Tomato')
    price += 0.1

print(price)
numOfSandwiches = pyip.inputInt("How many sandwiches do you need?", min=1)
price *= numOfSandwiches
print(price)
print("The final cost of your order is: %f £" % (price))
