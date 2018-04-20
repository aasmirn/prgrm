import os
import re

path = os.path.dirname(__file__)
folder = os.listdir(path)
files = []
for item in folder:
    fpath = os.path.join(path, item)
    if os.path.isfile(fpath):
        files.append(item)
nonumbers = []
for name in files:
    if re.findall(r'\d', name) == []:
        nonumbers.append(name)

print('Файлов, не содержащих цифр в названии:', len(nonumbers))
for item in nonumbers:
    print(item)
        
