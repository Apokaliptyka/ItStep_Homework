class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name:{self.name}, Age:{self.age}, Type:{self.__class__} ")


class Student(Person):

    def __init__(self, name, age, person_id):
        super().__init__(name, age)
        self.person_id = person_id

    def study(self, subgect):
        print(f"Name:{self.name},id:{self.person_id},subject:{subgect}")

    def introduce(self):
        print(f"Name:{self.name}, Age:{self.age},id:{self.person_id}, Type:{self.__class__} ")


class Teacher(Person):

    def __init__(self,name,age, subject):
        super().__init__(name,age)
        self.subject = subject

    def teach(self,s):
        if type(s) is Student:
            print(f"Teacher {self.name} studing {self.subject} student {s.name}")
        else:
            print(f" Object {s} not in class Student")

    def introduce(self):
        print(f"Name:{self.name}, Age:{self.age},subject:{self.subject}, Type:{self.__class__} ")



class Employee(Person):
    def __init__(self,name,age,salary,specialty):
        super().__init__(name,age)
        self.salary=salary
        self.asecialty=specialty

    def work(self):
        print(f"Name:{self.name},specialty:{self.asecialty},salary:{self.salary}")

    def introduce(self):
        print(f"Name:{self.name}, Age:{self.age},specialty:{self.asecialty},salary:{self.salary}, Type:{self.__class__} ")

person=Person("Andrew",28)
person.introduce()
student=Student("Nata",21,"66666")
student.study("Math")
student.introduce()
teacher=Teacher("Marta",33,"Math")
teacher.teach(student)
teacher.introduce()
spesialistic=Employee("Alica",22,1500,"developer")
spesialistic.work()
spesialistic.introduce()