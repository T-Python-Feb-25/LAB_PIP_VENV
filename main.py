from art import text2art
from colorama import Fore ,Style

art1 = text2art("BELIEVE AND ACHIEVE", font="block")
print(Fore.CYAN + art1 + Style.RESET_ALL)

art2 = text2art("HELLO", font="sub-zero")
print(Fore.GREEN + art2 + Style.RESET_ALL)


art3 = text2art("PYTHON", font="random")
print(Fore.YELLOW + art3 + Style.RESET_ALL)
