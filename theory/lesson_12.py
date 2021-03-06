print('Оператор IF\n')

# print(2 != 3)

'''
if выражение 1:    # если выражение 1 == True, то выполнится блок кода 1
    блок кода 1
elif выражение 2:  # если выражение 1 == False, a выражение 2 == True, то выполнится блок кода 2
    блок кода 2
else:              # если выражение 1 и 2 == False, то выполнится блок кода 3
    блок кода 3

Однострочная форма
Для простых случаев может быть полезна однострочная форма инструкции:

my_var = 'one' if x == 1 else 'other'
# my_var укажет на `one` если x равно 1, иначе на `other`
'''
s = 'Hello world'
if ' ' in s:  # МОЖНО ДОБАВЛЯТЬ ИНСТРУКЦИЮ in
    print(s.upper())
else:
    print(s.lower())

'''
Объекты, которые приравниваются к False:

Последовательности и коллекции
пустая строка «»; пустой список []; пустой кортеж (); пустой словарь {}; пустое множество set(); пустой диапазон range(0).

Нули любых численных типов
целочисленный ноль: 0; ноль с плавающей точкой: 0.0; комплексный ноль: 0j.

Константы
None; False.
'''

x = 0
if x:
    print('Пуременная х вернула истинно')
    print('Выполнится блок кода 1')
else:
    print('Переменная х вернула ложно')
    print('Выполнится блок кода 2\n')

# if 1:
#     print('Пуременная х вернула Истину')
#     print('Выполнится блок кода 1')
# else:
#     print('Переменная х вернула Ложь')

light = 'green'
if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print('Go\n')
else:
    print("What?")
#
# age = int(input('сколько вам лет? '))
# # Запросим у пользователя ввести число (функция input) и приведем его к числовому типу (функция int)
#
# if age >= 18:
#     print('Добро пожаловать!')
# else:
#     print(f'вам {age} лет, а вход разрешен с 18, приходите через {18 - age} года')

time = 11
if time < 12 or time > 13:  # Если время меньше 12 или время больше 13 - то возвращает True
    print('Welcome\n')
else:
    print('close')

time = 9
day = 'st'
if time >= 8 and day != 'su':  # Если время больше 8 и день != воскресенье - то возвращает True
    print('Open\n')
else:
    print('Close')

'''
Если необходимо сделать что бы условие выполнялось при False то применяем инверсию условия (оператор not):
'''
x = 0
if not x:
    print('OK')
else:
    print("NO")

# Сокращенное выражение:
x = 1
res = 'OK' if x else 'NO'  # в переменную res присвоить OK если х вернет True, в противном случае - NO
print(res)

x = 0
# можно не присваивать значение в переменную а просто писать:
print('OK' if x else 'NO')
