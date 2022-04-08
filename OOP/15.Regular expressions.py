import re
pattern=r"color"
text="My favourite color is red"
match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())