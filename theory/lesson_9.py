print('Операции со строками\n')

# Как использовать сырые строки(строка в которой ничего не обрабатывается)
s = 'C:\d\new.txt'  # в данном примере путь укажется неверно, последовательность \n сделает перенос строки
print(s)

# что бы в строке ничего не обрабатывалось и она вывводилась так как есть надо поставить перед строкой символ 'r'
# 'r' - является управляющей конструкцией, она укажет питону что в строке не надо ничего обрабатывать

s = r'C:\d\new.txt'
print(s)

# Конкатенация строк:
s = 'Py' 'thon'  # 2 строки склеить крайне просто - просто пишем их через пробел
print(s)

s1 = 'Hello, '
s2 = 'World!'
s3 = s1 + s2  # при сложении переменных необходимо использовать оператор конкатенации строк +
print(s3)

# Разные типы данных просто так не складываются. Надо привести все к одному типу с помощью функций из lesson_7:
name = 'John'
age = 20
print('Me name is ' + name + '. I`m ' + str(age))

# Повторение(дубоирование) строк:
print('hi ' * 5)  # строка продублируется заданное колличество раз

'''Индексация строк. Строка это последовательность символов которые могут быть проиндексированы. Можно получить из 
строки каждый конкретный символ или например перебрать символы в циклах

Строка  H     e      l	     l	     o
Индекс S[0]	 S[1]	S[2]	S[3]	S[4]
Индекс S[-5] S[-4]	S[-3]	S[-2]	S[-1]
'''

s = 'Hello world!'
print(s[0])
print(s[11])
print(s[-1])
print(s[-12])

# Строки в питоне являются неизменяемыми последовательностями, их можно только пересоздавать
s = 'Hello world!'
# попробуем заменить первый символ строки
# s[0] = 'D'

'''
Срезы строк:
Оперваторы извлечения срезы имеют такой синтаксис [X:Y:Z]
X - начало среза, Y - окончание, Z - шаг.
Все эти пораметры не являются обязательными.
'''

print(s[0:12])  # Hello world!
print(s[0:-1])  # Hello world!
print(s[0:5])  # Hello
print(s[:5])  # Hello
print(s[6:])  # world!
print(s[::2])  # Hlowrd

'''
Перевернуть строку можно поставив отрицательный шаг!!!
'''
print(s[::-1])  # !dlrow olleH

# срезы можно складывать:
print(s[:5] + s[6:])  # Helloworld!
