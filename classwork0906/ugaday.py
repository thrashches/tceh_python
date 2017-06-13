from random import randint
print('Угадай число от 1 до 10!')
score = 0
def play(i):
    rnd = randint(1, 10)
    if i == 'stop':
        quit()
    elif int(i) == rnd:
        print('Красава! Угадал!')
        return 1
    else:
        print('Неа, правильное число {}'.format(rnd))
        return 0
while True:
    try:
        if play(input('Введите число: ')):
            score += 1
        else:
            score -= 1
        print('Score = {}'.format(score))
    except ValueError:
        print('Вводите только целые числа от 1 до 10!')

