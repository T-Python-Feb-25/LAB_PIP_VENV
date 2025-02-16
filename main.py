from art import text2art
from colorama import Fore, Style

block_art = text2art("BELIEVE AND ACHIEVE", font="block")
print(Fore.CYAN + block_art + Style.RESET_ALL)


subzero_art = text2art("HELLO", font="sub-zero")
print(Fore.MAGENTA + subzero_art + Style.RESET_ALL)


bubble_art = text2art("Dream Big", font="bubble")
print(Fore.RED + bubble_art + Style.RESET_ALL)

print(Fore.BLUE + "Goodbye" )
