import os
import re

def check(dname):
    s = re.findall(r'[^а-яА-Я ]', dname)
    if s == []:
        check = True
    else:
        check = False
    return check

def choose(path):
    n = 0
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if check(d) == True:
                n += 1
    return n

def main():
    path = '.'
    print('Число папок с полностью кириллическими названиями:', choose(path))

if __name__ == '__main__':
    main()
