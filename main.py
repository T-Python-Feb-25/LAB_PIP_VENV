'''
Create a virtual environment & activate it
Use ART package to print Text Art.
Print the phrase "BELIEVE AND ACHEIVE" designed with font block.
print the phrase "HELLO" designed with font sub-zero.
Bonus
Come up with different phrases with different art and decoration
Use colorama to color the text in the terminal.
'''
from art import *
from colorama import Fore,Back,Style
Art= text2art("BELIEVE AND ACHEIVE", font='block',chr_ignore=True)
print (Art)
Art2=text2art("HELLO", font='sub-zero', chr_ignore=True)
print (Art2)
Art3=text2art("WE are \nusing \nthe Art\nModel with \nColorama",font='block', chr_ignore=True)
print (Fore.BLACK+Back.GREEN+Art3)




'''
LAB_PIP_VENV
Feb16, 2025
By Mohammed Albushaier
'''
