import random

def instructions():
    return '\nДанная программа предлагает вам угадать слово по подсказке. Вам будет предложено частотное словосочетание, где загаданное слово заменено многоточием. Число точек равно числу букв в слове. Вы можете попросить дополнительную подсказку.\nУдачи!\n\n'

def readfile(fname):
    with open(fname, encoding='utf-8') as f:
        return f.readlines()

def dictionary(lines):
    d = {}
    for line in lines:
        line = line.split(',')
        d[line[0]] = line[1].split()
    return d

def make_hint(d):
    word = random.choice(list(d.keys()))
    hint = random.choice(d[word]) + ' '
    for s in word:
        hint += '.'
    return hint

def win():
    print('''Вы угадали!''')
    choice = input('''Введите 'да', если хотите сыграть ещё раз.\n''')
    return(choice)

def game():
    d = dictionary(readfile('words.csv'))
    word = random.choice(list(d.keys()))
    hint1 = random.choice(d[word])
    hint = hint1 + ' '
    for i in range(len(word)):
        hint += '.'
    print('\n' + hint)
    guess = input('Вы думаете, что загадано слово: ')
    if word == guess:
        return win()
    else:
        guess = input('''Это неверно. Попробуйте ещё раз.\nЕсли вам нужна другая подсказка, введите 'подсказка'.\n''')
        while guess != 'подсказка' and guess != word:
            guess = input('''Это неверно. Попробуйте ещё раз.\nЕсли вам нужна другая подсказка, введите 'подсказка'.\n''')
        if guess == word:
            return win()
        elif guess == 'подсказка':
            hint2 = random.choice(d[word])
            while hint2 == hint1:
                hint2 = random.choice(d[word])
            hint = hint2 + ' '
            for i in range(len(word)):
                hint += '.'
            print('\n' + hint)
            guess = input('Вы думаете, что загадано слово: ')
            if word == guess:
                return win()
            else:
                guess = input('''Вы снова не угадали. У вас есть возможность попросить последнюю подсказку. Если хотите ей воспользоваться, введите 'подсказка'.\n''')
                while guess != 'подсказка' and guess != word:
                    guess = input('''Вы снова не угадали. У вас есть возможность попросить последнюю подсказку. Если хотите ей воспользоваться, введите 'подсказка'.\n''')
                if guess == word:
                    return win()
                elif guess == 'подсказка':
                    hint3 = random.choice(d[word])
                while hint3 == hint1 or hint3 == hint2:
                    hint3 = random.choice(d[word])
                hint = hint3 + ' '
                for i in range(len(word)):
                    hint += '.'
                print('\n' + hint)
                guess = input('Введите свой вариант.\n')
                if word == guess:
                    return win()
                else:
                    guess = input('''Это неверно. Попробуйте ещё раз. Если хотите сдаться, введите 'сдаюсь'.\n''')
                    while guess != 'сдаюсь' and guess != word:
                        guess = input('''Это неверно. Попробуйте ещё раз. Если хотите сдаться, введите 'сдаюсь'.\n''')
                    if guess == word:
                        return win()
                    if guess == 'сдаюсь':
                        choice = input('Загаданное слово: ' + word + '''\nВведите 'да', если хотите сыграть ещё раз.\n''')
                        return choice

def start():
    choice = input('''Чтобы играть, введите 'играть'.\nЧтобы вызвать инструкцию, введите 'инфо'.\nЧтобы закрыть программу, введите 'закрыть'.\n''')
    while choice != 'закрыть':
        if choice == 'инфо':
            print(instructions())
        elif choice == 'играть':
            while game() == 'да':
                continue
            else:
                break
        else:
            print('\nТакой команды не существует.\n')
        choice = input('''Чтобы играть, введите 'играть'.\nЧтобы вызвать инструкцию, введите 'инфо'.\nЧтобы закрыть программу, введите 'закрыть'.\n''')
        continue

start()
