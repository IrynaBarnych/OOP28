"""Завдання 2
Створіть клас для підрахунку площі геометричних
фігур. Клас має надавати функціональність підрахунку
площі трикутника за різними формулами, площі прямокутника,
 площі квадрата, площі ромба. Методи класу для
підрахунку площі реалізуйте за допомогою статичних
методів. Також клас має розрахувати кількість підрахунків
 площі та повернути це значення статичним методом"""

class AreaCalculator:
    count_of_calculations = 0

    @staticmethod
    def triangle_area(a, h):
        AreaCalculator.count_of_calculations += 1
        return 0.5 * h * a
    @staticmethod
    def square_area(a, b):
        AreaCalculator.count_of_calculations += 1
        return a * b
triangle = AreaCalculator.triangle_area(2, 5)
print(triangle)
square = AreaCalculator.square_area(23, 5)
print(square)
print("Кількість підрахунку площ", AreaCalculator.count_of_calculations)