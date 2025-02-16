from art import text2art,tprint
from colorama import Fore,Back

art = text2art("Raed",font="small")
print(Fore.CYAN +art)
print(Fore.RESET)

art_2 = text2art("Python",font="cybermedum")
print(Fore.GREEN + art_2)
print(Fore.RESET)

print(Back.YELLOW)
print(Fore.RED)
tprint("Raed")
print(Fore.RESET)
print(Back.RESET)