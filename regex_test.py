import re

def findMyExpression(input):
    myExpression = re.compile(r'Bath(wo)+man')
    result= myExpression.search(input)
    return result


mo = findMyExpression('My favourite movie is Bathwowowoman')
print(mo.group())