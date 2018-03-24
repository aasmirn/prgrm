def check(phrase):
    latin = "abcdefghijklmnopqrstuvwxyz' "
    check = ''
    for sym in phrase:
        if sym not in latin:
            check += 'not good'
            break
    return check

phrase = input('Type your English phrase: ').lower()
if phrase == '':
    print('Try to write something, please!')
else:
    if check(phrase)== 'not good':
        print("I guess that's not English? If it is, just remove the punctuation marks.")
    else:
        consonants = 'ghjklmnpqrstvwxzbcdf'
        for consonant in consonants:
            phrase = phrase.replace(consonant, consonant + 'aig')
        print('Your Aigy Paigy:', phrase)
