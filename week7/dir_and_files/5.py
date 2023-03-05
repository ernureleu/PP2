import os

aa = input().split()
with open('5zadacha.txt', 'a') as f:
    for i in aa:
        f.write(i)
        f.write(' ')
    f.close()