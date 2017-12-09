#! python

import webbrowser, sys, pyperclip, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.debug('Starting program...')

if len(sys.argv) > 1:
    logging.debug('Provided cmdline argument: ' + str(sys.argv[1:]))
    address = ' '.join(sys.argv[1:])
else:
    logging.debug('Pasting from clipboard: ' +str(pyperclip.paste()))
    address = pyperclip.paste()

logging.debug('Opening browser...')
webbrowser.open('https://www.google.com/maps/place/' + address)

logging.debug('Ending program...')