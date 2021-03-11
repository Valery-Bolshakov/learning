from bs4 import BeautifulSoup
import urllib.request


class Parser:
    # введем свойства которые потребуются для парсинга
    raw_html = ''
    html = ''
    results = []

    # введем конструктор для класса. Он будет принимать 2 параметра. 1й - 'url' который будет передаваться при
    # создании обьекта и далее будем оперировать им для создания запроса. 2й - 'path' путь к файлу для записи
    def __init__(self, url, path):
        self.url = url
        self.path = path

    # пишем метод-запрос для получения информации с сайта:
    def get_html(self):

        # пишем запрос к нужному сайту
        request = urllib.request.urlopen(self.url)  # адрес сайта будет задаваться параметром при создании обьекта
        # класса, по этому вместо адреса - вводим данное свойство self.url

        # читаем информацию с запроса
        self.raw_html = request.read()  # запишем в свойство raw_html НЕОБРАБОТАННЫЙ html текст

        # используя BeautifulSoup приведем html текст к более красивому виду и запишем это в свойство html:
        self.html = BeautifulSoup(self.raw_html, 'html.parser')  # получаем ОБРАБОТАННЫЙ html

    # напишем метод который удалит всю лишнюю информацию кроме необходимой:
    def parsing(self):

        # обратимся к свойству html, получим оттуда информацию(find_all) с указанными фильтрами ('li', class_='')
        news = self.html.find_all('li', class_='liga-news-item')  # запишем в перменную все li класса liga-news-item

        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            # ищем блок с заголовком новости. он находится в элемента span и классом с элементом d-block
            # добавим метод get_text что бы вытащить только текст
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')

            # запишем всю отфильтрованную информацию в свойство results
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href
            })

    # напишем метод save который запишет всю полученную из метода parsing информацию в нужный файл
    def save(self):
        """
        Можно реализовать метод таким путем:
        f = open('news_39.txt', 'w', encoding='utf-8')
        i = 1
        for item in results:
            f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n')
            i += 1
        f.close()

        А можно и другим, который будет представлен ниже. Метод автоматически закрывает файл после отрабатывания
        """

        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(
                    f'Новость №{i}\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n')
                i += 1

    # напишем некий метод который будет вызывать все остальные методы. его пишут либо в начале либо в конце.
    def run(self):
        self.get_html()
        self.parsing()
        self.save()
