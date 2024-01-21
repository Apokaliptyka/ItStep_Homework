from dz55 import Vector


class NewVector(Vector):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.list_vector = [self.x, self.y, self.z]

    def __getitem__(self, index):
        try:
            return self.list_vector[index - 1]
        except IndexError:
            return (f"Такого індекса {index} не існує!")

    def __setitem__(self, index, value):
        try:
            self.list_vector[index - 1] = value
            self.x, self.y, self.z = self.list_vector
        except IndexError:
            return (f"Такого індекса {index} не існує!")

    def __contains__(self, item):
        if item in self.list_vector:
            return True

    def __call__(self):
        for item in self.list_vector:
            if item < 0:
                print(f"Кордината {item} є від'ємна . ")
            elif item == 0:
                print(f"Кордината {item} є нульова . ")
            else:
                print(f"Кордината {item} є додатня. ")



v=NewVector(10,20,9)
v[1]=100
print(v)