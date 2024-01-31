

class Noda:
    def __init__(self, value):
        self.next = None
        self.data = value


class Stack:

    def __init__(self, max_size=-1):
        self.head = None
        self.max_size = max_size

    def push(self, value):
        new_noda = Noda(value)
        try:
            if self.max_size == 0:
                raise Exception("Stack is Full")
            if self.head is None:
                self.head = new_noda
            else:
                new_noda.next = self.head
                self.head = new_noda
            self.max_size -= 1
        except Exception as e:
            print(e)

    def display(self):  # Показати вміст списку
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

    def pop(self):
        if not self.is_empty():
            temp = self.head
            self.head = temp.next
            self.max_size += 1
            return temp.data

        raise Exception("Stack is Empty")

    def peak(self):
        if not self.is_empty():
            return self.head.data
        raise Exception("Stack is Empty")

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.max_size == 0

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def clear(self):
        self.head=None
        print("Стек очищено!")

if __name__=="__main__":
    stack=Stack(int(input("Введіть розмір стеку: ")))


    while True:
        menu=input("""Меню:
    1.	додавання рядка у стек; 
    2.	виштовхування рядка зі стеку; 
    3.	перевірку чи порожній стек, 
    4.	чи повний стек 
    5.	підрахунок кількості рядків у стеку ; 
    6.	повне очищення стеку 
    7.	отримання значення без виштовхування верхнього рядка зі стеку
    8.  вивести інформацію про стек 
    9.  вихід
    Введіть варіант : """)
        if menu=="1":
            stack.push(input("Введіть значення: "))
        if menu == "2":
            stack.pop()
            print("Елемент виштовхнений!")
        if menu == "3":
            print("Стек порожній ?",stack.is_empty())
        if menu == "4":
            print("Стек є повний?",stack.is_full())
        if menu == "5":
            print("Розмір стеку:", stack.size())
        if menu == "6":
            stack.clear()
        if menu == "7":
            print("Витягуємо значення :",stack.peak())
        if menu == "8":
            stack.display()
        if menu == "9":
            print("До побачення! ")
            break






