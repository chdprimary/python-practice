import re

# without using regex
def isPhoneNumber(text):
    if len(text) < 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# using regex
def isPhoneNumberUsingRegex(text):
    pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}')
    result = pattern.search(text)
    if result:
        if result.group():
            return True

def test(message, usingRegex=False):
    for i in range(0, len(message)-13):
        chunk = message[i:i+14]
        # print(chunk)
        if usingRegex:
            if isPhoneNumberUsingRegex(chunk):
                print('Phone number found: ' + chunk)
        else:
            if isPhoneNumber(chunk):
                print('Phone number found: ' + chunk)
    print('Done')

message1 = "This program recognizes that 313-515-8181 and 555-555-5555 are phone numbers but that 1824-654-85 is not."
test(message1, False)
test(message1, True)
message2 = "This program recognizes that (313) 515-8181 and 555-555-5555 are phone numbers but that (1824) 654-85 is not."
test(message2, False)
test(message2, True)
