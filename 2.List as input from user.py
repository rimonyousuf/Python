numberOfLetters=0
numberOfDigits=0
numberOfWords=0

text=input("Enter any text : ")

for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        numberOfLetters=numberOfLetters+1
    elif x>='0' and x<='9':
        numberOfDigits=numberOfDigits+1
    elif x==' ':
        numberOfWords=numberOfWords+1

print("Number of Letters :",numberOfLetters)
print("Number of Digits :",numberOfDigits)
print("Number of Words :",numberOfWords+1)