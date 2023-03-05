import os
# os.walk

BASE_URL = os.getcwd()

for root, dirs, files in os.walk(BASE_URL):
    print(root)
    print('all DIRECTORIES:')
    for dir in dirs:
        print(dir)
    print('ALL FILES:')
    for file in files:
        print(file)