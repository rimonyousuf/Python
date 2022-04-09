import re
pattern1=r"^colo.r$"
if re.match(pattern1,"colour"):
    print("Matched")
else:
    print("Not matched")

pattern2=r"(ab)*"
if re.match(pattern2,"color"):
    print("Matched")
else:
    print("Not matched")

pattern3=r"c+"
if re.match(pattern3,"olor"):
    print("Matched")
else:
    print("Not matched")

pattern4=r"Ice(-)?Cream"
if re.match(pattern4,"Ice-Cream"):
    print("Matched")
else:
    print("Not matched")

pattern5=r"a{1,3}$"
if re.match(pattern5,"aaaa"):
    print("Matched")
else:
    print("Not matched")

