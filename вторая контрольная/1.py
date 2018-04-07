import re

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def fwrite(i):
    with open('answer.txt', 'w', encoding='utf-8') as f:
        f.write('Число строк в файле: ' + i)

def main():
    i = 0
    for s in re.findall(r'\n', re.findall(r'<se>\s([\S\s]*?)</se>', fread('mystem.xml'))[0]):
        i += 1
    fwrite(str(i))
    print('Ответ записан в файл answer.txt')
    
if __name__ == '__main__':
    main()
