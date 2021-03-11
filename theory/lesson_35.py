print('Ошибки и исключения\n')

"""
Виды ошибок:
    - Синтаксические.
    - Исключения.(Built-in Exceptions)

"""
# print(100 / 0)  # ZeroDivisionError - Вид ошибки. division by zero - говорит типа нельзя делить на нолъ

# print(1 + '2')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(int('test'))  # ValueError: invalid literal for int() with base 10: 'test'

'''
После вылета исключения - выполнение последующего кода Останавливается 
Для того что бы продолжить выполнение кода Даже если вылетает исключение - надо воспользоваться конструкцией
try - except
try:
    pass
except:
    pass
'''

try:
    num = 100 / 0
except ZeroDivisionError:
    num = 0
'''
Расщифровка - код, Попробуй выполнить действие в блоке try, если выпадает исключение, которое указанно в блоке except
то Выполни блок except.
'''
print(num, '\n')

'''Выполнится тот except исключение которого вылетит в результате выполнения блока try'''
try:
    num = 100 / 0
except ZeroDivisionError:
    num = 0
except TypeError:
    num = 1

'''Если не важно какое исключение вылетет - указываем Общее исключение:'''
try:
    num = 100 / 0
except Exception:  # При Любом исключении - выполнится этот блок
    num = 0

'''Полная конструкция try-except выглядит следующим образом:'''
try:
    num = 100 / 2
except Exception:  # При Любом исключении - выполнится этот блок
    num = 0
else:
    print('Else')  # Срабатывает когда Не вылетает исключение
finally:
    print('Finally')  # Срабатывает всегда
print(num, '\n')

'''Блок finally удобно использовать для закрытия файлов после их прочтения'''
# print('Hi!')

'''Просим пользователя ввести число для дальнейшей опериции деления.
Если он ввел ноль - выводим сообщение об ошибке, по типу исключения ZeroDivisionError
Если ввел строку - выводи сообщение об ошибке, по типу исключения ValueError
Если все ввел правильно выполняется блок try и выводится соответствующий принт И выходим из цикла
'''
while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('The number must be greater than zero')
    except ValueError:
        print('Must be a number')
