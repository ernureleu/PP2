import re
text = input()

pattern = r'\w*a[0b]\w*'

print(re.findall(pattern, text))

