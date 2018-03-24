print('Введите слово:')
a=input()
if len(a)==0:
    print('Вы ввели пустую строку.')
else:
    print('Ваша абракадабра:')
    for i in range(1,len(a)+1):
        print(a[0:i])
