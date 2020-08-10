#!/user/bin/env python3

import re, pyperclip

#REGEX FOR PHONE NUMBERS
phoneRegex = re.compile(r'''
# several forms of numbers, XXX-XXX-XXXX, XXX-XXXX,
(XXX) XXX-XXXX, XXX-XXXX ext 12345, ext. 12345, x12345
(
(\d{3}|\(\d{3}\))?        #area code (optional)
(\s|-|\.)?                             #first separator
\d{3}                             #first 3 digits
(\s|-|\.)                              #separator
 \d{4}                            #last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?                #extension 
)                                   #re.VERBOSE allows for white spaces and comments

''', re.VERBOSE)
# REGEX FOR EMAIL ADDRESSES
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+-]+  #name portion
@                 #@symbol seperating name and domain
[a-zA-Z0-9_.+-]+  #domain portion
''', re.VERBOSE)
                            
# GET TEXT OFF CLIPBOARD
text = pyperclip.paste()
                        
# EXTRACT EMAIL/PHONE FROM CLIPBOARD TEXT
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# COPY EXTRACTED TEXT TO CLIPBOARD
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

if len(results) > 0:
    pyperclip.copy(results)
    print('Copied to clipboard:')
    print('\n'.join(results))
else:
    print('No phone numbers or email addresses found.')
