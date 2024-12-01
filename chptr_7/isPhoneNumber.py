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

