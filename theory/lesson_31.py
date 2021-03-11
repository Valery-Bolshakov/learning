from datetime import date, datetime, timedelta
import locale

# Импортируем из модуля datetime класс date, позволяет работать с датами
# Импортируем из модуля datetime класс datetime, работа с дата-временем

print('Модуль Datetime\n')

# days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
# days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

'''Примеры для класса date'''
today = date.today()  # метод today класса date возвращает текущую дату.  МЕТОД
print(today)  # 2021-02-24  Свойство
print(today.day)  # 24  Свойство
print(today.month)  # 2  Свойство
print(today.year)  # 2021  Свойство
print(today.weekday(), '\n')  # 2 - среда. Номер дня недели, начинается с 0.  МЕТОД

'''Примеры для класса datetime'''
now = datetime.now()  # 2021-02-24 20:18:59.627672
# now_2 = datetime.today()  # 2021-02-24 20:18:59.627672
print(now)

# print(now)  # 2021-02-24 20:18:59.627672
print(now.day)  # 24
print(now.month)  # 2
print(now.year)  # 2021
print(now.weekday())  # 2
print(now.hour)  # 20
print(now.minute)  # 23
print(now.second, '\n')  # 56

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
print(days[now.weekday()], '\n')  # вместо метода weekday() подставится 2, и days[2] выдаст 'Среда'

'''Метод strftime - с помощью данного методы можно получить отформатированные дату-время'''
now = datetime.now()
print(now)
print(now.strftime('%a'))  # Wed - Вывели день недели
print(now.strftime('%A'))  # Wednesday

'''Для вывода значений на русском - необходимо импортировать модуль locale и установить настройки на ru_RU
Но почему то у меня выводит ошибку'''
# locale.setlocale(locale.LC_ALL, 'ru_RU')
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

'''Выведем нужную нам дату'''
print(f'Дата: {now.strftime("%A, %d, %b, %Y")}')  # Дата: Wednesday, 24, Feb, 2021
print(f'Время: {now.strftime("%H:%M:%S")}\n')  # Время: 20:58:29

'''С помощью специальных маркеров можно вывести уже отформатированную дату-время:'''
print(now.strftime('%c'))  # Wed Feb 24 21:02:24 2021
print(now.strftime('%x'))  # 02/24/21
print(now.strftime('%X\n'))  # 21:02:24

'''Объект timedelta представляет собой продолжительность, разницу между двумя датами или временем.'''
now = datetime.today()
print(now.strftime('%c'))  # Wed Feb 24 21:18:11 2021
# Прибавим текущей дате какую-то временную отметку:
# print(now + timedelta(days=1, hours=2, minutes=15))  # 2021-02-25 23:33:11
d1 = now + timedelta(days=1, hours=2, minutes=15)

#                           Wed Feb 24 21:20:28 2021 - БЫЛО
print(d1.strftime('%c'))  # Thu Feb 25 23:35:28 2021 - СТАЛО
