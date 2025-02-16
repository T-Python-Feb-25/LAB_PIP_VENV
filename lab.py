from art import * 
first_phrase=text2art("BELIEVE AND ACHEIVE",font='block',chr_ignore=True) # this will print the text in block font as required 
print(first_phrase)

test1=text2art("BELIEVE\n AND\n ACHEIVE",font='block',chr_ignore=True) #this will print the test in the same required font but in different lines which make it more obvious
print(test1)

second_phrase=text2art("HELLO",font='sub-zero',chr_ignore=True) # Return ASCII text with block font
print(second_phrase)
