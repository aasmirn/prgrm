def check(phrase):
    latin = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    check = ''
    for sym in phrase:
        if sym not in latin:
            check += 'not good'
            break
    return check

phrase = input('Введите вашу фразу на русском: ').lower()
if phrase == '':
    print('Если вы это видите, значит, ваша строка оказалась пустой. Попробуйте ещё раз.')
else:    
    if check(phrase) == 'not good':
        print('Пишите, пожалуйста, по-русски. И забудьте о знаках препинания.')
    else:
        vowels = 'аеёиоуыэюя'
        for vowel in vowels:
            phrase = phrase.replace(vowel, vowel + 'с' + vowel)
        print('Вот так ваша фраза выглядит на кирпичном:', phrase)
