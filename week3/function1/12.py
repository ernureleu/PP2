def histogram(a):
    for i in a:
        for j in range(i):
            print('*', end='')
        print()

histogram([4, 9, 7])