'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

# class Data:
#
#     def __init__(self, raw_data):
#         # здесь будем храниить принятую строку, в "сыром" виде, без валидации
#         self.raw_data = raw_data
#
#     @classmethod
#     def extract_data_part(cls, raw_data):
#         '''
#         метод извлекает части даты, преобразует их в int и возвращает их в виде кортежа (день, месяц, год)
#         :param raw_data: -> str
#         :return: -> tuple
#         '''
#
#         # получим кортеж с частями даты
#         data_tpl = tuple([int(raw_data[:2]), int(raw_data[3:5]), int(raw_data[6:])])
#
#         # так как у нас есть ссылка на класс, со статическим методом, в котором определен метод для валидации частей даты,
#         # то сразу проверим эти части даты на корректность значений
#         success = cls.check_data_parts(data_tpl)
#
#         if not success:
#             print('Введены не корректные значения даты')
#
#         return tuple(data_tpl)
#
#     @staticmethod
#     def check_data_parts(data_tpl):
#         '''
#         метод проводит валидацию принятых частей даты, если все части даты корретны, возвращает True
#         :param data_tpl: -> tuple
#         :return: -> bool
#         '''
#
#         day, month, yaer = data_tpl
#
#         # проверим месяц
#         month_correct = (0 < month < 13)
#
#         # проверим день
#         last_day = 0
#         if month_correct:
#             if month in [1, 3, 5, 7, 8, 10, 12]:
#                 last_day = 31
#             elif month == 2:
#                 last_day = 28
#             else:
#                 last_day = 30
#
#         day_correct = (0 < day < last_day + 1)
#
#         # проверим год
#         year_correct = (yaer > 0)
#
#         return day_correct and month_correct and year_correct
#
#
# # значения для проверки
# d1 = Data('26-08-2022')
# print(Data.extract_data_part(d1.raw_data))
#
# d2 = Data('26-15-2022')
# print(Data.extract_data_part(d2.raw_data))

'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

#
# class MyZeroDiv(Exception):
#     def __init__(self, txt_err):
#         self.txt = txt_err
#
#
# # Зададим делимое
# dividend = 100
#
# # будем запрашивать делитель, пока не получим корректный
# currect = False
# while not currect:
#
#     # делитель получим у пользователя
#     divisor = int(input("Введите число-делитель\n"))
#
#     # обработаем исключение деления на "0"
#     try:
#         if divisor == 0:
#             raise MyZeroDiv('Ошибка деления на ноль')
#
#     except MyZeroDiv as err:
#         print(err)
#
#     else:
#         currect = True
#         print(f'{dividend}/{divisor}={dividend/divisor}')

'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
'''

# # создадим класс, обрабатывающий ошибку ввода неверного типа
# class NotDigitErr(Exception):
#     def __init__(self, txt_err):
#         self.txt = txt_err
#
# # Зададим константу, содержащую команду остановки ввода элементов
# STOP = 'stop'
#
# # переменная будет содержать текущие значения, вводимые пользователем
# next_el = ''
#
# # список чисел, заполняемый пользователем
# user_num_list = []
#
# # будем запрашивать данные, пока пользователь не введет команду остановки ввода
# while True:
#
#     next_el = input(f"Введите число для заполнения списка или {STOP}\n")
#
#     # если введена команда остановки - сразу прекращаем добавление элементов в список
#     if next_el.lower() == STOP:
#         break
#
#     try:
#         # при попытке ввода "не числа" активизируем исключение
#         if not next_el.isdigit():
#             raise NotDigitErr('Введено не числовое значение')
#
#     # отловим исключение
#     except NotDigitErr as err:
#         print(err)
#
#     else:
#         user_num_list.append(int(next_el))
#
#
# print(f'Введен список:\n{user_num_list}')

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
'''

'''
5. Продолжить работу над первым заданием. 
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру (например, словарь).
'''


class Warehouse:
    # хранит последний идентификационный номер товара на складх (сквозная нумерация по всем складам)
    id = 0

    def __init__(self, name):
        self.name = name

        # структура хранения остатков на складе
        self.stock = {}


    # метод будет обновлять последний присвоенный id на всех действующих складах и возвращать его
    @staticmethod
    def _get_id():
        '''
        возвращает следующий идентификационный номер
        :return: int
        '''
        Warehouse.id += 1
        return Warehouse.id

    # метод для оприходования техники на склад
    def posting(self, eqpt):
        # при оприходовании товара присваевается очередной идентификационный номер, этот номер присваивается товару
        # и товар добавляется в структуру хранимых на складе остатков

        curr_id = Warehouse._get_id()
        eqpt.inv_number = curr_id
        self.stock[curr_id] = eqpt


    def to_division(self, eqpt_id, division_name):

        try:
            find_eqpt = self.stock.pop(eqpt_id)
            print(f'{find_eqpt} передан в подразделение {division_name}')

        except KeyError:
            print(f'Товара под номером {eqpt_id} на складе {self.name} не числится')


    # метод показывает информацию об остатках на складе
    def get_info(self):
        st = f'На складе {self.name} в наличии:\n'
        for id, name in self.stock.items():
            st += f'{name}, (инв.№ {id})\n'
        return st


class Equipment():
    # характеристики, общие для класса "оргтехника"
    def __init__(self, model, manufacturer, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

        # идентификационный номер будет присваиваться при оприходовании на склад
        self.inv_number = None

    # определим строковое представление для товара,
    # но каждый дочерний класс переопределит и дополнит его
    def __str__(self):
        return f'{self.manufacturer}, {self.model}'


class Printer(Equipment):
    def __init__(self, model, manufacturer, price, print_type):
        super().__init__(model, manufacturer, price)
        self.print_type = print_type

    def __str__(self):
        return f'Принтер {super(Printer, self).__str__()}'


class Scaner(Equipment):
    def __init__(self, model, manufacturer, price, max_resol):
        super().__init__(model, manufacturer, price)
        self.max_resol = max_resol

    def __str__(self):
        return f'Сканер {super(Scaner, self).__str__()}'


class Copyr(Equipment):
    def __init__(self, model, manufacturer, price, two_size):
        super().__init__(model, manufacturer, price)
        self.two_size = two_size

    def __str__(self):
        return f'Копир {super(Copyr, self).__str__()}'


# создадим склад
wh_1 = Warehouse('Центральный')

# создадим несолько наименований товаров для хранения на складе
cop_1 = Copyr(model='LJ 2010', manufacturer='HP', price=1200, two_size=False)
cop_2 = Copyr(model='RG-2300-1', manufacturer='Xerox', price=34590, two_size=True)

pr_1 = Printer(model='G-124', manufacturer='Toshiba', price=47346, print_type='laser')
pr_2 = Printer(model='F-0045', manufacturer='Toshiba', price=7764, print_type='matrix')

scan_1 = Scaner(model='df9087', manufacturer='Cannon', price=4352, max_resol="1490x1860")
scan_2 = Scaner(model='DD90', manufacturer='Samsung', price=9234, max_resol="2500x4890")

# примем все на склад
wh_1.posting(cop_1)
wh_1.posting(pr_1)
wh_1.posting(scan_1)

wh_1.posting(cop_2)
wh_1.posting(pr_2)
wh_1.posting(scan_2)

# Посмотрим наличие на складе
print(wh_1.get_info())

# передадим один принтер и два сканера в подразделение
wh_1.to_division(pr_1.inv_number, 'Администрация')
wh_1.to_division(scan_1.inv_number, 'Администрация')
wh_1.to_division(scan_2.inv_number, 'Администрация')

# попытаемся передать в подразделение несуществующий id
wh_1.to_division(888, 'Администрация')

# Посмотрим наличие на складе после передачи в подразделение
print(wh_1.get_info())


