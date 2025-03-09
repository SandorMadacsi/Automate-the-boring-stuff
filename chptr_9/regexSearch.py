#! python3
#regexSearch.py
#input search word to look for in all text files in working directory

import re, sys, pyinputplus as pyip
from pathlib import Path

prompt = 'Input your regular expression to search for: '
regexPattern = pyip.inputStr(prompt)
myRegex = re.compile(regexPattern)

mainPath = Path.cwd()
ext = "*.txt"

files = list(mainPath.glob(ext))
for filePath in files:
    myFile = open(filePath)
    myContent = myFile.read()
    

    results = myRegex.findall(myContent)
    if len(results) > 0:
        print("Results in %s :" %(filePath.name))
        for result in results:
            print(result)
    else:
        print("Not found in %s " %(filePath.name)) 