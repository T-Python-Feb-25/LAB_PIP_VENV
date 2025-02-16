from colorama import Fore,Back,Style
from art import text2art

print(Fore.LIGHTCYAN_EX+text2art("BELIEVE AND ACHIEVE", font='block'))


print(Style.BRIGHT+Fore.LIGHTGREEN_EX+text2art("hello", font='sub-zero'))

print(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+Back.LIGHTWHITE_EX+text2art("Dream Big, Work Hard!"
                                    "\nYou Can Do It <3", font="script"))

