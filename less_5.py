'''
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''


def write_str(str, f_obj):
    '''
    функция записывает строку string в переданный объект открытого файла
    :param string: -> (str)
    :param f_obj: -> (_io.TextIOWrapper)
    :return: None
    '''
    f_obj.write(str + '\n')     # будем добавлять перенос строки после каждого ввода

def ask_usr():
    '''
    функция опрашивает пользователя, ожидая ввод строки для записи в файл
    :return: (str) строка, введенная пользователем
    '''
    return input('Введите строку для записи в файл. Для окончания ввода - пусттая строка\n')


with open('my_files/task_1.txt', 'w') as f_obj:
    str_to_write = ask_usr()
    while str_to_write:
        write_str(str=str_to_write, f_obj=f_obj)
        str_to_write = ask_usr()
    else:
        print('Запись в файл окончена')

