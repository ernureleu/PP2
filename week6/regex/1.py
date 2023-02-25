import re
text = input()

pattern = r'\w*a{2,3}b\w*'

print(re.findall(pattern, text))