#Во всех файлах найдите все имена собственные (их леммы должны
#быть написаны с заглавной буквы) и подсчитайте, сколько раз
#каждое из них встретилось во всей текстовой коллекции. Результаты
#запишите в таблицу со столбцами: найденное имя, количество вхождений.
#В качестве разделителя надо использовать табуляцию.


import re
import os

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def getfiles(direc):
    return os.listdir(direc)

def findcapitals(text):
    words = re.findall(r'<w><ana lex="(.*?)".*?</w>', text)
    capitals = [word for word in words if word.istitle()]
    return capitals

def main():
    d = {}
    for file in getfiles('news'):
        text = fread('news\{}'.format(file))
        for title in findcapitals(text):
            if len(title) > 1:
                if title in d:
                    d[title] += 1
                else:
                    d[title] = 1
    with open('titles.tsv', 'w', encoding='utf-8') as f:
        for k in d.keys():
            f.write('{}\t{}\n'.format(k, d[k]))
        

if __name__ == '__main__':
    main()
