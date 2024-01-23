# class Student:
#     team="Python31"
#     __slots__ = ["name","age","gender"]
#
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#     def greet(self):
#         print("Hi,my name is",self.name)
#
#     def description(self):
#         print(f"Person<{self.name},{self.age},{self.gender}>")
#
# s=Student("Alex",20,"female")
# print(s.name)


def init(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def greet(self):
    print("Hi, my name is", self.name)

def description(self):
    print(f"Person<{self.name},{self.age},{self.gender}>")


Student = type(
    "Student",
    (),
    {
        "team": "Python31",
        "__slots__": ["name", "age", "gender"],
        "__init__": init,
        "greet": greet,
        "description": description,
    }
)


student= Student("John", 20, "Male")
student.greet()
student.description()
print(student.name)
print(student.team)
print(Student.__dict__)