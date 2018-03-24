import re
import os

def getfile():
    return input('Введите имя файла: ')

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return re.sub('\W', ' ', f.read()).lower()

def words(search, forms):
    for word in search:
        forms.append(word[:-1])
    return forms
    

def search(text):
    forms = []
    forms = words(re.findall('найтис?ь?\s', text), forms)
    forms = words(re.findall('наш[её]?л[аои]?с?[яь]?\s', text), forms)
    forms = words(re.findall('найд[яуеёи][тмш]?[ье]?с?[ья]?\s', text), forms)
    forms = words(re.findall('найден[аоы]?н?[а-я]{0,3}\s', text), forms)
    forms = words(re.findall('нашедш[а-я]{1,3}с?[ья]?\s', text), forms)
    return forms

def dic(array):
    d = {}
    for word in array:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def getkeys(d, file):
    if d == {}:
        print('Необходимых форм не найдено.')
    else:
        print("Формы глагола 'найти' в вашем тексте:")
        for word in list(d.keys()):
            print('\t' + word)
        choice = input('Если хотите узнать частотность конкретной формы, введите её: ').lower()
        while choice in dic(search(fread(file))):
            print(dic(search(fread(file)))[choice])
            choice = input('Можете ввести другую форму: ').lower()

def main():
    file = getfile()
    if os.path.exists(file) == False:
        print('Файл не найден.')
    else:
        getkeys(dic(search(fread(file))), file)
        print('Спасибо, что воспользовались этой программой!')
            

if __name__ == '__main__':
    main()
