from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def fill_color(self):
        pass

    @abstractmethod
    def erase(self):
        pass


class Circle(Shape):

    def draw(self):
        print("Тип фігури : коло ")

    def fill_color(self):
        print(f"Колір заливки червоий ")

    def erase(self):
        print("Фігура видалена ")


class Rectangle(Shape):
    def draw(self):
        print("Тип фігури : прямокутник ")

    def fill_color(self):
        print(f"Колір заливки чорний ")

    def erase(self):
        print("Фігура видалена ")


class Creator(ABC):

    def render(self):
        shape = self.createProduct()
        shape.draw()
        shape.fill_color()

    @abstractmethod
    def createProduct(self):
        pass


class CreateCircle(Creator):
    def createProduct(self):
        return Circle()


class CreateRectangle(Creator):
    def createProduct(self):
        return Rectangle()


def client_code(creator: Creator):
    return creator.render()


c=client_code(CreateCircle())
r=client_code(CreateRectangle())

