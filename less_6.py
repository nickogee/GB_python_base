'''
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, т
ретьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

import time
from itertools import cycle


# Определим список кортежей, в которых первыми элементами будут режимы светофора,
# а вторыми - продолжительности режимов в сек.
MODES = [
    ('Красный', 7),
    ('Желтый', 2),
    ('зеленый', 5),
]


class TrafficLight:
    __color = ''

    def run(self, duration):
        '''
        Запускает цикл работы светофора на время duration (сек)
        :param duration:
        :return:
        '''

        # Переменная накапливает время работы светофора
        run_time = 0

        # итератор, повторяющий элементы некоторого списка
        for mode, long in cycle(MODES):
            self.__color = mode

            # В каждый проход цикла будем проверять текущую наработку по времени светофора
            if run_time < duration:
                print(f'Зажегся {self.__color} свет')
            else:
                print('Светофор выключен')
                return

            # задает время действия текущего состояния
            time.sleep(long)

            run_time += long


tr_1 = TrafficLight()

# Протестируем работу светофора в заданном промежутке времени
tr_1.run(20)

'''
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
'''


class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, mass_m2, width):
        '''
        Расчитывает массу асфальта для покрытия дороги, заданной ширины и длины
        необходимы плотность асфальта mass_m2 и толщина слоя width
        :param mass_m2: -> float
        :param width: -> float
        :return:
        '''
        return self.__width * self.__length * mass_m2 * width


# создадим экземпляр класса Road
rd_1 = Road(2000, 5)

# получим результат расчета расхода асфальта дя этой дороги
print(rd_1.calculate(2, 10))

'''
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus};

создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: 
создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'


    def get_total_income(self):
        return f'Доход сотрудника {self._income["wage"] + self._income["bonus"]}'


# Создадим экземпляры класса Position и проверим работу методов
p1 = Position('Иван', 'Петров', 'академик', 200000, 50000)
p2 = Position('Влад', 'Винокуров', 'асистент', 100000, 10000)
p3 = Position('Игорь', 'Сафонов', 'лаборант', 150000, 20000)

print(p1.get_full_name())
print(p1.get_total_income())
print(p1._income)

print(p2.get_full_name())
print(p2.get_total_income())
print(p2._income)

print(p3.get_full_name())
print(p3.get_total_income())
print(p3._income)

'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
'''

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, color, name, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police

        # Добавим свойство, в котором будем хранить строковое представление признака is_police
        # и будем его применять сразу в сообщениях
        self.str_police = "полицейская " if self.is_police else ''


    def go(self, speed):
        # Пусть у нас целевая скорость будет задаваться при старте
        self.speed = speed
        print(f'{self.str_police}{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.str_police}{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.str_police}{self.color} {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Текущаая скорость у {self.str_police}{self.color} {self.name} - {self.speed} км/ч')


class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):

        if self.speed > 60:
            print(f'Внимание! Текущаая скорость автомобтля - {self.speed} км/ч при разрешенной - 60 км/ч')
        else:
            print(f'Текущаая скорость автомобтля - {self.speed} км/ч')


class SportCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name)


class WorkCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):

        if self.speed > 40:
            print(f'Внимание! Текущаая скорость автомобтля - {self.speed} км/ч при разрешенной - 40 км/ч')
        else:
            print(f'Текущаая скорость автомобтля - {self.speed} км/ч')


class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, True)


# Создадим по экземпляру каждого класса автомобиля
town_1 = TownCar('Серебристый', 'Toyoto')
sport_1 = SportCar('Синий', 'Subaru')
work_1 = WorkCar('Черный', 'VW')
police_1 = PoliceCar('Бело-Синий', 'Land Cruiser')


# Протестируем методы и свойства объектов
town_1.go(70)
town_1.turn('Право')
town_1.show_speed()
town_1.stop()
print('-------------')

sport_1.go(170)
sport_1.turn('Право')
sport_1.show_speed()
sport_1.stop()
print('-------------')

work_1.go(45)
work_1.turn('Лево')
work_1.show_speed()
work_1.stop()
print('-------------')

police_1.go(65)
police_1.turn('Лево')
police_1.show_speed()
police_1.stop()

'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка инструментом {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} отрисовывает фигуру')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'С помощю {self.title} выделим область')


# Создадим по экземпляру каждого класса канцтовара

pen_1 = Pen('Шариковая ручка')
pencil_1 = Pencil('Карандаш полутвердый')
handle_1 = Handle('Маркер')

# Протестируем методы
pen_1.draw()
pencil_1.draw()
handle_1.draw()