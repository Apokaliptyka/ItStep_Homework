class Node:
    def __init__(self, id, name, priority=None):
        self.next = None
        self.name = name
        self.id = id
        self.priority = priority

    def __str__(self):
        return f"Task№{self.id}: {self.name},prioryty-->{self.priority}"


class Queue:

    def __init__(self):
        self.head = self.tail = None
        self.__size = 0
        self.comp_task_size=0

    def enqueue(self, id, name, priority):
        new_noda = Node(id, name, priority)
        current = self.head
        if not self.head:
            self.head = self.tail = new_noda
        else:
            while current:

                if new_noda.priority < self.head.priority:
                    new_noda.next = self.head
                    self.head = new_noda
                    break
                if current.priority == new_noda.priority:
                    new_noda.next = current.next
                    current.next = new_noda
                    break
                if current.priority > self.head.priority and new_noda.priority < current.priority:
                    new_noda.next = self.head.next
                    self.head.next = new_noda
                    break
                if self.tail.priority < new_noda.priority:
                    self.tail.next = new_noda
                    self.tail = new_noda
                    break
                current = current.next
        self.__size +=1


    def dequeue(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            temp = self.head
            self.head = self.head.next
            self.__size-=1
            self.comp_task_size+=1
            if self.__size==0:
                self.tail=None
            return temp

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        if self.head==None:
            return True

    def display(self):  # Показати вміст списку
        current = self.head
        while current:
            print(f"Task№{current.id}: {current.name},prioryty-->{current.priority}", end="\n")
            current = current.next
    def completed_tasks(self):
        return self.comp_task_size


queue = Queue()
queue.enqueue(1, "Підготувати звіт про продажі", 3)
queue.enqueue(2, "Відправити заказ клієнту A", 1)
queue.enqueue(3, "Сформувати презентацію для команди", 3)
queue.enqueue(4, "Зателефонувати постачальнику щодо поставки товару", 2)
queue.enqueue(5, "Відправити заказ клієнту B", 1)
queue.enqueue(6, "Замовити нове обладнання для офісу.", 2)
print(queue.size)

print("Completed task",queue.comp_task_size)
print(queue.dequeue())
print(queue.dequeue())
print("Completed task",queue.comp_task_size)
print("Size is ",queue.size)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print("Completed task",queue.comp_task_size)
print(queue.dequeue())
print("Size is ",queue.size)
print("Is empty? ",queue.is_empty())
