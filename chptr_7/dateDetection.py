#! python3

# dateDetection.py - detects dates

import pyperclip, re

input = str(pyperclip.paste())


dateRegex = re.compile(r'''(
                       ([0-2]?\d{1}|[3][0,1]{1})
                       (\/)
                       ([0,1]?\d{1})
                       (\/)
                       ([1]{1}[9]{1}\d{2}|[2]{1}\d{3})
                        )''',re.VERBOSE)


matches = []
for groups in dateRegex.findall(input):
    day, month, year = (groups[1],groups[3],groups[5])
    print(groups[0])
    matches.append(str((day, month, year)))

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates were found.')




