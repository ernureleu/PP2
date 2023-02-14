n = int(input())

def even(x):
    for i in range(x):
        if i % 2 == 0: 
            yield str(i) + ','

a = ' '.join(list(even(n)))
print(a[0:len(a)-1])

# 22
# 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20