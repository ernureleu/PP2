import re

text=input()

m = ''.join(x.capitalize() or '_' for x in text.split('_'))

print(m)