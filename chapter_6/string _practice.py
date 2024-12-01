import pyperclip



# Using backslash to create line breaks
print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw string
print(r"That is Carol\s cat")


''' Multi line comment
    Explaining the multi line string usage
    below
    '''
print(''' Dear Madam,
      
        I am contacting you regarding an important document that Cat's dog ate.
        
        
        Kind Regards,
        Sandor''')



spam = "Hello, World!"

print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[1:7])

#This doesn't modify the initial string but stores the first slice of it in a new variable
first_part = spam[0:7]


# The 'in' and 'not in' operators can be used with Strings
print('Hello' in spam)

# String interpolation
name = 'Sandor'
age = 27
print('Hello, my name is %s and I am %s years old' %(name, age))

# Python 3.6 introduced f-strings
print(f'My name is {name} and I will be {age + 1} next year')


# upper() and lower() methods don't change the original strange but create a new string
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)


# isupper() and islower() return boolean if they find one charecter matching the criteria
print(spam.islower())

print(spam.upper().islower())

# Some useful isX() methods

print('abc'.isalpha()) #True
print('abc1345'.isalpha()) #False
print('aed32'.isalnum()) #True
print('hi'.isalnum()) #True
print('This Is A Title'.istitle()) #True
print('This isn"t a title'.istitle()) #False



# startswith() and endswith() to check part of string

print('Hello, World'.startswith('Hello,')) #True
print('bob'.startswith('b')) #True
print('bob'.endswith('b')) #True


# join() is called on the string that will join the list of strings by

print('/'.join(['horses', 'cats', 'sheeps', 'dogs']))

# split() is called on the string to be split into a list of strings

print('My name is dog'.split())




email = """
         Dear Sender,
         
         I am away at the moment but I soon will come back and can respond to your query.
         Thank you for your time.
         
         Kind Regards,
         Developer"""
        
        
lines = email.split('\n')
#print(lines)




# partition() splitting the given string into 3 substings. A 'before' the given string and 'after'

partitioned = 'my separator string'.partition('sepa')
print(partitioned)



# Justifying text

print('Tittle'.rjust(10,'*'))
print('Tittle'.ljust(10,'*'))
print('Tittle'.center(20,'*'))


# Stripping strings

trimmable = '    Hello my name is  Jeff    '
trimmable = trimmable.strip()
print(trimmable)



#Access unicode value of character with ord()

print(ord('%'))


#Access character by passing unicode value to chr()

print(chr(77))


# Accessing clip board info
print(pyperclip.paste())



