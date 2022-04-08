import re
pattern=r"Color"
if re.match(pattern,"Color is red,I love red Color"):
    print("Match")
else:
    print("Not match")

if re.search(pattern,"Rose is red,I love red Color"):
    print("Match")
else:
    print("Not match")

print(re.findall(pattern,"Is it red Color?No it is orange Color"))