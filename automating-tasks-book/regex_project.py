import re
import pyperclip

def scrapeEmailsAndPhoneNumbers(text):
    phoneNumberRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                  # area code (optional)
        (\s|-|\.)?                          # whitespace, hyphen, or dot (optional)
        (\d{3})                             # first 3 digits
        (\s|-|\.{1})                        # whitespace, hyphen, or dot
        (\d{4})                             # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?        # extension (optional)
        )''', re.VERBOSE)

    emailRegex = re.compile(r'''(
        ([a-zA-Z0-9._%+-]+)                   # username
        (@)                                   # at sign
        ([a-zA-Z0-9.-]+)                      # domain
        (\.[a-zA-Z]{2,4})                   # dot, TLD
        )''', re.VERBOSE)

    matches = []

    for numberGroup in phoneNumberRegex.findall(text):
        number = numberGroup[0].strip()
        matches.append(number)

    for emailGroup in emailRegex.findall(text):
        email = emailGroup[0]
        matches.append(email)

    return matches

message = str(pyperclip.paste())
# message = "Hi here's some stuff (318) 834-6909 564-3708 chdprimary@gmail.com a@b 101010 1010 okay 318.560.7909"
results = scrapeEmailsAndPhoneNumbers(message)

if len(results) > 0:
    pyperclip.copy('\n'.join(results))
    print("Copied to clipboard:")
    print('\n'.join(results))
else:
    print("No phone numbers or email addresses found on clipboard.")