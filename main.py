#Завдання 3
#Створіть клас для підрахунку максимуму з чотирьох аргументів, мінімуму з чотирьох аргументів, середнє
#арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
#методів.

import math
import math

class Calculator:
    count_of_calculations = 0

    @staticmethod
    def max_value(a, b, c, d):
        Calculator.count_of_calculations += 1
        return max(a, b, c, d)

    @staticmethod
    def min_value(a, b, c, d):
        Calculator.count_of_calculations += 1
        return min(a, b, c, d)

    @staticmethod
    def average(a, b, c, d):
        Calculator.count_of_calculations += 1
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        Calculator.count_of_calculations += 1
        return math.factorial(n)

a, b, c, d = 5, 10, 15, 20

max_result = Calculator.max_value(a, b, c, d)
min_result = Calculator.min_value(a, b, c, d)
average_result = Calculator.average(a, b, c, d)
factorial_result = Calculator.factorial(a)

print("Максимум:", max_result)
print("Мінімум:", min_result)
print("Середнє арифметичне:", average_result)
print(f"Факторіал {a}:", factorial_result)
print("Кількість обчислень:", Calculator.count_of_calculations)
