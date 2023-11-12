# Завдання 3
# Створіть клас для конвертування з метричної системи в англійську, та навпаки.
# Реалізуйте функціональність у вигляді статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.

class Converter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feets):
        return feets * 0.3048

meters_length = 10
feet_length = Converter.meters_to_feet(meters_length)
print(f"{meters_length} метрів дорівнює {feet_length} футів")

feet_length = 32.8084
meters_length = Converter.feet_to_meters(feet_length)
print(f"{feet_length} футів дорівнює {meters_length} метрів")

