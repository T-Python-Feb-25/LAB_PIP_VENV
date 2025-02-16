from art import text2art
from colorama import Fore, Back, Style

def print_makeup_art(phrase, font, text_color, border_color):
    art_text = text2art(phrase, font=font)
    border = border_color + "=" * (len(phrase) * 6) 

    print(border)
    print(text_color + art_text)
    print(border)
    print(Style.RESET_ALL)  

print_makeup_art("MAKEUP IS ART", "block", Fore.MAGENTA, Fore.YELLOW)
print_makeup_art("BLEND IT LIKE A PRO", "slant", Fore.RED, Fore.CYAN)
print_makeup_art("LIPSTICK & CONFIDENCE", "3d", Fore.YELLOW, Fore.MAGENTA)
print_makeup_art("GLOW UP", "sub-zero", Fore.CYAN, Fore.WHITE)
print_makeup_art("SLAY THE LOOK", "speed", Fore.BLUE, Fore.RED)