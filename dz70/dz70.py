from abc import ABC, abstractmethod
from math import pi

"""interface"""


class IShape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass


"""abstract class"""


class Shape(IShape):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def info(self):
        pass


class Square(Shape):

    def __init__(self, name: str, size: float):
        super().__init__(name)
        self.size = size

    def info(self):
        return f"{self.name} {self.size}"

    def get_area(self) -> float:
        return round(self.size * 4, 2)


class Circle(Shape):

    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    def info(self):
        return f"{self.name} {self.radius}"

    def get_area(self) -> float:
        return round(pi * (self.radius) ** 2)


class Pizza:
    def __init__(self, price: float, shape:Shape):
        self.__price = price
        self.__shape = shape

    def get_price(self) -> float:
        return self.__price

    def get_shape_class(self) -> str:
        return self.__shape.__class__.__name__

    def cut_pizza(self):
        return f"Name:{self.__shape.name},price:{self.__price} UAH, area:{self.__shape.get_area()} sm"


if __name__ == "__main__":

    square = Square("Margarita", 15)
    circle = Circle("Italia", 10)
    print("Площа фігури",circle.get_area())

    pizza_square = Pizza(150, square)
    pizza_circle = Pizza(120, circle)
    print(pizza_circle.cut_pizza())
    print(pizza_square.cut_pizza())

    pizza_circle.cut_pizza()
    print("Фігура класу ",pizza_circle.get_shape_class())
    print("Ціна піци",pizza_circle.get_price())
