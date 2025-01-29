from pathlib import Path
import os

# myPath = Path('spam', 'omlett', 'mushroom', 'bacon', 'spring-onion')

# print(myPath)

helloFile = open(Path.cwd() / './hello.txt')
helloContent = helloFile.read()
print(helloContent)



myFile = open(Path.cwd() / './lines.txt')
myLines = myFile.readlines()
print(myLines)


chapter = Path.cwd()
print(chapter)

baconFile = open(chapter / 'bacon.txt', 'w')
print(baconFile)
baconFile.write('Hello bacons! My name is pork')
baconFile.close()

baconFile = open(chapter / 'bacon.txt', 'a')
print(baconFile)
baconFile.write('\nThis is my crazy line')
baconFile.close() 