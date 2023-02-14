n = int(input()) 

def div(x):
    for i in range(x):
        if i % 12 == 0:
            yield i 

a = list(div(n)) 

print(a)

# 100
# [0, 12, 24, 36, 48, 60, 72, 84, 96]