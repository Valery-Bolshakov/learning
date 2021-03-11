print('Homework\n')

"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли 
в списке число, которое равно индексу элемента "odd". Напишите функцию, которая будет 
возвращать True или False, соответсвенно.
"""
my_list_1 = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]
my_list_2 = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]
my_list_3 = ["even", 10, "odd", 2, "even"]


# print(my_list_1.index('odd'))  # индекс элемента равен 10 <class 'int'>
def odd_ball(arr):  # на вход принимает некий список(arr)
    j = False  # устанавливаем флаг на false
    if 'odd' in arr:  # проверяем наличие нужного элемента в последовательности
        i = 0
        while i < len(arr):  # len(arr) вернет колличество элементов списка
            if arr[i] == arr.index('odd'):  # сравниваем каждый элемент с индексом 10
                j = True  # если условие выполнится меняем на true и возвращаем его
                break  # останавливаем выполнение цикла если условие выполнилось
            i += 1
        return j


print(f'my_list_1 = {odd_ball(my_list_1)}')  # True
print(f'my_list_2 = {odd_ball(my_list_2)}')  # False
print(f'my_list_3 = {odd_ball(my_list_3)}\n')  # True

'''КАК СДЕЛАТЬ ПРОЩЕ:'''


def get_odd(arr):
    """
    Функция принимает параметром какой то список.

    Затем конструкция 'arr.index('odd')' выдает индекс указанного элемента (если он имеется в списке). Далее
    получаем '10 in arr', где конструкция 'in arr' проверяет есть ли элемент 10 в arr => вернёт True or False
    """
    return arr.index('odd') in arr


print(get_odd(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))
print(get_odd(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))
print(get_odd(["even", 10, "odd", 2, "even"]), '\n')

"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности 
включительно. Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте 
решить задачу двумя способами (один из способов в одну строчку кода).
"""


def find_sum(n):
    return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)


print(find_sum(5))  # 8  (3 + 5)
print(find_sum(10))  # 33  (3 + 5 + 6 + 9 + 10)
print(find_sum(9), '\n')  # 23  (3 + 5 + 6 + 9)

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
new_names = []


def get_names(names):
    for elem in names:
        s = list(elem)
        if len(s) == 4:
            new_names.append(elem)
    return new_names


print(get_names(names))

'''КАК СДЕЛАТЬ ПРОЩЕ:'''


def get_names1(arr):
    return [i for i in arr if len(i) == 4]


print(get_names1(names))
