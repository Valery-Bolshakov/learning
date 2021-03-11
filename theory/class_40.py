class Person:

    # конструктор
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # создаем метод который будет печатать данные о какой то персоне
    def print_info(self):
        print(f'Name:  {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, elem):
    #     if elem in range(1, 101):
    #         self.__age = elem
    #     else:
    #         print('Wrong age')

    """С помощью геттеров и сеттеров можно изменить закрытые свойства"""

    @property  # Геттер
    def age(self):
        return self.__age

    @age.setter  # Сеттер - @age.setter:
    def age(self, elem):
        if elem in range(1, 101):
            self.__age = elem
        else:
            print('Wrong age')


# Создаем новый класс, который будет наследовать свойства и методы класса Person:
# можно расширить функционал подкласса:
class Employee(Person):
    company = 'Google'

    # в новых методах подкласса недоступны закрытые свойства родительского коасса
    def more_info(self):
        print(f'Name:  {self.name} works in {self.company}')
