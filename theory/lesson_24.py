print('Методы словаря', '\n')

'''Словари неупорядочены

Методы для работы со словаря
dict.copy() Возвращает  копию словаря.
dict.get(key[, default]) -> Значение по ключу, либо default. Возвращает значение из словаря по указанному ключу.
    key : Ключ, значение по которому требуется получить.
    default : Значение, которое следует вернуть, если в словаре не окажется указанного ключа. По умолчанию — None.
dict.clear() Удаляет из словаря все его элементы.
dict.items() - возвращает пары ключ-значение
dict.keys() - возвращает ключи в словаре
dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет возвращает default, 
    (по умолчанию бросает исключение)
dict.popitem() - удаляет и возвращает пару ключ-значение. Если словарь пуст - исключение KeyError
dict.setdefault(key[, default]) -> Значение по ключу, либо default
    Возвращает значение по ключу, инициализируя элемент словаря, если необходимо, указанным значением.
    Позволяет получить значение из словаря по ключу. Автоматически добавляет элемент словаря, если он отсутствует.
dict.update([other], **kwargs) -> None. Обновляет данные словаря, заменяя значения при совпадении ключей.
    Позволяет обновить данные словаря, или дополнить их. Существующие ключи перезаписываются
dict.values() - Возвращает значения словаря.
'''

product1 = {'title': 'Sony', 'price': 100}
print(product1.items())  # dict_items([('title', 'Sony'), ('price', 100)])
print(product1.keys(), '\n')  # dict_keys(['title', 'price'])
# print(product1.pop('title'))  # Sony
# print(product1.pop('title2', 'NO'))  # NO

print(product1)
# print(product1.setdefault('title'))  # Sony
# print(product1.setdefault('title2', 'test'))  # None
print(product1, '\n')  # {'title': 'Sony', 'price': 100, 'title2': 'test'} Добавились новые ключ-значение

product1.update({'test': 'value'})
print(product1)  # {'title': 'Sony', 'price': 100, 'test': 'value'}
product1.update({'price': '200'})  # Перезаписали значение ключа
print(product1, '\n')  # {'title': 'Sony', 'price': '200', 'test': 'value'}

print(product1.values())  # dict_values(['Sony', '200', 'value'])
