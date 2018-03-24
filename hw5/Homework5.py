print('Введите слова:')
with open('words.txt', 'w', encoding='utf-8') as f:
    a=input()
    if a=='':
        print('Вы ничего не ввели. Попробуйте ещё раз.')
    else:
        while a!='':
            if len(a)>5:
                f.write(a)
                f.write('\n')
            a=input()
            if len(a)==0:
                break
print('Слова, удовлетворяющие условию(если есть), введены в файл.')
