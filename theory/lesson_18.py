print('Домашнее задание\n')

"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""
'''
Генераторы списков:
my_generator = (i [*2] for i in range(10) [if i != '5']) # операция с 'i' и условие [if] не обязательно
my_generator = [i*i for i in my_list [if i is not ' ']]

my_sum = sum(i*i for i in range(10))  # сумма квадратов 0, 1, 4, ... 81
'''
my_list = [1, 2, 3]
new_list = [i * 2 for i in my_list]
print(f'new_list = {new_list}')

my_list_new = []
for i in my_list:
    i *= 2
    my_list_new.append(i)
print(f'my_list_new = ', my_list_new, '\n')

"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""
my_list = [1, 2, 3]

my_sum = sum(i ** 2 for i in my_list)
print(my_sum)

j = 0
for i in my_list:
    j += i ** 2
print(j, '\n')

"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания 
и пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно вернуть количество литров, 
которые Игорь выпьет, с округлением до наименьшего значения.

time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""
time1 = 3
time2 = 6.7
time3 = 11.8

print(int(time1 * 0.5))
print(int(time2 * 0.5))
print(int(time3 * 0.5), '\n')

print(time1 // 2)
print(time2 // 2)
print(time3 // 2, '\n')

"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", 
тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
***************
"""

s = 'Hello world'

if s.find(' ') > 0:
    print(s.upper())
else:
    print(s.lower())

'''Можно сделать проще'''
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()
print(s)
