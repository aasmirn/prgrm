with open('text.txt', encoding = 'utf-8') as f:
    n = 0
    for line in f:
        splitted_line = line.split('|')
        if len(splitted_line[2]) > 0:
            n += 1
    print('Количество слов с антонимами:',n)
