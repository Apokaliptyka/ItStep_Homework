class Noda:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node({self.data})"


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):  # Додавання в хвіст
        new_noda = Noda(data)
        if self.head is None:
            self.head = new_noda
            new_noda.prev = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_noda
            new_noda.prev = current

    def prepend(self, data):  # Додати елемент до списку на початок
        new_node = Noda(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        new_node.prev = None
        self.head = new_node

    def delete_tail(self):  # Видалити елемент з хвоста списку
        current = self.head
        if not current:
            print("Немає елементів для видалення")
        elif not current.next:
            self.head = None
        else:
            while current.next.next:
                current = current.next
            current.next = None

    def delete_head(self):  # Видалити елемент з голови списку
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            print("Немає елементів для видалення")

    def delete_by_value(self, target_data, count=1):  # Видалити елемент із деяким значенням у списку
        current = self.head
        prevent = None
        deleted_count = 0
        while current and deleted_count < count:
            if current.data == target_data:
                if prevent:
                    prevent.next = current.next
                    if current.next:
                        current.next.prev = prevent
                else:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                deleted_count += 1
            else:
                prevent = current
            current = current.next

    def insert_after(self, index, new_data):  # •	Додавання нового елемента за індексом
        new_node = Noda(new_data)
        current = self.head
        current_index = 1
        if index == 1:
            self.prepend(new_data)
        while current:
            current_index += 1
            if current_index == index:
                new_node.next = current.next
                current.next.prev = new_node
                new_node.prev = current
                current.next = new_node
                break
            current = current.next

    def display(self):  # Показати вміст списку  голови до хвоста
        current = self.head
        print("None <--", end="\t")
        while current:
            print(current, end=" <----> ")
            current = current.next
        print("None")

    def display_reverse(self):  # Показати вміст списку від хвоста до голови
        current = self.head
        while current and current.next:
            current = current.next
        print("None<--", end="\t")
        while current:
            print(current, end=" <----> ")
            current = current.prev
        print("None")

    def cleaning(self):
        self.head=None
        print("Список очищений")


if __name__ == "__main__":
    list = LinkedList()
    list.prepend(900)
    list.prepend(9888)
    list.prepend(1000)
    list.append(500)
    list.display()
    list.delete_head()
    list.display()
    list.insert_after(2, 800)
    list.display()
    list.insert_after(1, 700)
    list.display()
    list.insert_after(5, 600)
    list.display()
    list.display_reverse()
    list.cleaning()
    list.prepend(900)
    list.prepend(900)
    list.prepend(900)
    list.prepend(9888)
    list.prepend(1000)
    list.append(500)
    list.display()
    list.delete_head()
    list.display()
    list.delete_tail()
    list.delete_by_value(900, 3)
    list.display()
    list.delete_by_value(9888, 5)
    list.display()
