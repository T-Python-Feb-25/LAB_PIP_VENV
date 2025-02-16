from art import text2art
from colorama import Fore, Back, Style
'''
هنا خليناالوان النص قبل امر لطباعه
 عشان تكون معممه على الاوامر كلها بل ما اخصص الالوان لكل نص 
 
'''
print(Fore.MAGENTA)
print(Back.BLACK)
print (text2art("BELIEVE AND ACHEIVE",font="block"))
print(text2art("HELLO",font="sub-zero"))
print(text2art("my name is rahaf ahmed fallatah",font="random"))
