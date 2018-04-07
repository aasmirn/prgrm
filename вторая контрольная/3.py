import re

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def fwrite(text):
    with open('answer.txt', 'w', encoding='utf-8') as f:
        f.write(text[:-2])



def main():
    file = fread('mystem.xml')
    words = re.findall(r'<w>.*?gr="A.*?жен.*?/>(.*?)</w>', file)
    text = ''
    for word in words:
        text += word + ', '
    fwrite(text)
    text = re.findall(r'<body>([\s\S]*?)</body>', file)
    strings = re.findall(r'<w>.*?</w>', text[0])
    with open('another answer.txt', 'w', encoding='utf-8') as f:
        for string in strings:
            line = re.findall(r'lex="(.*?)"', string)[0] + ', ' + re.findall(r'gr="(.*?)"', string)[0] + ', ' + re.findall(r'/>(.*?)</w>', string)[0]
            f.write(line + '\n')    
    print('Ответы записаны в файлы answer.txt и another answer.txt')
    
if __name__ == '__main__':
    main()
