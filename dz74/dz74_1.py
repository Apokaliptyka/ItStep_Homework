from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass


class Product(Component):

    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = price

    def execute(self) -> float:
        return self.__price


class Category(Component):

    def __init__(self, name: str):
        self.name = name
        self.__children = []

    def add(self, comp: Component) -> None:
        return self.__children.append(comp)

    def remove(self, comp: Component) -> None:
        return self.__children.remove(comp)

    def get_children(self):
        return self.__children

    def execute(self):
        cost = 0
        for component in self.__children:
            cost_component = component.execute()
            cost += cost_component
        return cost


class Store(Component):
    def __init__(self):
        self.data_store = []

    def add(self, category: Category, comp: Component):
        if category not in self.data_store:
            self.data_store.append(category)
        category.add(comp)

    def execute(self):
        if len(self.data_store) == 0:
            return "Магазин порожній"
        else:
            cost_max = self.data_store[0].execute()
            return cost_max


if __name__ == '__main__':
    store = Store()

    catalog1 = Category("box1")
    catalog2 = Category("box2")
    catalog3 = Category("box3")
    catalog4 = Category("box4")
    p1 = Product("Lg Smart", 200)
    p2 = Product("Iphone 15", 200)
    p3 = Product("Samsung 14", 200)
    p4 = Product("Banana", 200)

    store.add(catalog1, p1)
    store.add(catalog1, catalog2)
    store.add(catalog2, p2)
    store.add(catalog2, catalog3)
    store.add(catalog2, p3)
    store.add(catalog3, p4)
    store.add(catalog3, catalog4)
    print(catalog1.execute())
    print(store.execute())
    catalog3.remove(p4)
    print(catalog1.execute())
    print(store.execute())
