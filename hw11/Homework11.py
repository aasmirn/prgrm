import re

with open('wiki.html', encoding='utf-8') as f:
    text = f.read()

with open('new.html', 'w', encoding='utf-8') as f:
    f.write(re.sub(r'[VvWw][ií]kingr?', r'burunduk', re.sub(r'викинг', r'бурундук', re.sub(r'В[и́]{1,2}кинг', r'Бурундук', text))))

