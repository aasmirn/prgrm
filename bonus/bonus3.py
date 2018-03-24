def change_word(word):
    vowels = 'aeiouy'
    index = 0
    for letter in word:
        if letter not in vowels:
            index +=1
        if letter in vowels:
            break
    return word[index:] + word[:index] + 'ay'

def remove(phrase):
    symbols_to_remove = '.,!"()/?'
    for s in symbols_to_remove:
        if s in phrase:
            phrase = phrase.replace(s, '')
    return(phrase)

def check(phrase):
    latin = "abcdefghijklmnopqrstuvwxyz' "
    check = ''
    for sym in phrase:
        if sym not in latin:
            check += 'not good'
            break
    return check
            

phrase = input('Write your English phrase: ').lower()
if phrase == '':
    print('Try to write something less empty.')
else:
    phrase = remove(phrase)
    if check(phrase) == 'not good':
        print("That's not the way English works!")
    else:
        words = phrase.split(' ')
        pl_phrase = ''
        for word in words:
            pl_phrase += change_word(word) + ' '
        print('This is Pig Latin for you: ', pl_phrase.capitalize())


