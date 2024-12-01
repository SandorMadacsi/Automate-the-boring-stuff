#! python3
# mclip.py - A multi-clipboard program.”

TEXT = {'thanks': """Thank you for your time!

                      Kind Regards,
                      Sandor Madacsi""",
        'greet': """Hi,
                    
                    I hope this email finds you well."""}

import sys, pyperclip
if len(sys.argv) < 2:
 print('Usage: python mclip.py [keyphrase] - copy phrase text')
 sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase
if keyphrase in TEXT:
   pyperclip.copy(TEXT[keyphrase])
   print('Text for ' + keyphrase + ' copied to clipboard.')
else:
   print('There is no text for ' + keyphrase)



