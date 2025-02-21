class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"

book1 = Book("Harry Potter", "J.K Rowling", 1997)
book2 = Book("The Da Vinci Code", "Dan Brown", 2003)
book3 = Book("The Hanger Games", "Suzanne Collins", 2008)

print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
