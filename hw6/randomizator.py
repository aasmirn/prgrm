import random

def choose_word(filename):
    with open(filename, encoding='utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words += [line]
        return random.choice(words)

def adv():
    return choose_word('texts/adv.txt')

def agn():
    return choose_word('texts/agn.txt')

def ind1():
    return choose_word('texts/ind1.txt')

def pref():
    return 'за'+ind1()

def inf2():
    return choose_word('texts/inf2.txt')

def ind2():
    verb = inf2()
    if verb.endswith('сть'):
            verb = verb[:-3]+'л'
    elif verb.endswith('ть'):
            verb = verb[:-2]+'л'
    return verb
    
def loc():
    return choose_word('texts/loc.txt')

def modal():
    return choose_word('texts/modal.txt')

def move():
    return choose_word('texts/move.txt')

def obj1():
    return choose_word('texts/obj1.txt')

def obj2():
    return choose_word('texts/obj2.txt')

def prtc():
    return choose_word('texts/prtc.txt')

def qual():
    return choose_word('texts/qual.txt')

def verb():
    return choose_word('texts/verb.txt')

def capitalization(sentence):
    return sentence[0].upper() + sentence[1:]

def oddline1():
    number = random.choice([1,2])
    if number == 1:
        sentence = agn() + ' ' + ind1() + ', ' + prtc() + ' ' + obj2() + ','
    else:
        sentence = ind1() + ' ' + agn() + ', ' + prtc() + ' ' + obj2() + ','   
    return capitalization(sentence)

def oddline2():
    number = random.choice([1,2])
    if number == 1:
        sentence = ind2() + ' ' + obj1() + ' ' + agn() + '-' + qual() + ','
    else:
        sentence = obj1() + ' ' + ind2() + ' ' + agn() + '-' + qual() + ','
    return capitalization(sentence)

def oddline():
    number = random.choice([1,2])
    if number == 1:
        return oddline1()
    else:
        return oddline2()

def evenline1():
    number = random.choice([1,2])
    if number == 1:
        sentence = ind2() + ' ' + obj1() + ' и ' + pref() + '.' 
    else:
        sentence = obj1() + ' ' + ind2() + ' и ' + pref() + '.'
    return capitalization(sentence)
       
def evenline2():
    number = random.choice([1,2])
    if number == 1:
        sentence = move() + ' ' + loc() + ' и там ' + verb() + '.'
    else:
        sentence = loc() + ' ' + move() + ' и там ' + verb() + '.' 
    return capitalization(sentence)

def evenline3():
    number = random.choice([1,2,3])
    if number == 1:
        sentence = adv() + ' ' + modal() + ' ' + inf2() + ' ' + obj1() + '.'
    elif number == 2:
        sentence = adv() + ' ' + modal() + ' ' + obj1() + ' ' + inf2() + '.'
    else:
        sentence = adv() + ' ' + obj1() + ' ' + modal() + ' ' + inf2() + '.'
    return capitalization(sentence)

def evenline():
    number = random.choice([1,2,3])
    if number == 1:
        return evenline1()
    elif number == 2:
        return evenline2()
    else:
        return evenline3()


for i in range(2):
    print(oddline()+'\n'+ evenline())

