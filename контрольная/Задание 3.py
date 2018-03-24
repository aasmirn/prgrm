words = []
info = ''
print('Введите слова:')
a = input()
if a == '':
     print('Вы ничего не ввели. Перезапустите программу и попробуйте ещё раз.')
else:
    while a != '':
        words.append(a)
        a = input()
        continue
        if a == '':
            break
    for word in words:
        info_upd = info
        with open('text.txt', encoding = 'utf-8') as f:
            for line in f:
                splitted_line = line.split('|')
                if splitted_line[0] == word:
                    example = splitted_line[3]
                    info_upd += splitted_line[0] + ' – ' + example[:-1] + ' – ' + splitted_line[1] + '\n'
            if info_upd == info:
                info_upd += '\"' + word + '\"' + ' не найдено в словаре\n'
            info = info_upd
    print(info[:-1])  
            
