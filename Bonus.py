'''
## Bonus
- Come up with different phrases with different art and decoration
- Use colorama to color the text in the terminal.
'''
from art import *
from colorama import Fore, Back, Style
print(Fore.GREEN,text2art("happy new year",font='slant',decoration="star1"))
print(Style.RESET_ALL)
print(Fore.RED,text2art("Don't give up",font='big',decoration="heart2"))

