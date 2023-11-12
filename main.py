# Завдання 3
# До вже реалізованого класу «Автомобіль» додайте необхідні перевантажені методи та оператори.

class Car:
    count = 0
    def __init__(self, brand, model, year, cost_USA, dolar):
        self.brand = brand
        self.model = model
        self.year = year
        self.cost_USA = cost_USA
        self.dolar = dolar
        Car.count += 1

    def start_engine(self):
        print("Двигун запущено")

    def __sub__(self, other):
        return self.year - other.year

    def __mul__(self, other):
        cost1 = self.cost_USA * self.dolar
        cost2 = other.cost_USA * other.dolar
        return abs(cost1 - cost2)

    def car_info(self):
        print(f"Марка автомобіля: {self.brand}, Модель: {self.model}, Рік випуску: {self.year},"
              f" Вартість у Доларах: {self.cost_USA}, Курс Долару: {self.dolar}")

    @staticmethod
    def get_count():
        return Car.count

# Створення екземплярів класу
car_instance1 = Car("BMW", "X5", 2022, 13999, 36)
car_instance1.start_engine()
car_instance1.car_info()
car_instance2 = Car("BMW", "X6", 2023, 17599, 36)
car_instance2.start_engine()
car_instance2.car_info()

difference = car_instance1 - car_instance2
print(f"Різниця в роках: {difference}")

cost_difference = car_instance1 * car_instance2
print(f"Різниця в вартості: {cost_difference} Гривень")

print("Кількість створених об'єктів:", Car.get_count())