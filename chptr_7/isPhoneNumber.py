import re


def isPhoneNumber(input):
    myRegex = re.compile(r"(\d{3}-\d{3}-)(\d{4})")
    result = myRegex.search(input)

    # if len(input) != 12:
    #     return False
    # for i in range(0,3):
    #     if not input[i].isdecimal():
    #         return False
    # if input[3] != '-':
    #         return False
    # for i in range(4,7):
    #      if not input[i].isdecimal():
    #         return False
    # if input[7] != '-':
    #         return False
    # for i in range(8,12):   
    #     if not input[i].isdecimal():
    #         return False
    return result


myPhone = isPhoneNumber('my pphe number 415-555-4242')

print('Phone number found: ' + myPhone.group(1))

print('Phone number found: ' + myPhone.group(0))

areaCode, mainNum = myPhone.groups()

print(areaCode, mainNum)


# Matching multiple groups with pipe

myWord = re.compile(r"Bat(man|animal|mobile|bat)")

result = myWord.search("my Batmobile is my favourite Batbat its a Batanimal")
print(result.groups())



# Optional matching with ?

myOptional = re.compile(r'Bat(wo)?man')

result1 = myOptional.search('The story of my Batman')


result2 = myOptional.search('The other story of Batwoman')

res1 = result1.group()

res2 = result2.group()

# print(res1)
# print(res2)

# Optional area code

myArea = re.compile(r'(\(\d{3}\)-)?\d{3}-\d{4}')

res1 = myArea.search('(415)-555-4242')
res2 = myArea.search('555-4242')
#print(res2.group())

# Matching  pattern with 0 or more occurance using '*'

myRegex = re.compile(r'(\(\d{3}\)-)*(\d{3}-\d{4})')

res = myRegex.search('(415)-555-4242')
print(res.group())

# Matching  pattern with 1 or more occurance using '+'

myRegex = re.compile(r'(\(\d{3}\)-)+(\d{3}-\d{4})')

res1 = myRegex.search('(415)-555-4242')
res2 = myRegex.search('233124')
print(res1.group())
print(res2 == None)


# Matching a repetition of a pattern

myRep = re.compile(r'(wa){2,6}')
res = myRep.search('wawawawelcome')
print(res.group())

# Use '?' to lazy search (finding the shortest match)
myRep = re.compile(r'(wa){2,6}?')
res = myRep.search('wawawawelcome')
print(res.group())


# findall() method matches all occurances of a pattern. Without groups int returns a list of matched strings With groups it returns a list of tuples of the matched groups

myRegex = re.compile(r'chicken(sandwitch|roast|pizza)')
chicken = myRegex.findall('It is a great chickensandwitch but I prefer chickenpizza')
print(chicken)

# Defining own classes with squared brackets

myClass = re.compile(r'[aeu]')
res = myClass.findall(' It is a beautiful day and I love it')
print(res)

# Negative class by using carrot sign after initial square bracket

myClass = re.compile(r'[^aeu]')
res = myClass.findall(' It is a beautiful day and I love it')
print(res)


# Carrot at the beginning of expression to start with the pattern
myBeginning = re.compile(r'^Hello')
res = myBeginning.findall('Hello world!')
print(res)

# Matcing Evering with Dot-Star

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
res = nameRegex.search('First Name: John Last Name: Smith')
print(res.group(1))
print(res.group(2))

# Case-Insensitive Matching

myInsensitive = re.compile('robocop', re.I)
res = myInsensitive.findall('ROBOcop robocOP roboCOP RoBoCoP')
print(res)


nameRegex = re.compile(r'Agent \w+')
myNames = nameRegex.sub('CENSORED', 'Agent James gave the files to Agent Thomson')
print(myNames)


nameRegex = re.compile(r'Agent (\w)\w*')
myNames = nameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(myNames)

# Complex Regex with re.VERBOSE


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


# Passing ignorecase , dotall and verbose to the compile
# IGNORECASE - ignores wheter a letter is capital or not
# DOTALL - matches everyhting including line brakes
# VEROBSE - enables multiline code for regex
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) 