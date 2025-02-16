from art import *
from colorama import Fore, Back


text1 = text2art("BELIEVE AND ACHEIVE", font="block")
print(text1)

text2 = text2art("HELLO",font='sub-zero')
print(text2)

text3 = text2art("Nawaf",font="shadow")
print(Fore.BLUE + text3)

text4 = text2art("Alahmadi",font="lean")
print(Back.WHITE + text4)


