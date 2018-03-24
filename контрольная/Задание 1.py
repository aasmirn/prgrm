with open('text.txt', encoding='utf-8') as f:
    for line in f:
        splitted_line = line.split('|')
        if len(splitted_line[0]) >= 20:
            print(line[:-1])
