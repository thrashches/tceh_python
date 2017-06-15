from random import randint
print('''
Игра "Виселица".
Тема игры: Методы списков в Python.
''')
words = {
    'append':'Добавляет элемент в конец списка',
    'extend':'Расширяет список list, добавляя в конец все элементы списка L',
    'insert':'Вставляет на i-ый элемент значение x',
    'remove':'Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует',
    'pop':'	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент',
    'index':'Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)',
    'count':'Возвращает количество элементов со значением x',
    'sort':'Сортирует список на основе функции',
    'reverse':'Разворачивает список',
    'copy':'Поверхностная копия списка',
    'clear':'Очищает список'
}
print('{} вопросов в базе.'.format(len(words)))

def play():
    q_num = randint(0, len(words)-1)
    def get_q(num):
        i = 0
        for key, value in words.items():
            if i == num:
                return (key, value)
            else:
                i += 1
    print('''
    Вопрос №{}:
    Назовите метод, который: {}
    '''.format(q_num, get_q(q_num)[1]))
    #print(get_q(q_num))
    i = 0
    while  i < 10:
        if i != 9 and input('Ваш ответ: ') == get_q(q_num)[0]:
            print('Вы выиграмли!')
            break
        elif i == 9 and input('Ваш ответ: ') != get_q(q_num)[0]:
            print('Вас повесили!')
            break
        else:
            i += 1
            print('Неверно! Осталось {} попыток!'.format(10 - i))

play()