'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Data:

    def __init__(self, raw_data):
        # здесь будем храниить принятую строку, в "сыром" виде, без валидации
        self.raw_data = raw_data

    @classmethod
    def extract_data_part(cls, raw_data):
        '''
        метод извлекает части даты, преобразует их в int и возвращает их в виде кортежа (день, месяц, год)
        :param raw_data: -> str
        :return: -> tuple
        '''

        # получим кортеж с частями даты
        data_tpl = tuple([int(raw_data[:2]), int(raw_data[3:5]), int(raw_data[6:])])

        # так как у нас есть ссылка на класс, со статическим методом, в котором определен метод для валидации частей даты,
        # то сразу проверим эти части даты на корректность значений
        success = cls.check_data_parts(data_tpl)

        if not success:
            print('Введены не корректные значения даты')

        return tuple(data_tpl)

    @staticmethod
    def check_data_parts(data_tpl):
        day, month, yaer = data_tpl

        # проверим месяц
        month_correct = (0 < month < 13)

        # проверим день
        last_day = 0
        if month_correct:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                last_day = 31
            elif month == 2:
                last_day = 28
            else:
                last_day = 30

        day_correct = (0 < day < last_day + 1)

        # проверим год
        year_correct = (yaer > 0)

        return day_correct and month_correct and year_correct


# значения для проверки
d1 = Data('26-08-2022')
print(Data.extract_data_part(d1.raw_data))

d2 = Data('26-15-2022')
print(Data.extract_data_part(d2.raw_data))
