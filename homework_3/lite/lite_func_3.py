def func(flag = bool(), li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    if flag:
        print('Флаг True! Только нечетные.')
        for value in li:
            if value % 2 == 0:
                print('{} removed!'.format(value))
                li.remove(value)
        return li
    else:
        print('Флаг False! Только четные.')
        for value in li:
            print('{} removed!'.format(value))
            li.remove(value)
        return li
fl = int(input('Введите значение флага(1 или 0): '))
lst = list()
arg = ''
while arg != 'stop':
    arg = input('Вводите целые числа по очереди. Для завершения введите "stop": ')
    try:
        lst.append(int(arg))
    except ValueError:
        pass
print(func(fl, lst))
