
stroka = (input())
def palindrom(stroka):
    string1 = stroka
    string2 = ''.join(reversed(stroka))
    if string1 == str(string2):
        print(True)
    else:
        print(False)
palindrom(stroka)


