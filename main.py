# Завдання 4
# Створіть клас InformationSystem, який має атрибут data - словник, де ключі - це імена користувачів, а значення -
# список їх контактів. Реалізуйте методи класу для додавання нових користувачів та їх контактів.

class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user(self, username):
        self.data[username] = []

    def add_contact(self, username, contact):
        if username in self.data:
            self.data[username].append(contact)
        else:
            print(f"Користувач {username} не знайдений. Додайте користувача перед додаванням контактів.")

info_system = InformationSystem()

info_system.add_user("Анна")
info_system.add_user("Марія")

info_system.add_contact("Анна", "111")
info_system.add_contact("Анна", "222")
info_system.add_contact("Марія", "333")

print(info_system.data)

