import re

text=input()

x = re.findall("[A-Z][^A-Z]*", text)

print(x)