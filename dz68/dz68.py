from abc import ABC, abstractmethod


class BinarySearchTree(ABC):
    def __init__(self, root=None):
        self.root = root

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def find_min(self):
        pass

    @abstractmethod
    def search(self, value):
        pass


class Node:
    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return f"Noda {self.data}"


class MyBinarySearchTree(BinarySearchTree):

    def insert(self, value: int):  # Вставка нового елемента
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node, value: int):  # Рекрусивна функція
        if value < node.data:  # Рух у лівий бік піддерева
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.data:  # Рух у правий бік піддерева
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def post_order(self, node: Node):  # Виведення дерева на екран
        if node is not None:
            self.post_order(node.left)
            print(node, end="-->")
            self.post_order(node.right)

    def remove(self, value: int):  # Функція видалення
        self.root = self.remove_node(self.root, value)

    def remove_node(self, root: Node, value: int):  # Рекрусивна функція для видалення
        if root is None:
            return root

        # Знаходимо вузол, який потрібно видалити
        if value < root.data:
            root.left = self.remove_node(root.left, value)
        elif value > root.data:
            root.right = self.remove_node(root.right, value)
        else:  # Знайшли вузол, який потрібно видалити
            # Випадок 1: вузол має один або жодного нащадка
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Випадок 2: вузол має двох нащадків
            # Знаходимо найменший вузол в правому піддереві
            temp = self.find_recursive(root.right, flag=True)
            # Копіюємо значення найменшого вузла в поточний вузол
            root.data = temp.data
            # Видаляємо найменший вузол з правого піддерева
            root.right = self.remove_node(root.right, temp.data)

        return root

    def find_min(self):  # Функція знаходження мінімального вузла
        min_node = self.find_recursive(self.root, flag=True)
        return min_node if min_node else None

    def find_recursive(self, node: Node, value=None, flag=None):  # Рекрусивна функція пошуку
        if node is not None:
            if node.left == None and flag:  # Знаходження мінімального значення
                return node
            if node.data == value and not flag:  # Почук за значенням
                return node
            left_result = self.find_recursive(node.left, value, flag)
            right_result = self.find_recursive(node.right, value, flag)
            return left_result or right_result

    def search(self, value: int):  # Функція пошуку за значенням
        result = self.find_recursive(self.root, value, False)
        return result if result else f"Такого значення немає в дереві!"


if __name__ == "__main__":

    tree = MyBinarySearchTree()

    data = [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]
    for item in data:
        tree.insert(item)
    tree.post_order(tree.root)
    print()
    print("Мінімальне значення в дереві :", tree.find_min().data)

    print("Пошук елемента:", tree.search(11))
    tree.remove(11)
    tree.remove(10)
    tree.remove(12)
    tree.post_order(tree.root)
    print()
    print("Мінімальне значення в дереві :", tree.find_min().data)
    print("Пошук елемента:", tree.search(11))
