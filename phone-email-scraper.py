#!/user/bin/env python3

import re, pyperclip

#TODO:
    # Create REGEX FOR PHONE NUMBERS
    re.compile(r'''
# several forms of numbers, XXX-XXX-XXXX, XXX-XXXX,
(XXX) XXX-XXXX, XXX-XXXX ext 12345, ext. 12345, x12345

((\d\d\d) | (\(\d\d\d\)))?          #area code (optional)
            #first separator
            #first 3 digits
            #separator
            #last 4 digits
            # extension (optional)


''', re.VERBOSE
    # CREATE REGEX FOR EMAIL ADDRESSES
    # GET TEXT OFF CLIPBOARD
    # EXTRA EMAIL/PHONE FROM CLIPBOARD TEXT
    # COPY EXTRACTED TEXT TO CLIPBOARD
