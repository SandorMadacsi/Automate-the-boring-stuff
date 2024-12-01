#! python3

print("Insert a sentance to be translated into pig latin:")
#userInput = input()

userInput = "My name is GEORGE and I am 2000 years old."

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []

words = userInput.split()



prefix = ''
suffix =''
for i,word in enumerate(words):
    print(word)
    while(len(word) > 0 and not word[0].isalpha()):
        prefix += word[0]
        word = word[1:]
    if(len(word) == 0):
        pigLatin.append(prefix)
        continue

    while not word[-1].isalpha():
        suffix += word[-1] + suffix
        word = word[:-1]
    
    isTitle = word.istitle()
    isUpper = word.isupper()

    word = word.lower()
    prefixConsonants = ''
    while len(word)> 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    if prefixConsonants != "":
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    if isUpper:
        word = word.upper()
    if isTitle:
        word = word.title()
    
    pigLatin.append(prefix + word + suffix)

print(' '.join(pigLatin))
