# Завдання 2
# Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки. У класі має знаходитися
# два статичні методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій.
# Також клас має розрахувати кількість підрахунків температури та повернути це значення статичним методом.

class Converter:
    count = 0
    @staticmethod
    def cel_to_fah(celsius):
        Converter.count += 1
        return (celsius * 9/5) + 32
    @staticmethod
    def fah_to_cel(fahrenheit):
        Converter.count += 1
        return (fahrenheit - 32) * 5/9
    @staticmethod
    def get_conversion_count():
        return Converter.count

celsius_temperature = 25
fahrenheit_temperature = Converter.cel_to_fah(celsius_temperature)
fahrenheit_temperature = 25
celsius_temperature = Converter.cel_to_fah(celsius_temperature)

print(f"{celsius_temperature} градусів Цельсія дорівнює {fahrenheit_temperature} градусів Фаренгейта")
print(f"{fahrenheit_temperature} градусів Цельсія дорівнює {celsius_temperature} градусів Фаренгейта")

print("Кількість підрахунків температури:", Converter.get_conversion_count())
