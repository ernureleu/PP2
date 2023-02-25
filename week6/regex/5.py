import re
text = input()

pattern = r'^a\w*b\w*'

print(re.findall(pattern, text))


