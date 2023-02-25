import re

text = input()

pattern = r'[A-Z][a-z]+'

x = re.findall(pattern, text)

print(x)