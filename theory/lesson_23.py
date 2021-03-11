print('Словари', '\n')

'''
Словарь — изменяемый объект-отображение. dict([obj, ][**kwargs])
    obj : Первым необязательным позиционным аргументом может являться отображение или итерирующийся 
объект (при этом каждый его элемент должен быть тоже итерирующемся и содержать ровно два объекта).
    kwargs : Поддерживаются также необязательные именованные аргументы. При использовании вкупе с 
позиционными аргументами и совпадении ключей значениями из именованных пользуются приоритетом.
'''
# Создание Словаря через литерал:
d = {}
print(d, type(d))

product1 = {
    'title': 'Sony',
    'price': 100
}
print(product1, '\n')  # {'title': 'Sony', 'price': 100}

# Создание Словаря через конструктор:
d = dict()
print(d, type(d))

product2 = dict(title='iPhone', price=101)
print(product2, '\n')  # {'title': 'iPhone', 'price': 101}

# Создание Словаря из списка или кортежа:
users = [
    ['email_1@gmail.com', 'Email_1'],
    ['email_2@gmail.com', 'Email_2'],
    ['email_3@gmail.com', 'Email_3']
]  # сщздали списка
print(users)  # [['email_1@gmail.com', 'Email_1'], ['email_2@gmail.com', 'Email_2'], ('email_3@gmail.com', 'Email_3']]

d_users = dict(users)  # преобразовали списка в Словаря
print(d_users, '\n')  # {'email_1@gmail.com': 'Email_1', 'email_2@gmail.com': 'Email_2', 'email_3@gmail.com': 'Email_3'}

users1 = (
    ('email_1@gmail.com', 'Email_1'),
    ('email_2@gmail.com', 'Email_2'),
    ('email_3@gmail.com', 'Email_3')
)  # сщздали кортежа
print(users1)  # (('email_1@gmail.com', 'Email_1'), ('email_2@gmail.com', 'Email_2'), ('email_3@gmail.com', 'Email_3'))

d_users = dict(users1)  # преобразовали кортежа в Словаря
print(d_users, '\n')  # {'email_1@gmail.com': 'Email_1', 'email_2@gmail.com': 'Email_2', 'email_3@gmail.com': 'Email_3'}

# Создание словаря методом formkeys:
prosuct3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(prosuct3)  # {'price1': 50, 'price2': 50, 'price3': 50}

prosuct3 = dict.fromkeys(['price1', 'price2', 'price3'])
print(prosuct3)  # {'price1': None, 'price2': None, 'price3': None}

# Создание словаря с помощью генераторов:
nums = {i: i + 1 for i in range(1, 10)}
# В качестве ключа мы последовательно берем числа от 1 до 9 из range, а в значения записываем те же числа + 1
print(nums, '\n')  # {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

'''
Получение данных из словаря
Для получения значений из словаря просто обращаемся к нему по нужному ключу. Либо использовать метод .get
Метод get возвращает либо значение либо None, если ключа не существует.
Следует обратить внимание на то какой тип данных у ключа(строка или число) и обращаться соответствующе
'''

product1 = {
    'title': 'Sony',
    'price': 100
}

product2 = dict(title='iPhone', price=101)

print(product1['title'])  # Sony
print(product1.get('title'))  # Sony or None
print(product1.get('title2', 'no key!!!'))  # Выдаст значение либо no key!!!, если ключа не существует
print(product2['title'])  # iPhone

# print(nums['1'])  # KeyError: '1'
print(nums[8], '\n')  # 9

# Перебираем словарь
for key in product1:
    print(key)  # title, price
    print(product1[key])  # Sony, 100
    print(f'{key}: {product1[key]}\n')  # title: Sony, price: 100

'''метод .items() выводит пары ключ-значения:'''
print(product1.items())  # dict_items([('title', 'Sony'), ('price', 100)])
for key, value in product1.items():
    print(key, value)  # title: Sony, price: 100

'''
Когда значений в словаре много - их можно поместить в список для удобства
'''

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]

print(products)
# [{'title': 'Sony', 'price': 100}, {'title': 'iPhone', 'price': 110}, {'title': 'Samsung', 'price': 90}]
for product in products:
    print(product['title'], product['price'])  # Sony 100
    # iPhone 110
    # Samsung 90
