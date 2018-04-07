import re

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def make_dict(array):
    dic = {}
    for el in array:
        if el in dic:
            dic[el] += 1
        else:
            dic[el] = 1
    return dic

def fwrite(dic):
    with open('answer.txt', 'w', encoding='utf-8') as f:
        for k in dic:
            f.write(k + ' = ' + str(dic[k]) + '\n')

def main():
    forms = re.findall(r'gr="(.*?)"', fread('mystem.xml'))
    dic = make_dict(forms)
    fwrite(dic)
    print('Ответ записан в файл answer.txt')
    
if __name__ == '__main__':
    main()
