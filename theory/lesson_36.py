print('Основы ООП. Класс и объект\n')

''' Создали обьект класса с названием А'''
# class A:
#     pass

'''Создаем экземпляр класса'''
# a = A()
# print(a)  # <__main__.A object at 0x0000020CA6E8BD90> Получили обьект класса А

'''Определим для данного обьекта какие нибудь атрибуты(свойства)'''


# a.property1 = 'Property 1'
# a.property2 = 'Property 2'
# print(a.property1)  # Property 1


class A:
    # Рекомендуется задавать свойства внутри класса
    property1 = 'Property 1'
    property2 = 'Property 2'

    # Создаем метод внутри класа:
    # Допишем еще какие нибудь параметры помимо self:
    # Параметрам можно задавать значения по умолчанию
    def say_hi(self, name, age='18'):
        """
        аргумент self это специальное ключевое слово который содержит в себе указатель на экземпляр класса
        """
        return f'Hi, {name}, {age}'


a = A()
b = A()
print(a.property2)  # Property 2
# print(a.say_hi('Qrii'))  # Hi Qrii
# print(b.say_hi('Trii'))  # Hi Trii

print(a.say_hi('Qrii'))  # Hi Qrii, 18
print(b.say_hi('Trii', '20\n'))  # Hi Trii, 20


class B:
    # Свойство можно определять не в методе и затем передавать их аргументом в метод:
    name = 'user'

    def say_u(self, name=''):
        # Аргумент name делаем Необязательным: name=''
        # Для того что бы это сработала - вводим условие:
        if name:
            # Если аргумент задается при вызове класса то выполняется это условие,
            # иначе подставится значение по умолчанию
            return f'Hi, {name}'
        else:
            # Для того что бы вызвать свойство name надо обратиться к self + свойство:
            return f'Hello, {self.name}'


a = B()
b = B()

print(b.say_u())  # Hello, user
print(a.say_u('Pio'))  # Hi, Pio
