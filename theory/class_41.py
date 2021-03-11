class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, elem):
        if elem in range(1, 101):
            self.__age = elem
        else:
            print('Wrong age')

    # Переопределим один из методов суперкласса Object __str__
    def __str__(self):
        """переопределённый метод str должен возвращать СТРОКУ"""
        # return f'Name: {self.name}'

        # или выведем например Имя данного класса следующей конструкцией:
        # Метод 'self.__class__.__name__' выводит имя класса в котором он находится(пофиг отнаследован он или нет)
        return 'Class: ' + self.__class__.__name__


class Employee(Person):

    def __init__(self, name, age, company):
        """
        Дополним метод подкласса новыми параметрами (self.company = company) + наследуем параметры суперкласса:

        Убираем код который был в главном классе и пишем новый конструктор. В новый конструктор передаем
        параметры главного класса name и age следующей конструкцией 'super().__init__(name, age)'.
        Это позволит при вызове метода передавать различные значения аргумента company. И избежим дублирования
        кода суперкласса.
        """
        super().__init__(name, age)  # super(Employee, self).__init__ более старый вариант записи
        self.company = company

    # в новых методах подкласса недоступны закрытые свойства родительского коасса
    def more_info(self):
        print(f'Name: {self.name} works in {self.company}')

    # Подобным образом (как с конструктором) можно переписывать любые методы Главного класса
    def print_info(self):
        """
        Теперь данный метод выполнит код 'print(f'Name: {self.name}, Age: {self.__age}')' из главного класса.
        Затем код 'print(f'Work: {self.company}')' подкласса.
        """
        super().print_info()
        print(f'Work: {self.company}')
