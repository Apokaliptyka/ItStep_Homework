from dz55 import Vector

vector1 = Vector(1, 2, 6)
vector2 = Vector(1, 2, 3)
print(vector1 == vector2)
print(vector1 != vector2)
vector3 = vector2 + vector1
print(vector3)
vector4 = vector3 - vector1
print(vector4)
vector4+=vector1
print(vector4)
vector4-=vector1
print(vector4)

print(vector4*100)
print(vector4*vector1)
print(10*vector4)
print(len(vector4))
int_vector4=int(vector4)
print(int_vector4)
print(vector4.__neg__())
print(vector4.__bool__())


