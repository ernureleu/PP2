import re

text = input()

x = re.findall("[A-Z][^A-Z]*", text)

for i in x :
    print(i, end=" ")
