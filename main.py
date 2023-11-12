# Завдання 4
# До вже реалізованого класу «Книга» додайте необхідні перевантажені методи та оператори.

class Book:
    def __init__(self, title, author, genre, date):
        self.title = title
        self.author = author
        self.genre = genre
        self.date = date

    def __sub__(self, other):
        return self.date - other.date

    def __lt__(self, other):
        return self.date < other.date

    def Book(self):
        print(f"Назва книги: {self.title}, Автор: {self.author}, Жанр: {self.genre}, Дата випуску: {self.date}")

my_book_info1 = Book("Кобзар", "Т. Г. Шевченко", "різні літературні жанри", 1840)
my_book_info1.Book()

my_book_info2 = Book("Енеїда", "І. П. Котляревський", "комічна епічна поема", 1798)
my_book_info2.Book()

date_difference = my_book_info1 - my_book_info2
print(f"Різниця в роках: {date_difference}")

if my_book_info1 == my_book_info2:
    print("Ці книги мають одного автора та однакову назву.")

if my_book_info1 < my_book_info2:
    print(f"{my_book_info1.title} вийшла раніше за {my_book_info2.title}.")
else:
    print(f"{my_book_info2.title} вийшла раніше за {my_book_info1.title}.")