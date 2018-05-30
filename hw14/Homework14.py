def askfile():
    return input('Введите имя файла, который нужно открыть: ')

def readfile(fname):
    with open(fname, encoding='utf-8') as f:
        text = f.read().replace('...', '.').replace('…', '.').split('.')
        sentences = []
        for sentence in text:
            sentences += sentence.split('?')
        text = []
        for sentence in sentences:
            text += sentence.split('!')
    return text

def cleantext(sentence):
    symbols = """.,!"()/?'—-:;«»\n"""
    for s in symbols:
         sentence = sentence.replace(s, ' ')
    return sentence

def search(sentence):
    if len(sentence.split()) > 10:
        words = [w for w in sentence.split() if w.istitle()]
    else:
        words = []
    return words

def main():
    file = askfile()
    try:
        if readfile(file) == ['']:
            print('Файл пустой.')
        else:
            n = 0
            for s in readfile(file):
                n += 1
                if len(cleantext(s).split()) > 10:
                    titles = search(cleantext(s))
                    if len(titles) == 1:
                        print('В предложении №{} слово с заглавной буквы: {}.'.format(n, titles[0]))
                    elif len(titles) > 1:
                        print('В предложении №{} слова с заглавной буквы: {}.'.format(n, ', '.join(titles)))
                    else:
                        print('В предложении №{} слов с заглавной буквы не найдено.'.format(n))
                else:
                    print('Предложение №{} короче десяти слов.'.format(n))
    except FileNotFoundError:
        print('Файл не найден.')

if __name__ == '__main__':
    main()
