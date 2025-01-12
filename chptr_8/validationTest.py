#! python3

import pyinputplus as pyip

# limit responses
# response = pyip.inputNum(limit=2)

# adds time limit to input
# response = pyip.inputNum(prompt="Imput a number under 5 sec", timeout=5)

# adds promt to validator input
# response = pyip.inputNum("Please input a number: ")

# adds regex to input validation
# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

# blocks regex from input validation
# response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# adding regex overrides the block regex argument
# response = pyip.inputStr(prompt='Input a string', allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

# custom validation function

def sumUpToTen(nums):
    print(nums)
    numberList = list(nums)
    print(numberList)
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
    
    finalSum = sum(numberList)
    
    if finalSum != 10:
        raise Exception('The digits must add up to 10, not %s.' %(finalSum))
    print(int(nums))
    return int(nums)


response = pyip.inputCustom(sumUpToTen)