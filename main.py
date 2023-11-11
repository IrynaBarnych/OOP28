#статичні атрибути
class Bank:
    interest_rate = 0.05 #статичний атрибут класу
print(Bank.interest_rate)
#статичний виклик атрибуту
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now I am {self.age} years old.")

person = Person("Oleg", 12)
person.greet()
person.celebrate_birthday()
result = Person.greet(person)

#статичний метод
class Calculator:
    #x = 10
    @staticmethod
    def add(y, x):
        return x + y
print(Calculator.add(2, 3))
#метод класу
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def bonus(self):
        return person.greet() + 10

p1 = Person("Oleg")
p2 = Person("Olga")
print(Person.get_count())
print(p1.count)
print(p2.count)
p1.count = 3
p2.count = 4
print(Person.get_count())
print(p1.count)
print(p2.count)

# практичне завдання
class Calculator:
    #сценарій 2
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2
    @classmethod
    def add_numbers_rounded(cls, num1, num2):
        rounded_num1 = round(num1)
        rounded_num2 = round(num2)
        return cls.add_numbers(rounded_num1, rounded_num2)
print(Calculator.add_numbers(2.7,3.4))
print(Calculator.add_numbers_rounded(2.7,3.4))
