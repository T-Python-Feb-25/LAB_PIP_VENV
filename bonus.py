import art
from colorama import init, Fore
init()

try:


    user_font = input("Enter type of font you want: ")
    
    user_phrase = input("Enter the phrase: ")
    user_color = input("Enter the font color: ").upper()
    
    color_dict = {
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    color = color_dict.get(user_color, Fore.WHITE)
    
    text_art = art.text2art(user_phrase, font=user_font)
    colored_text = color + text_art
    print(colored_text)
    
except Exception as e:
    print(f"An error occurred: {e}")