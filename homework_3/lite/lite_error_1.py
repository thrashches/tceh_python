try:
    x = int(input('Введите число: '))
except:
    print('Введено неверное число!')
if x % 2 == 0:
    try:
        raise ValueError
    except ValueError:
        print('Число {} четное!'.format(x))
elif x < 0:
    try:
        raise TypeError
    except TypeError:
        print('Число {} < 0!'.format(x))
elif x > 10:
    try:
        raise IndexError
    except IndexError:
        print('Число {} > 10!'.format(x))
