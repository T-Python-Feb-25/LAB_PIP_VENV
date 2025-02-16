from art import text2art
from colorama import Fore, Back, Style

art_1=text2art("""BELIEVE
AND 
ACHEIVE
""",font='block',chr_ignore=True) # Return ASCII text with block font
print(art_1)

art_2 = text2art("Hello", font="sub-zero")
print(Fore.YELLOW,art_2)

