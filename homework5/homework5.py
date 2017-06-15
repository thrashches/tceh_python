### 1
class Person:

    def __init__(self, age, name):
        self.name = name
        self.age = age
        print('New person {}. {} years old.'.format(self.name, self.age))
        self.known_persons = []

    def know(self, person):
        self.known_persons.append(person)
        print('Now {} knows {}.'.format(self.name, person.name))

    def is_known(self, person):
        try:
            self.known_persons.index(person)
            print('{} knows {}.'.format(self.name, person.name))
        except ValueError:
            print('{} dont knows {}.'.format(self.name, person.name))


p1 = Person(50, 'Alex')
p2 = Person(31, 'Vasya')

p1.is_known(p2)
p1.know(p2)
p1.is_known(p2)


### 2
class Printer(object):
    def __init__(self, *values):
        print('This is new Printer!')

        self.vals = []
        for v in values:
            self.vals.append(v)

    def log(self):
        for v in self.vals:
            print(v)


class FormattedPrinter(Printer):
    def log(self):
        for value in self.vals:
            print('*****************************\n{}\n*****************************\n'.format(value))


pr = Printer('qazwsxed', 883, 'asdsjJNBH', {1: 'val1', 2: 'val2'})
pr.log()
fp = FormattedPrinter('qazwsxed', 883, 'asdsjJNBH', {1: 'val1', 2: 'val2'})
fp.log()


### 3
class Human:
    name = str()

    def __init__(self, name):
        self.name = name
        print('{} is a new human!'.format(self.name))

    def is_dangerous(self, animal):
        if animal.dangerous:
            print('The {} is dangerous for human!'.format(animal.name))
        else:
            print('The {} is not dangerous for human!'.format(animal.name))


class Animal:
    name = str()
    dangerous = False

    def __init__(self, name, dangerous=False):
        self.name = name
        self.dangerous = dangerous
        print('{} is a new animal!'.format(self.name))


hum = Human('Vasiliy')
cat = Animal('Cat')
snake = Animal('Python', True)
hum.is_dangerous(snake)
hum.is_dangerous(cat)
