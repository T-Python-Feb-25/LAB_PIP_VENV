from art import text2art
from colorama import Fore, Back, Style
art_3 = text2art("success", font="starwars")
print(Fore.BLUE + Style.BRIGHT + art_3)

art_4 = text2art("dangerous", font="starwars")
print(Fore.RED + Style.BRIGHT + art_4)

art_5 = text2art("CODE & PYthon", font="epic")
print(Fore.LIGHTBLACK_EX + Style.BRIGHT,art_5)

art_6 = text2art("Keep going", font="big")
print(Fore.LIGHTBLACK_EX + art_6)
