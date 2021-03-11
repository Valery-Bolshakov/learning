from class_39 import Parser

print('Класс парсинга\n')

# создаем обьект класса, с параметрами url и path:
# В параметре url лежит адрес сайта, в path - путь до файла в который парсим сайт. т.к. файл лежит в корневой
# папке - пишем просто название файла.
parser = Parser('https://www.ua-football.com/sport', 'news_39.txt')
parser.run()  # запускает скрипт class_39


# print(parser.raw_html)  # обращаясь к свойству - получаем необработанный html
# print(parser.html)  # обращаясь к свойству - получаем ОБРАБОТАННЫЙ html
# print(parser.results)  # обращаясь к свойству - получаем ОТФИЛЬТРОВАНЫЙ html














