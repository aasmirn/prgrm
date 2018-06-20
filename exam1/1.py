# Для каждого файла сделайте следующее: восстановите исходный текст и
#сохраните его в новый файл с тем же названием, но расширением .txt
#и в кодировке «cp1251». В первой строке нового файла напишите
#название новости, взяв его из тега <title>.


import re
import os

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def getfiles(direc):
    return os.listdir(direc)

def formatting(text):
    return re.sub(r'([\w)]),(\w)', r'\1, \2', re.sub(r'(\w)(\() ?(\w)', r'\1 \2\3', re.sub(r'(\w)"(\w)', r'\1 "\2', text)))

def main():
    os.makedirs('исходные тексты', exist_ok=True)
    for file in getfiles('news'):
        text = fread('news\{}'.format(file))
        with open('исходные тексты\{}'.format(file.replace('html', 'txt')), 'w', encoding='cp1251') as f:
            header = re.findall(r'<title>(.*?)</title>', text)
            f.write('{}\n'.format(header[0]))
            text = re.sub(r'\n', ' ', re.sub(r'`', '', re.sub(r'<.*?>', '', re.sub(r'> (.+?)\n?<', r'>\1<', re.sub(r'<title>.*?</title>', '', text)))))
            f.write(formatting(text))


if __name__ == '__main__':
    main()
