"""# LAB_PIP_VENV


## using what you've learned , create a new project to print Text Art in the terminal :
- Create a virtual environment & activate it
- Use ART package to print Text Art.

- Print the phrase "BELIEVE AND ACHEIVE" designed with font `block`.
- print the phrase "HELLO" designed with font `sub-zero`.


## Bonus
- Come up with different phrases with different art and decoration
- Use colorama to color the text in the terminal.


### checkout the package on pip
https://pypi.org/project/art/
"""

from art import tprint
from colorama import Fore, Back, Style


tprint('''BELIEVE
AND
ACHEIVE''', font="block",chr_ignore=True) 
print(Fore.BLUE)
tprint('Hello',font="sub-zero",chr_ignore=True)
print(Fore.LIGHTMAGENTA_EX+Back.WHITE)
# print(DECORATION_NAMES)
tprint("Sabreen",font="white_bubble",chr_ignore=True,decoration="snow1",space=2)
print(Style.BRIGHT+Back.RESET+Fore.RED)
tprint("Sabreen",font="cybermedum",chr_ignore=True)
