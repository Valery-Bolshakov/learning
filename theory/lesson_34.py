from bs4 import BeautifulSoup
import urllib.request

print('Парсинг\n')

'''
help('modules') - Покажет все доступные модули в Python Console
pip (аналог композера в php) - система управления пакетами, которая используется для установки и 
управления программными пакетами, написанными на Python. 

Beautiful Soup - это пакет Python для анализа документов HTML и XML. Он создает дерево синтаксического 
анализа для проанализированных страниц, которое можно использовать для извлечения данных из HTML, 
что полезно для парсинга веб-страниц.

Urllib — это модуль, который можно использовать для открытия URL-адресов. Он определяет функции и классы 
для обработки URL-адресов.
'''

# Для начала необходимо сделать Запрос:
req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()  # Создаем переменную и запишем в нее прочитанную с сайта информацию(набор символов)

# далее используем модуль BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')  # 'html.parser' вводим параметр что бы избежать ошибок в работе модуля
# print(soup)  # Выдаст html код страницы с тегами текстом и прочей атрибутикой

# Далее получаем новости с сайта:
news = soup.find_all('li', class_='liga-news-item')  # Ищем все эдементы li  класса liga-news-item
#  с помощью метода find.all - получаем все новости. Если надо что то одно - используем метод find

# print(news)  # Получим список с набором элементов

# Отфильтруем список и выберем только ключевые элементы
results = []  # Сделаем список с элементами из Словарей

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    # ищем блок с заголовком новости. он находится в элемента span и классом с элементом d-block
    # добавим метод get_text что бы вытащить только текст
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href
    })

# Получаем Список Словарей
# print(results)  # [{'title': 'Красюк: По контракту с Усиком у нас еще 1 бой', 'desc': 'Но переговоры проходят...

# Создаем новый файл и Запишем(Каждый раз перезаписываются) новости в отформатированном виде:
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n')
    i += 1
f.close()
