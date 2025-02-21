class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")


car1 = Car("Toyota", "Lexus LS", 1989)
car2 = Car("Toyota", "Mirai", 2014)


car1.display_info()
car2.display_info()
