import re

text = input()

x = re.sub('\s', ',', text)

print(x)