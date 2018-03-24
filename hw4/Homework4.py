with open('text.txt', encoding='utf-8') as f:
    text=f.read()
    lines=text.splitlines()
    minimum=len(lines[0])
    maximum=len(lines[0])
    for line in lines:
        if len(line)<minimum:
            minimum=len(line)
        if len(line)>maximum:
            maximum=len(line)
    if minimum==0:
        print('Самая короткая строка данного текста - пустая. Попробуйте от неё избавиться =)')
    else:
        a=maximum/minimum
        if a==1:
            print('Все строки данного текста одинаковой длины.')
        elif a//1==a and ((a>=2 and a<=4) or (a%100>20 and a%100%10>=2 and a%100%10<=4)):
            print('Самая короткая строка данного текста короче самой длинной в',a,'раза.')
        else:
            print('Самая короткая строка данного текста короче самой длинной в',a,'раз.')
        
