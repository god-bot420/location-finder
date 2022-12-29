#show my location on google maps
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    
else:
    # Get address from clipboard.
    address = pyperclip.paste()
    #address = "White House Washington D.c."
webbrowser.open('https://www.google.com/maps/place/' + address)
print(address)

#!/usr/bin/env python3
