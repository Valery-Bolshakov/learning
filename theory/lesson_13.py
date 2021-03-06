print('Циклы For и While\n')

'''
Инструкция, позволяющая повторять цикл пока выполняется определённое условие.
do = True
while do:
    print('делаем')
    do = False
    print('делаем')
else:
    print('закончили')
    
# делаем
# делаем
# закончили

На каждом витке цикла условие, заданное при помощи выражения идущего после while, проверяется на истинность.
    Если выражение истинно, выполняется тело цикла(код после while);
    Если выражение ложно, то тело цикла [больше] не выполняется, но выполяется блок else, если он задан.
'''

# # While выполняет тело цикла пока условие == True:
# while True:
#     print('Hello')  # Безконечный цикл
#
# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1

'''
For - Инструкция, позволяющая производить проход(итерирование) по элементам объектов, поддерживающих итерирование.
Часть, идущая после in, будучи вычисленной единожды, должна предоставить объект, поддерживающий итерирование. 
Для данного объекта создаётся итератор. Далее переменной, предшествующей in, поочерёдно присваиваются 
значения [элементов], предоставляемые итератором и для каждого из них выполняется тело инструкции.

continue - Инструкция позволяет «проскочить» исполнение следующего после неё кода и продолжить 
проход по следующим элементам.

break - Инструкция позволяет прервать цикл. При этом часть после else не будет выполнена.

else - Всегда выполняется после цикла если не отрабатывает инструкция break
'''

s = 'Hello World'
for j in s:  # переменной j поочередно присваива.тся итерируемые значения из s и выполняется тело
    if j == ' ':  # если присваивается пробел то перескакиваем к следубщей итерации без выполнения тела цикла
        continue
    print(f'"{j}"', end=' ')
print('\n')

for i in 'Hello World':
    if i == ' ':
        break  # если во время итерации по строке попадается ' ' то цикл прерывается
    print(i, end=' ')
else:
    print('\nNo spaces')
print('\n')

# year = 1900
# while year <= 2020:
#     print(year, end=' ')
#     year += 1

'''
Вкладываем циклы друг в друга:
напишем наглядный порядок отработки основного и вложенных циклов
'''
for i in range(1, 3):
    print(f'Внешний цикл №{i}')
    for j in range(1, 3):
        print(f'\tВнутренний цикл №{j}')  # добавим символ отступа (\t) для наглядности
