"""Завдання 2
Створіть клас для підрахунку площі геометричних
фігур. Клас має надавати функціональність підрахунку
площі трикутника за різними формулами, площі прямокутника,
 площі квадрата, площі ромба. Методи класу для
підрахунку площі реалізуйте за допомогою статичних
методів. Також клас має розрахувати кількість підрахунків
 площі та повернути це значення статичним методом"""

import math
class AreaCalculator:
    count_of_calculations = 0

    @staticmethod
    def triangle_area(a, h):
        AreaCalculator.count_of_calculations += 1
        return 0.5 * h * a
    @staticmethod
    def rectangle_area(a, b):
        AreaCalculator.count_of_calculations += 1
        return a * b
    @staticmethod
    def square_area(a):
        AreaCalculator.count_of_calculations += 1
        return a ** 2

    @staticmethod
    def rhombus_area(a,b):
        AreaCalculator.count_of_calculations += 1
        return 0.5 * math.sqrt(a) * math.sqrt(b)


triangle = AreaCalculator.triangle_area(2, 5)
print(f"Площа трикутника: {triangle}")
rectangle = AreaCalculator.rectangle_area(2, 5)
print(f"Площа прямокутника: {rectangle}")
area = AreaCalculator.square_area(5)
print(f"Площа квадрата: {area}")
rhombus = AreaCalculator.rhombus_area(4,4)
print(f"Площа ромба: {rhombus}")

print("Кількість підрахунку площ", AreaCalculator.count_of_calculations)