from math import pi

class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return f" Circle have radius:{self.radius}"

    def area_of_circle(self):
        return f" Area of a circle is {self.radius**2*pi:.2f}"

    def circuit(self):
        return f" Circle lenght is {2*pi*self.radius:.2f}"


circle1=Circle(2)
circle2=Circle(3)
print(circle1)
print(circle2)
print(circle1.area_of_circle())
print(circle2.circuit())