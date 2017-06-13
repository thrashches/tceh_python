from random import randint
num = 0
li = list()
while num < randint(0, 1000):
    li.append(randint(0,1000000))
    num += 1
#li = [0, '2', 'str', 5.1]

i = int()
print('Введите "exit" или "выход" для выхода в любой момент.')
while True:
    index = input('Введите индекс элемента списка: ')
    if index == 'exit' or index == 'выход':
        quit()
    else:
        try:
            i = int(index)
            print(li[i])
        except ValueError:
            print('Индекс элемента может быть только целым числом!')
        except IndexError:
            print('Элемент с индексом {} не входит в данный список!'.format(i))
