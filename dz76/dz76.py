from abc import ABC, abstractmethod
import datetime
import json

file_json_name="SaleReportHotDog.json"

# Абстрактний клас Склад
class WareHouse(ABC):
    """Клас Склад. Тут зберігаються інгредієнти та інше."""
    abstractwarehous = {}

    @abstractmethod
    def add_to_warehouse(self, name, count, prise):
        pass

    @abstractmethod
    def get_ingredientes(self):
        pass

# Склад харчових продуктів для виготовлення хот-догів
class FoodWareHouse(WareHouse):
    warehous = {} # Контейнер для збереження продуктів(назва,кількість,ціна)

    def add_to_warehouse(self, name:str, count:int, prise:float):
        self.warehous[name] = [count, prise]

    def get_ingredientes(self)->list:# отримуємо список інгредієнтів з яких отримуємо хот-дог
        data_ingredientes = [com for com in self.warehous.keys()]
        return data_ingredientes


food_warehouse = FoodWareHouse()
# Заповнюємо наш склад інгредієнтами
food_warehouse.add_to_warehouse("біла булка", count=15, prise=15)
food_warehouse.add_to_warehouse("сосиска", 30, 10)
food_warehouse.add_to_warehouse("кукурудза", 15, 15)
food_warehouse.add_to_warehouse("кетчуп", 30, 10)
food_warehouse.add_to_warehouse("майонез", 30, 10)
food_warehouse.add_to_warehouse("цибуля", 7, 15)
food_warehouse.add_to_warehouse("солоний огірок", 6, 15)
food_warehouse.add_to_warehouse("чилі", 6, 15)
food_warehouse.add_to_warehouse("гірчиця", 30, 10)
food_warehouse.add_to_warehouse("чорна булка", 10, 15)
food_warehouse.add_to_warehouse("капуста", 10, 10)

# Абстрактний склад для створення їжі
class Food(ABC):

    def __init__(self, food_name: str, warehouse: FoodWareHouse):
        self.food_name = food_name
        self.composition = []# контейнер(вміщує інгредієнти з яких складається продукт)
        self.ingredients = warehouse.warehous
        self.price = 0

    def __str__(self):
        return f"Name:{self.food_name}, prise:{self.get_price()} UAH \ncomposition:{self.composition}"

    @abstractmethod
    def create_food(self, composition: list):# Створення продукту
        pass

    @abstractmethod
    def add_indigridientes(self, indigrigient):# Додаємо інгредієнти до продукту
        pass

    @abstractmethod
    def del_indigridientes(self, indigrigient):# Видаляємо інгредієнти з продукту
        pass

    @abstractmethod
    def get_price(self):# Отримуємо ціну  продукту
        pass

    @abstractmethod
    def update_ingredients(self):# Оновлюємо залишок Складу після створення продукту
        pass

# Створюємо Хот-Дог
class HotDog(Food):

    def __init__(self, food_name: str, warehouse: FoodWareHouse):
        super().__init__(food_name, warehouse)
        self.create_food([])  # Виклик create_food для ініціалізації ціни

    def __str__(self):
        return f"Хот-дог:{self.food_name},ціна:{self.get_price()} грн \nсклад:{self.composition}"

    def create_food(self, components: list):
        price = 0
        remaining_ingredients = []

        for ing in components:
            if ing in self.ingredients.keys() and self.ingredients[ing][0] > 0:
                price_ing = self.ingredients[ing][1]
                price += price_ing
                remaining_ingredients.append(ing)
            else:
                print(f"Інгредієнта {ing} немає на залишку")
                return None
        self.composition = remaining_ingredients
        self.price = price  # Оновлення ціни
        return self.price, self.update_ingredients()

    def update_ingredients(self):
        for ing in self.composition:
            count = self.composition.count(ing)
            count_ing = self.ingredients[ing][0]
            update_count = count_ing - count
            self.ingredients[ing][0] = update_count
        return self.ingredients

    def add_indigridientes(self, ingredients: list):
        new_ingredients = []
        for i in ingredients:
            if i not in self.composition:  # Додавати тільки ті інгредієнти, яких немає вже у складі
                new_ingredients.append(i)
        self.composition.extend(new_ingredients)  # Додавання нових інгредієнтів
        self.create_food(self.composition)  # Виклик create_food з новими інгредієнтами

    def del_indigridientes(self, ingredients: list):
        for i in ingredients:
            if i in self.composition:
                self.composition.remove(i)
        self.create_food(self.composition)  # Виклик create_food зі списком без видалених інгредієнтів

    def get_price(self)->float:
        return self.price

# Створюємо продукт
hotdog_france = HotDog("France", food_warehouse)
hotdog_france.create_food(["біла булка", "сосиска", "кукурудза", "кетчуп", "майонез"])

hotdog_ukr = HotDog("Ukraine", food_warehouse)
hotdog_ukr.create_food(["чорна булка", "сосиска", "солоний огірок", "кетчуп", "майонез"])

hotdog_big = HotDog("BigHotDog", food_warehouse)
hotdog_big.create_food(
    ["біла булка", "сосиска", "кукурудза", "кетчуп", "майонез", "солоний огірок", "капуста", 'цибуля'])

# Абстрактний клас замовлення
class Order(ABC):

    def __init__(self):
        self.data_order = {}#контейнер де зберігається замовлення

    @abstractmethod
    def create_order(self, product:Food, count:int):# створює замовлення
        pass

    @abstractmethod
    def info_order(self):#виводить інформацію про  замовлення
        pass

    @abstractmethod
    def order_caculation(self):#підраховує  замовлення
        pass


class FoodOrder(Order):

    def create_order(self, product:Food, count: int)->dict:
        count_food = count
        full_price = 0
        while count:
            price_product = product.price
            full_price += price_product
            product.update_ingredients()
            count -= 1
        product_name = product.food_name
        self.data_order[product_name] = [count_food, full_price]
        return self.data_order

    def order_caculation(self)->float:
        cost_order = 0
        count_hotdog = sum(value[0] for value in self.data_order.values())
        summa_hotdog = sum(value[1] for value in self.data_order.values())
        if count_hotdog < 3:
            cost_order = summa_hotdog
        if 3 <= count_hotdog < 7:
            cost_order = self.sale(summa_hotdog, 10)
        if count_hotdog >= 7:
            cost_order = self.sale(summa_hotdog, 30)
        return cost_order

    def sale(self, summa: float, prosent: float) -> float:#розрахунок знижки
        cost = summa - (summa * (prosent / 100))
        return cost

    def info_order(self)->None:
        print("Ваше замовлення:")
        for item in self.data_order.keys():
            print(f"Хото-дог '{item}', кількість {self.data_order[item][0]}шт. сума {self.data_order[item][1]} грн")
        summa_hotdog = sum(value[1] for value in self.data_order.values())
        print(f"Знижка: {summa_hotdog - self.order_caculation()} грн ")
        print(f"Загальна сума: {self.order_caculation()} грн")

    def clean(self)->dict:
        self.data_order = {}
        return self.data_order


order = FoodOrder()

#Звіт продаж
class SalesReport(ABC):

    @abstractmethod
    def process_sals_reports(self, order: Order,filename:str):
        pass
#Відкривання файлів
class OpenFile(ABC):
    @abstractmethod
    def open_file(self,filename:str):
        pass
#Відкривання файлу Json
class OpenJsonFile(OpenFile):
    def open_file(self,filename:str)->dict:
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        return data
#Створення звіту та чеку
class SaleReportHotDog(SalesReport):

    def process_sals_reports(self, order: FoodOrder,filename:str)->None:
        now_data = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        data=OpenJsonFile().open_file(filename)
        key = now_data
        data_order = []
        for item in order.data_order.keys():
            product_name = item
            count = order.data_order[product_name][0]
            summa = order.data_order[product_name][1]
            data_order.append({"name": product_name, "count": count, "summa": summa})
        summa_all = order.order_caculation()
        data_order.append({"summa_all": summa_all})
        data[key] = data_order

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        self.create_check(order)

    def create_check(self, order: FoodOrder)->None:
        check_data = {}
        now_data = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        with open(fr"checkes\{now_data}.json", "w") as file:
            key = now_data
            check = order.data_order
            summa = order.order_caculation()
            check_data[key] = [check, summa]
            json.dump(check_data, file)

#Інтерфейс для роботи із звітами
class WorkWithReport(ABC):
    @abstractmethod
    def get_total_amount_sales(self,filename:str):#кількість продукції та їх суми продаж
        pass

    @abstractmethod
    def get_total_product(self,filename:str):#загальна сума продаж
        pass

#Робота над звітами по продажах Хот-Догів
class WorkReportHotDog(WorkWithReport):

    def get_total_product(self,filename:str)->float:

        data = OpenJsonFile().open_file(filename)
        total_sum = 0
        for key, value in data.items():
            for item in value:
                if 'summa_all' in item:
                    total_sum += item['summa_all']
        return total_sum

    def get_total_amount_sales(self,filename)->dict:
        data = OpenJsonFile().open_file(filename)
        product_count = {}
        for key, value in data.items():
            for item in value:
                if 'name' in item and 'count' in item:
                    product_name = item['name']
                    product_count[product_name] = product_count.get(product_name, 0) + item['count']
        return product_count


food_repord = WorkReportHotDog()

chech = SaleReportHotDog()


#Абстрактний клас оплати
class Payments(ABC):
    @abstractmethod
    def process_payments(self, money: float, cost: Order)->bool:
        pass

#Оплата готівкою
class CashPayments(Payments):
    def process_payments(self, money: float, cost: FoodOrder)->bool:
        cost = cost.order_caculation()
        print("Розрахунок готівкою обробляється ")
        if money < cost:
            print("Недостатньо грошей для здійснення операції")
            return False
        print(f"Ваша решта {money-cost} грн")
        print("Розрахунок успішний!")
        return True

#Оплата карткою
class CardPayments(Payments):
    def process_payments(self, money: float, cost: FoodOrder)->bool:
        cost = cost.order_caculation()
        print("Розрахунок готівкою обробляється ")
        if money < cost:
            print("Недостатньо грошей для здійснення операції")
            return False
        print("Розрахунок успішний!")
        return True


card_payment = CardPayments()
cash_payment = CashPayments()


