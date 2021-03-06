print('Форматирование строк\n')

name = 'John'
age = 30

print('My name is ' + name + '. I\'m ' + str(age))  # Для вывода призодитсяс постоянно разрывать строку. Это не удобно


print('''\n МЕТОД format (рекомендован к использованию вместо оператора %)''')
# позиционные аргументы
print('My name is {}. I\'m {}.'.format(name, age))  # в {} скобках проставляется неявная нумерация : 0, 1, 2 и т.д.
print('My name is {0}. I\'m {1}. Hi, {0}.'.format(name, age))  # нумерацию можно использовать много раз

# именные аргументы
print('My name is {x}. I\'m {y}.'.format(x=name, y=age))  # присваиваем маркерам x, y соответствующие переменные
print('My name is {name}. I\'m {age}. Hi, {asd}'.format(name=name, age=age, asd='Yong'))
# маркерам можно задавать толькочто созданные значение


print('''\n Оператор для форматирования f-strings (рекомендован для python 3.6 и выше)''')
print(f'My name is {name}. I\'m {age}. Hi {name}')  # ПРОСТО ставим перед '' букву f и ВСЕ ЗАЕБИСЬ РАБОТАЕТ!!!
# Дополнительное удобство данного метода - Можно проводить операции над переменными! Например:
print(f'My name is {name}. I\'m {age - 5}. Hi {name}')
print(f'5 + 2 = {5 + 2}')


print('''\n Оператор для форматирования строк - % (не рекомендуем к использованию)''')
# применим специальные именные маркеры для строки что бы избежать раззрывов:
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})
# %(name)s и %(age)d - маркеры для переменных. s - строка, d - значение(digit - цифра)
# %{'name': name, 'age': age} - задаем соответствия для введённых маркеров
# Удобство - после задания соответствий, один и тот же маркер можно использовать в строке много раз
print('My %(name)s name %(name)s is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})

# применим позиционные маркеры
print('My name is %s. I\'m %d. Hi, %s.' % (name, age, 'David'))
# позиционные маркеры можно определять непосредственно уже в строке
# Необходимо соблюдать четкое позиционирование маркеров

# Рассмотрим работу с float числами
print('Title: %s, Price: %f' % ('Sony', 40))  # Title: Sony, Price: 40.000000
# что бы избежать лишних нулей изменим %f -> %.2f Этим говорим что выводить 2 знака после запятой
print('Title: %s, Price: %.2f' % ('Sony', 40))
