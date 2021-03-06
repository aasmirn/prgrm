import re
import os

def getfile():
    return input('Введите имя файла: ')

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def main():
    file = getfile()
    if os.path.exists(file) == False:
        print('Файл не найден.')
    else:
        with open('info.txt', 'w', encoding='utf-8') as f:
            m = re.findall(r'<a href="/wiki/UTC.*?" class="mw-redirect" title="UTC.*?">(.*?)</a>', fread(file))
            if len(m) == 0:
                f.write('К сожалению, на странице нет информации о часовом поясе.')
            if len(m) == 1:
                f.write('Часовой пояс вашего города: '+m[0])
            if len(m) > 1:
                f.write('Часовой пояс вашего города зимой: ' + m[0] + '; летом: ' + m[1])
        print('Информация записана в файл info.txt')
        
if __name__ == '__main__':
    main()
