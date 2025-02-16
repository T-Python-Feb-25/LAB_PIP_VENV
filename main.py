
from art import text2art
art_1=text2art("BELIEVE AND ACHEIVE", font="block") # return art as str in normal mode
print(art_1)
art_1=text2art("Hello", font="sub_zero") # return art as str in normal mode
print(art_1)

#/////////////Bonus////////////////
art_1=text2art("Eman") # return art as str in normal mode
print(art_1)



from art import text2art
from colorama import Fore, Style, init
import random

# Initialize colorama
init(autoreset=True)

# List of colors
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE]

# List of phrases with different fonts
phrases = [
    ("Be happy", "block"),
    ("Im Dream", "slant"),
    ("Stay Positive", "bubble"),
    ("must be developer", "standard"),
    ("Never lose", "speed"),
    ("the future", "big"),
   
]

# Print each phrase with a random color
for text, font in phrases:
    ascii_art = text2art(text, font=font)
    color = random.choice(colors)
    print(color + ascii_art)

