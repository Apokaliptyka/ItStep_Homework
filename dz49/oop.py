class Person:
    """Опис класу.
    Ці рядки автоматично можна подивитись функцією help"""

    def __init__(self,name="xxx",money=0):

        self.name=name
        self.money=money
        self.friend=[]
        print('A new Person is born! -> ',self.name)

    def know(self,person):
        self.friend.append(person.name)
    def is_know(self,person):
        return person.name in self.friend

    def replenishment(self):
        if self.money <50:
            self.money=self.money + 100
        print('Рахунок {}  всього = {}'.format(self.name,self.money))

    def __str__(self):
        return self.name + str(self.money)

    def giveMoney(self,delta):
        self.money+=delta
        print('Рахунок {} поповнено на суму {}, всього = {}'.format(self.name,delta,self.money))

A = Person()
B = Person()
C= Person("Petro",10)
D= Person("Ira",30)
print('A: Name = {},money = {:.2f}'.format(A.name, A.money))
print('B: Name = {},money = {:.2f}'.format(B.name, B.money))

A.name = "Ivan"
B.name = "Anna"
B.money = 100.2852

A.giveMoney(50.127)
B.giveMoney(40)

print('A: Name = {},money = {:.2f}'.format(A.name, A.money))
print('B: Name = {},money = {:.2f}'.format(B.name, B.money))


def info(person):
    i = person.name + str(person.money)
    return i
people=[A,B,C,D]

for p in people:
    print(p)
# help(Person)

A.replenishment()
B.replenishment()
C.replenishment()
D.replenishment()

A.know(B)
B.know(C)
A.know(D)
D.know(B)
C.know(A)
print(f"A know is B?",A.is_know(B))
print(f"B know is C?",B.is_know(A))
print(f"D know is B?",D.is_know(B))
print(f"C know is A?",C.is_know(A))