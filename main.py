#Завдання 6
#Створіть клас Student, який має атрибути name, age, grade та courses. Реалізуйте метод класу add_course, який
#додає новий предмет до списку курсів студента

class Student:
    students_count = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.students_count += 1

    def add_course(self, course):
        print(f"Предмет {course} додано до списку курсів студента {self.name}.")

    @staticmethod
    def get_students_count():
        return Student.students_count

student1 = Student("Іван", 20, "A")
student2 = Student("Марія", 22, "B")

student1.add_course("Математика")
student1.add_course("Фізика")
student2.add_course("Хімія")

print(f"Загальна кількість студентів: {Student.get_students_count()}")




