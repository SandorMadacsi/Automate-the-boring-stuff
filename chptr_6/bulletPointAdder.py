#! python3
# Formating text to list items
import pyperclip

text = pyperclip.paste()


lines = text.split("\n")
for i in range(len(lines)):
    lines[i] ='[] ' + lines[i]

final = ('\n').join(lines)
print('Text is copied to clipboard!')
pyperclip.copy(final)


