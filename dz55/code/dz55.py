+import  math

class Vector:

    def __init__(self, x, y, z):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
            raise TypeError("Тип операнта повинен бути числовим ")

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        try:
            if isinstance(other, Vector):
                new_x = self.x + other.x
                new_y = self.y + other.y
                new_z = self.z + other.z
            else:
                raise TypeError("Можна додати тільки інший вектор")
            return Vector(new_x, new_y, new_z)
        except TypeError as t:
            return f"Помилка додавання: {t}"

    def __sub__(self, other):
        try:
            if isinstance(other, Vector):
                new_x = self.x - other.x
                new_y = self.y - other.y
                new_z = self.z - other.z
            else:
                raise TypeError("Можна відняти тільки інший вектор")
            return Vector(new_x, new_y, new_z)
        except TypeError as t:
            return f"Помилка віднімання: {t}"

    def __iadd__(self, other):
        try:
            if isinstance(other, Vector):
                self.x += other.x
                self.y += other.y
                self.z += other.z
            else:
                raise TypeError("Можна додати тільки інший вектор")
        except TypeError as t:
            return f"Помилка iadd: {t}"
        return self

    def __isub__(self, other):
        try:
            if isinstance(other, Vector):
                self.x -= other.x
                self.y -= other.y
                self.z -= other.z
            else:
                raise TypeError("Можна відняти тільки інший вектор")
        except TypeError as t:
            return f"Помилка isub: {t}"
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Множення підтримується тільки для числа або вектора")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __len__(self):
         return round(math.sqrt(abs(self.x**2) + abs(self.y**2) + abs(self.z**2)))

    def __int__(self):
        return int(len(self))

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __bool__(self):
        return bool(len(self))
