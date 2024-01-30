class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):  # Додати елемент у хвіст списку
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):  # Додати елемент до списку на початок
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_data, new_data):  # Вставити новий елемент після елемента зі значенням target_data
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == target_data:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def delete_tail(self):  # Видалити елемент з хвоста списку
        current = self.head
        if not current:
            print("No data elements to delete")
        elif not current.next:
            self.head = None
        else:
            while current.next.next:
                current = current.next
            current.next = None

    def delete_head(self):  # Видалити елемент з голови списку
        if self.head:
            self.head = self.head.next
        else:
            print("No data elements to delete")

    def delete_by_value(self, target_data, count=1):  # Видалити елемент із деяким значенням у списку
        current = self.head
        prev = None
        deleted_count = 0
        while current and deleted_count < count:
            if current.data == target_data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                deleted_count += 1
            else:
                prev = current
            current = current.next

    def replace_value(self, old_value, new_value, replace_all=False):  # Замінити значення у списку
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                if not replace_all:
                    break
            current = current.next

    def size(self):  # Визначити розмір списку
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):  # Показати вміст списку
        current = self.head
        while current:
            print(current, end=" --> ")
            current = current.next
        print("None")

