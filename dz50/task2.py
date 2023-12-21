class Car:
    brand = "BMW"
    total = 0

    def __init__(self, name, year, engine, color, prise):
        self.name = name
        self.year = year
        self.engine = engine
        self.color = color
        self.price = prise
        Car.total += self.price

    def __str__(self):
        return f"""
                   Car: {self.name},
                   Brand: {self.brand},
                   Year: {self.year},
                   Engine capacity: {self.engine}
                   Color: {self.color}
                   Prise: {self.price}                    
                    """

    def change_color(self, new_color):
        self.color = new_color

    def change_price(self, new_prise):
        Car.total = Car.total - self.price
        self.price = new_prise
        Car.total += new_prise


car1 = Car("X3", 1992, 2.8, "red", 2500)
car2 = Car("X6", 2000, 2.9, "blue", 5500)
car3 = Car("X4", 1995, 1.8, "green", 4000)
print("Cумарна ціна створенихавтомобілів",Car.total)
print(car1)

car1.change_color("blue")
car1.change_price(4000)
print(car1)
print("Cумарна ціна створенихавтомобілів",Car.total)
