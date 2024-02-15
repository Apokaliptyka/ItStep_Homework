from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass


class OrderFood(Order):
    def process_order(self):
        print("Замовлення на їжу обробляється !")


class OrderDrink(Order):
    def process_order(self):
        print("Замовлення на напої обробляється !")


class Payments(ABC):
    @abstractmethod
    def process_payments(self):
        pass


class CashPayments(Payments):
    def process_payments(self):
        print("Розрахунок готівкою обробляється ")


class CardPayments(Payments):
    def process_payments(self):
        print("Розрахунок картою обробляється ")


class SalesReport(ABC):
    @abstractmethod
    def process_sals_reports(self):
        pass


class JsonSalesReport(SalesReport):
    def process_sals_reports(self):
        print("Звіт в форматі JSON обробляється ")


class CswSalesreport(SalesReport):
    def process_sals_reports(self):
        print("Звіт в форматі CSW обробляється ")


class AbstractFactory(ABC):
    @abstractmethod
    def create_order(self):
        pass

    @abstractmethod
    def create_payment(self):
        pass

    @abstractmethod
    def create_sales_report(self):
        pass


class FoodFactory(AbstractFactory):
    def create_order(self):
        return OrderFood()

    def create_payment(self):
        return CardPayments()

    def create_sales_report(self):
        return JsonSalesReport()


class DrintFactory(AbstractFactory):
    def create_order(self):
        return OrderDrink()

    def create_payment(self):
        return CashPayments()

    def create_sales_report(self):
        return CswSalesreport()


class Client:

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def place_order(self):
        order = self.factory.create_order()
        order.process_order()

    def make_payment(self):
        payment = self.factory.create_payment()
        payment.process_payments()

    def generate_sales_report(self):
        sales_report = self.factory.create_sales_report()
        sales_report.process_sals_reports()

client_1=Client(FoodFactory())
client_1.place_order()
client_1.make_payment()
client_1.generate_sales_report()