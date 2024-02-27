import json
from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self,indeficator, name,catalog,price,count):
        self.name = name
        self.catalog = catalog
        self.price = price
        self.indeficator=indeficator
        self.product={}
        self.count=count

    @abstractmethod
    def info(self, display_metod):
        pass

class Output(ABC):

    @abstractmethod
    def display(self,product:Product):
        pass

# Клас створення картки товару
class ProductCart(Product):

    def __init__(self,indeficator, name:str, catalog:str, price:float,count=1):
        super().__init__(indeficator, name, catalog, price,count)
        self.product = {"артикул":self.indeficator,
                        "назва":self.name,
                        "категорія":self.catalog,
                        "ціна":self.price,
                        "кількість":self.count
                        }


    def info(self, display_metod:Output):
        display_metod.display(self)


# Клас для виведення інформації про товар
class ConsolOutput(Output):

    def display(self,product:Product):
        for key,value in product.product.items():
            print(f"{key}:{value}")


class FileOutput(Output):
    def __init__(self,catalog):
        self.catalog=catalog


    def display(self,product:Product):
        filename=product.name
        with open(fr"{self.catalog}\{filename}","w",encoding="utf-8") as file:
            json.dump(product.product,file,indent=4,ensure_ascii=False)


# Клас бази даних
class DataBase(ABC):

    def __init__(self,file_name:str):
        self.file_name=file_name

    @abstractmethod
    def update_database(self,object):
        pass
    @abstractmethod
    def open_database(self):
        pass
# База даних в Json
class JsonBase(DataBase):
    def __init__(self,file_name:str):
        super().__init__(file_name)

    def open_database(self):
        try:
            with open(self.file_name, "r",encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = []
        return data

    def update_database(self,object:Product):
        data = self.open_database()
        found = False
        for cart in data:
            if str(cart.get("артикул")) == str(object.indeficator):
                cart.update(object.product)
                found = True
                break
        if not found:
            data.append(object.product)
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


# Склад
class WareHous(ABC):

    def __init__(self,database:DataBase):
        self.database=database


    @abstractmethod
    def add_product(self, indeficator, name, catalogy, price,count):
        pass

    @abstractmethod
    def del_product(self, indeficator):
        pass

    @abstractmethod
    def update_price(self, indeficator, new_price):
        pass

    @abstractmethod
    def find_product(self, indeficator):
        pass

    @abstractmethod
    def output_all_products_whith_catal(self, catalog):
        pass

    @abstractmethod
    def total_count_products(self):
        pass

    @abstractmethod
    def total_cost_catagory(self, catagory):
        pass

    @abstractmethod
    def total_all_cost_products(self):
        pass

# Склад готової продукції(робота із складом)
class FoodWareHous(WareHous):

    def __init__(self,database):
        super().__init__(database)


    def add_product(self, indeficator, name, catalogy, price,count):
        new_product=ProductCart(indeficator,name,catalogy,price,count)
        self.database.update_database(new_product)



    def del_product(self, indeficator):
        data=self.database.open_database()
        card_product=self.find_product(indeficator)
        data.remove(card_product)
        with open(self.database.file_name, "w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)


    def update_price(self, indeficator, new_price):
        card_product = self.find_product(indeficator)
        if card_product:
            product = ProductCart(indeficator=card_product["артикул"],
                                  name=card_product["назва"],
                                  catalog=card_product["категорія"],
                                  price=new_price,
                                  count=card_product["кількість"])
            self.database.update_database(product)
        else:
            print("Product not found.")


    def find_product(self, indeficator):
        data = self.database.open_database()
        for card in data:
            if card["артикул"] == indeficator:
                return card


    def output_all_products_whith_catal(self, catagory):
        data = self.database.open_database()
        all_product=[]
        for product in data:
            if product['категорія']==catagory:

                all_product.append(product)
        return all_product



    def total_count_products(self):
        data = self.database.open_database()
        print("Загальна кількість карток товарів",len(data),"шт")

    def total_cost_catagory(self, catagory):

        lst_category=self.output_all_products_whith_catal(catagory)
        return self.calculation_cost(lst_category)


    def calculation_cost(self,data:list):
        total_category = 0
        for card in data:
            price = card["ціна"]
            count = card["кількість"]
            summa = price * count
            total_category += summa
        return total_category

    def total_all_cost_products(self):
        data = self.database.open_database()
        return self.calculation_cost(data)

#Створюємо карточку товару
banana=ProductCart(indeficator="12345",name="Банан",catalog="Фрукти",price=74)
orange=ProductCart(indeficator="13444",name="Апельсин",catalog="Фрукти",price=99)


#Папка де будуть виводитися  картки товарів у файли
name_catalog_for_food_cart="productcart"
#Метод виведення у консоль
consol_output=ConsolOutput()
#Метод виведення у файл
file_output=FileOutput(name_catalog_for_food_cart)
#Виводимо інформацію карток
banana.info(consol_output)
banana.info(file_output)
orange.info(consol_output)
orange.info(file_output)
#Створюємо базу даних і зберігаємо там картки
jsonbase=JsonBase("database.json")
jsonbase.update_database(banana)
jsonbase.update_database(orange)

#Склад Харчових продуктів
food_warehouse=FoodWareHous(database=jsonbase)
#Додаємо новий продукт
food_warehouse.add_product("66666","Помідора","Овочі",66,count=8)
# food_warehouse.del_product("66666")  #Видаляємо продукт
print(food_warehouse.find_product("66666"))#Знаходимо продукт за артиклом
food_warehouse.update_price("66666",90)#Змінюємо ціну
for i in food_warehouse.output_all_products_whith_catal("Фрукти"):
        print(i)#Виводимо всі товари із каталогу
food_warehouse.total_count_products()# Виводимо загальну кількість створених продуктів
print(food_warehouse.total_cost_catagory("Фрукти"))#Виводимо на яку суму є товарів в каталозі
print(food_warehouse.total_all_cost_products())#Виводимо загальну суму товарів в магазині

