#! python3

# phoneAndEmail.py - Finds phone numbers and emails then pastes to clipboard

import pyperclip, re


emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        )''',re.VERBOSE)




phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?
                        (\s|-|\.)?
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})
                        (\s*(ext|x|ext.)\s*\d{2,5})?
                            )''',re.VERBOSE)



input = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(input):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)

for groups in emailRegex.findall(input):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')