import os

def ask_name():
    fname = input('Введите имя файла: ')
    return fname

def read_file(fname):
    with open(fname, encoding = 'utf-8') as f:
        return remove(f.read().lower()).split()
        
def remove(text):
    symbols_to_remove = """.,!"()/?'—-:;«»…"""
    for s in symbols_to_remove:
        if s in text:
            text = text.replace(s, '')
    return(text)

def make_dict(text):
    dic = {}
    for word in text:
        if word.endswith('ness'):
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    return dic

def count(dic):
    number = 0
    for v in dic.values():
        number += v
    return number

def maximum(dic):
    words = sorted(dic, key = dic.get, reverse = True)
    return words[0]

def give_results():
    file = ask_name()
    if os.path.exists(file) == False:
        print('Файл не найден.')
    else:
        if make_dict(read_file(file)) == {}:
            print('В вашем тексте нет слов на -ness.')
        else:
            print('Всего слов на -ness:', count(make_dict(read_file(file))))
            print('Самое частое слово на -ness:', maximum(make_dict(read_file(file))))

give_results()
