print('Введите слово в кириллице:')
word=input()
even=word[::2]
for letter in even:
    if letter=='о' or letter=='п' or letter=='е' or letter=='О' or letter=='П' or letter=='Е' :
        print(letter)
