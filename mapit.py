#! python3
# mapit.py - Launches a map in the browser using an address from the 
# command line or clipboard

import pyperclip as pc
import webbrowser as wb
import sys

if len(sys.argv) > 1:
    # Get the address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pc.paste()

wb.open(f'https://www.google.com/maps/place/{address}')