#Завдання 5
#Створіть клас Character, який має атрибути name, health та damage. Реалізуйте метод класу attack, який виводить
#повідомлення про атаку гравця.

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other):
        print(f"{self.name} атакує і завдає {self.damage} одиниць урону {other.name}!")
        other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.health -= damage
        print(f"{self.name} отримує {damage} одиниць урону. Залишок здоров'я: {self.health}")

    @staticmethod
    def display_info(player):
        print(f"Інформація про {player.name}: Здоров'я - {player.health}, Урон - {player.damage}")

# Створення гравців
player1 = Character("Гравець 1", 100, 20)
player2 = Character("Гравець 2", 90, 15)

# Атаки гравців
player1.attack(player2)
player2.attack(player1)

# Виведення інформації про гравців за допомогою статичного методу
Character.display_info(player1)
Character.display_info(player2)





