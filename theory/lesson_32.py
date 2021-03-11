import os

print('HomeWork\n')

'''homeWork рассмотреть модуль os and os.path
создать папку с папками и файлами. написать скрипт выводящий дерево файлов
walk - метод который позволяет получить дерево файлов'''

p = os.path.abspath('folder ')  # вернет абсолютный путь к файлу/директории
# print(p)  # C:\Python\learning\theory\folder

'''Воспользовавшись методом walk, можно получить доступ к названиям и путям всех подпапок и файлов, 
относящихся к заданному каталогу. Применив один внешний цикл for, а также два вложенных, 
несложно получить информацию об объектах в каталоге folder через специальные списки directories и files.'''

i = 0
# tree = os.walk('folder')  # Относительный путь. Можно задать т.к. папка лежит в корневой директории
tree = os.walk(r"C:\Python\learning\theory\folder")  # абсолютный путь

# Распаковываем кортеж, присвоив имена переменных каждому элементу:
for root, directories, files in tree:  # из tree получают кортеж
    if i == 0:
        i = 1
        print(f'\nНахоидмся в директории: {root} \nПапка содержит следующее:')  # путь до текущей директории
    else:
        print(f'\nПереходим в директорию: {root} \nПапка содержит следующее:')
    for file in files:
        print(file)
    for directory in directories:
        print(directory)

print('\n')
tree = os.walk('folder')  # Относительный путь. Можно задать т.к. папка лежит в корневой директории
for files in tree:
    print(files)

# ('folder', ['subFolder'], ['test_1.py', 'test_2.py'])
# ('folder\\subFolder', ['subSubFolder'], ['test_3.py', 'test_4.py'])
# ('folder\\subFolder\\subSubFolder', [], ['test_5.py', 'test_6.py'])
'''
Функция walk() модуля os принимает один обязательный аргумент - имя каталога.

Возвращает объект-генератор, из которого получают кортежи для каждого каталога переданной файловой иерархии.

Каждый кортеж состоит из трех элементов: - ('folder', ['subFolder'], ['test_1.py', 'test_2.py'])

1. Адрес очередного каталога в виде строки.       - 'folder'
2. В форме списка - имена подкаталогов первого    - ['subFolder']
   уровня вложенности для данного каталога.
3. В виде списка - имена файлов данного каталога. - ['test_1.py', 'test_2.py']
'''
print('\n')


def read_dir(folder):
    # Распаковываем кортеж, присвоив имена переменных каждому элементу:
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, files)
        # Сделаем вывод в виде дерева (С отступами):
        # Отступы ставим по колличеству слешей в пути. их считаем и пользуем метод sep для корректного отображения
        level = root.count(os.sep)
        indent = ' ' * 4 * level  # Переменная для отступа ДЛЯ ПАПОК
        file_indent = ' ' * 4 * (level + 1)  # Переменная для отступа ДЛЯ ФАЙЛОВ
        # print(root, files, level)
        # print(indent, root, files)  # пока что все работает
        # Выводим Дерево Файлов:
        print(f'{indent}[{os.path.basename(root)}]')
        '''Метод os.path.basename(root) - выдаст базовое имя от относительного пути folder\\subFolder -> subFolder'''
        for file in files:
            print(f'{file_indent}{file}')


read_dir('folder')

# [folder]
#     test_1.py
#     test_2.py
#     [subFolder]
#         test_3.py
#         test_4.py
#         [subSubFolder]
#             test_5.py
#             test_6.py
