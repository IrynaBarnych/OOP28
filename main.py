#Завдання 4
#Створіть клас FileUtils, який має метод класу count_lines, який приймає шлях до файлу і повертає
#кількість рядків у файлі.

class FileUtils:
    @classmethod
    def count_lines(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            return -1

file_path = 'приклад.txt'


lines_count = FileUtils.count_lines(file_path)
print(f"Кількість рядків у файлі '{file_path}': {lines_count}")

print(f"Файл '{file_path}' не знайдено.")






