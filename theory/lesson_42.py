print('Декораторы\n')

"""
    Функции можно присваивать переменным:
test = hello  - присвоили переменной test функцию hello !!!пишем без (), иначе функция вызовется и отработает!!!

    теперь переменная test являлется обьектом и можно её вызвать:
print(test())  - вызываем функцию test() = Hello, I am func "hello"
"""

"""
    Так как Функция это ОБЬЕКТ - её можно перредавать параметром в другие функции.
    
    Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности 
без непосредственного изменения её кода. 
"""


def hello():
    """
    Декорируемая функция
    """
    return 'Hello, I am func "hello"\n'


def super_func(func):  # func аргумент - пишем без ()!!!!
    """
    Декоратор функция
    """
    print('Hello, I am func "super_func"')
    print(func())  # вызываем функцию func() - пишем ()!!!!


'''Передаем функцию hello в качестве аргумента функции super_func, hello - это аргумент, по этом пишем ео без (). 
Иначе функция hello будет вызываться.'''
super_func(hello)  # Hello, I am func "super_func"  +  Hello, I am func "hello"

'''
Конструкция(идея) функции декоратора:

def my_decorator(func):  # функция декоратор
    def func_wrapper():  # функция обертка
        print('Code before')
        func()
        print('Code after\n')

    return func_wrapper  # вернем функцию func_wrapper без выполнения кода функции func_wrapper

def func_test():
    print('Hello, I am func "func_test"')

# поместим в переменную test декорирующую функцию my_decorator
test = my_decorator(func_test)
test()  # Code before  + Hello, I am func "func_test"  + Code after
    Таким образом мы обработали код из функции func_test в функции декораторе my_decorator


test = my_decorator(func_test)  ___ данную конструкцию ЖЕЛАТЕЛЬНО заменить на декоратор @my_decorator : 
test()_________________________/
    Просто указываем "@имя_декоратора" перед функией которую надо декорировать. И потом вызываем эту функцию
'''


def my_decorator(func):  # функция декоратор
    def func_wrapper():  # функция обертка
        print('Code before')
        func()
        print('Code after\n')

    return func_wrapper  # вернем функцию func_wrapper без выполнения кода функции func_wrapper


@my_decorator
def func_test():
    print('Hello, I am func "func_test"')


func_test()  # Code before  +  Hello, I am func "func_test"  +  Code after

''' Создаем более полезный декоратор, приводящий первый символ строки в верхний регистр и удаляет запятые:'''


def make_title(fn):
    def wrapper():
        title = fn()  # функция fn() вернет строку и записывам её в переменную
        title = title.capitalize()  # Делаем первую букву заглавной
        title = title.replace(',', '-')  # заменяем запятые пустой строкой
        return title

    return wrapper


@make_title
def hi():
    return 'hello,,,, world'


print(hi())  # Hello---- world
