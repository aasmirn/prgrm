# Найдите в текстах все биграммы вида «число (NUM) + существительное в
#родит. падеже (gen)». Создайте csv-таблицу (используйте в качестве
#разделителя «;» и кодировку «cp1251») со следующими полями: «doc_id»;
#найденная биграмма; «topic» (см. тег meta). Повторяющиеся биграммы убирать
#не надо.

import re
import os

def fread(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

def getfiles(direc):
    return os.listdir(direc)

def getbigrams(text):
    return re.findall(r'<w>.*?gr="NUM.*?ana>(.*?)</w>\W+<w>.*?gr="S,.*?,gen.*?"></ana>(.*?)</w>' ,text)

def findname(name, text):
    return re.findall(r'<meta content="(.*?)" name="{}">'.format(name), text)[0]
    

def main():
    with open('bigrams.csv', 'a', encoding='cp1251') as f:
        f.write('doc_id;bigram;topic\n')
    for file in getfiles('news'):
        text = fread('news\{}'.format(file))
        docid = findname('docid', text)
        topic = findname('topic', text)
        bigrams = getbigrams(text)
        if len(bigrams) > 0: 
            with open('bigrams.csv', 'a', encoding='cp1251') as f:
                for bi in bigrams:
                    f.write('{};{};{}\n'.format(docid, ' '.join(bi), topic))

if __name__ == '__main__':
    main()
