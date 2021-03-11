from class_41 import Person, Employee

print('Полиморфизм\n')

person = Person('Katy', 25)
person.print_info()  # Name:  Katy, Age: 25
# person.age = 30  # Изменяем закрытое свойство с помощью Геттера и Сеттера
# person.print_info()  # Name:  Katy, Age: 30
print(person)  # Class: Person

# создали экземпляр подкласса
employee = Employee('Eefje', 25, 'Google')
employee.print_info()  # Name: Eefje, Age: 25  +  Work: Google
employee.more_info()  # Name: Eefje works in Google

'''
Начиная с 3й версии Python Все классы неявно наследуют один Общий Суперкласс Object и все его методы.
    Данные методы можно увидеть если ввести название экземпляра класса и точку (employee.). Далее мы увидим 
список доступных методов Object ( __метод__).  Их можно переопределить.
'''
# employee.

# простой принт экземпляра по умолчанию вызывает метод клааса Object __str__ и выводит следующее:
# print(employee)  # <class_41.Employee object at 0x000001FE2A366E50>
# После его переопределения выводит:
# print(employee)  # Name: Eefje
print(employee)  # Class: Employee
