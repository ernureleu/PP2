stroka = input()

def func(stroka):
    count_1 = 0
    count_2 = 0
    for i in range(len(stroka)):
        if stroka[i] >= 'A' and stroka[i] <= 'Z':
            count_1 += 1
        else:
            count_2 += 1
    print(f'Uppercase number:{count_1}')
    print(f'Lowercase number:{count_2}')
func(stroka)