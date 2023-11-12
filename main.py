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

player1 = Character("Гравець 1", 100, 20)
player2 = Character("Гравець 2", 90, 15)

player1.attack(player2)
player2.attack(player1)






