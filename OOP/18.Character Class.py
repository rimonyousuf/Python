import re
pattern1=r"[A-Z][a-z][0-9]"

if re.match(pattern1,"I think he is a great man"):
    print("Matched")
else:
    print("Not matched")

pattern2=r"[A-Z]"

if re.match(pattern2,"I think he is a great man"):
    print("Matched")
else:
    print("Not matched")

