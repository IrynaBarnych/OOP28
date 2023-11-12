#Завдання 1
#До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
#створених об’єктів класу «Людина».

from datetime import datetime
class People:
    num_of_instances = 0  #статичний атрибут класу

    def __init__(self, full_name, date_of_birth, contact_phone_number, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.contact_phone_number = contact_phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

        People.num_of_instances += 1 #рахуємо кількість ініціалізацій об'єкта

    @classmethod
    def get_num_of_instances(cls):
        return cls.num_of_instances

    def get_full_name(self):
        return self.full_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_contact_phone_number(self):
        return self.contact_phone_number

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_home_address(self):
        return self.home_address

    def __eq__(self, other):
        # Перевизначення оператора ==
        return self.full_name == other.full_name

    def __lt__(self, other):
        date1 = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        date2 = datetime.strptime(other.date_of_birth, "%Y-%m-%d")
        return date1 < date2

    def __sub__(self, other):
        date1 = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        date2 = datetime.strptime(other.date_of_birth, "%Y-%m-%d")
        difference = date1 - date2
        years = difference.days // 365  # Оцінка років
        return years

# Створення екземпляра класу
person1 = People("Шевченко Т.Г.", "2020-03-09", "0661234567", "Київ",
               "Україна", "вул. Листопадна буд. 4")
person2 = People("Котляревський І.П.", "2005-01-01", "0998765432", "Львів",
                 "Україна", "вул. Незалежності буд. 10")

print(f"ПІБ: {person1.get_full_name()}")
print(f"Дата народження: {person1.get_date_of_birth()}")
print(f"Контактний телефон: {person1.get_contact_phone_number()}")
print(f"Місто: {person1.get_city()}")
print(f"Країна: {person1.get_country()}")
print(f"Домашня адреса: {person1.get_home_address()}")


print(f"ПІБ: {person2.get_full_name()}")
print(f"Дата народження: {person2.get_date_of_birth()}")
print(f"Контактний телефон: {person2.get_contact_phone_number()}")
print(f"Місто: {person2.get_city()}")
print(f"Країна: {person2.get_country()}")
print(f"Домашня адреса: {person2.get_home_address()}")

if person1 == person2:
    print("Обидві людини мають однакове ім'я.")
else:
    print("Люди мають різні імена.")

if person1 < person2:
    print("Людина 1 молодший за Людину 2.")
else:
    print("Людина 1 старший Людина 2.")

difference = abs(person1 - person2)
print(f"Різниця в: {difference} роках")
print("Кількість людей: ", People.num_of_instances)