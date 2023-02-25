import re

text=input()

x=re.findall("[a-z]+", text)

y=re.findall("[A-Z]+[a-z]+",text)

for j in x:
    print(j, end="")
    break

for i in y :
    print("_" , end="")
    print(i.lower(),end="")

