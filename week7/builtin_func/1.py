a = list(input().split())

def product(ab):
    prod = 1
    aa = list(ab)
    for i in aa:
        prod *= int(i)
    print(prod)
product(a)