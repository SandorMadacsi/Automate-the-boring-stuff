 #! python3
 
import pyinputplus as pyip


extras = []

print("Welcome to the sandwitch maker!")

price = 0
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
price += 0.5

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
price += 1

print("Do you need cheese?")
if pyip.inputYesNo() is 'y' or pyip.inputYesNo() is 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    price += 0.3
print("Do you need mayo?")
if pyip.inputYesNo() is 'y' or pyip.inputYesNo() is 'yes':
     extras.append('Mayo')
     price += 0.1
print("Do you need mustard?")
if pyip.inputYesNo() is 'y' or pyip.inputYesNo() is 'yes':
     extras.append('Mustard')
     price += 0.1
print("Do you need letuce")
if pyip.inputYesNo() is 'y' or pyip.inputYesNo() is 'yes':
     extras.append('Letuce')
     price += 0.1
print("Do you need tomato?")
if pyip.inputYesNo() is 'y' or pyip.inputYesNo() is 'yes':
     extras.append('Tomato')
     price += 0.1
     
numOfSandwiches = pyip.inputInt("How many sandwiches do you need?", min=1)
price *= numOfSandwiches
print("The final cost of your order is: %d £" % (price))