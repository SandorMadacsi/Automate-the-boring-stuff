#! python3
#madlibs.py


from pathlib import Path
import pyinputplus as pyip
import re

patterns = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
myFile = open(Path.cwd() /'./test.txt', 'r+')

myContent = myFile.read()
myFile.seek(0)
for pattern in patterns: 
    myRegex = re.compile(pattern)
    results = myRegex.findall(myContent)
    if len(results) > 0:
        for result in results:
            sub = pyip.inputStr('Enter a %s: ' %(pattern.lower()))
            myContent = re.sub(myRegex,sub,myContent, count=1)

myFile.write(myContent)
myFile.truncate()
myFile.close()

