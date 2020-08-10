#!/user/bin/env python3

import re, pyperclip

#REGEX FOR PHONE NUMBERS
phoneRegex = re.compile(r'''
# several forms of numbers, XXX-XXX-XXXX, XXX-XXXX,
(XXX) XXX-XXXX, XXX-XXXX ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?          #area code (optional)
(\s|-)                              #first separator
\d\d\d                              #first 3 digits
-                                   #separator
\d\d\d\d                            #last 4 digits
(((ext(\.)?\s)| x)                  # segment of extension with words, either ext(.) or x
(\d{2,5}))?                         # segment of extension with numbers for the extension, lenght of 2-5 digits
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
pyperclip.copy(results)

print("Done")
