def index(h, w):
    i = w / ((h/100)*(h/100))
    return i

def interpretation(i):
    if i < 16:
        return 'выраженный дефицит массы'
    elif i >= 16 and i < 18.5 :
        return 'недостаточная масса тела'
    elif i >= 18.5 and i < 25 :
        return 'норма'
    elif i >= 25 and i < 30 :
        return 'предожирение'
    elif i >= 30 and i < 35 :
        return 'ожирение первой степени'
    elif i >= 35 and i < 40 :
        return 'ожирение второй степени'
    else:
        return 'ожирение третьей степени'

h = float(input('Введите ваш рост в см: '))
w = float(input('Введите ваш вес в кг: '))
print('Интерпретация вашего ИМТ:', interpretation(index(h,w)))

