import re
pattern=r"Colour"
text1="My favourite Colour is Black.I love green Colour as well"
text2=re.sub(pattern,"color",text1,count=1)
print(text2)