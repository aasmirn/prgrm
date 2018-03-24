print('Введите числа: ')
a=input()
n=0
s=0
if a == '':
    print('Вы ничего не ввели.')
else:
    a=int(a)
    maximum=a
    minimum=a   
    while a!='':
        a=int(a)
        n+=1
        s+=a
        if a>maximum:
            maximum=a
        if a<minimum:
            minimum=a
        a=input()
        if a=='':
            break
    av=s/n
    print('Среднее арифметическое введенных чисел: ', av)
    print('Минимальное из введенных чисел: ', minimum)
    print('Максимальное из введенных чисел: ', maximum)
