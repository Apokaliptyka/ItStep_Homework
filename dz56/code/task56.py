from task54 import NewBankAccount
from task52 import BankAccount


class UpBankAccount(NewBankAccount):

    def __eq__(self, other):
        if isinstance(other, UpBankAccount):
            return self._balance.currency == other._balance.currency and \
                self._balance.amount == other._balance.amount

    def __lt__(self, other):
        try:
            if isinstance(other, UpBankAccount):
                rate_self = BankAccount._BankAccount__exchange_rate.get(self._balance.currency)
                rate_other = BankAccount._BankAccount__exchange_rate.get(other._balance.currency)
                amount_self = self._balance.amount * rate_self
                amount_other = other._balance.amount * rate_other
                return amount_self < amount_other
        except TypeError:
            return ("Помилка при конвертації: такої валюти не існує.")

    def __bool__(self):
        return self._balance.amount > 0

    def __float__(self):
        return type(self._balance.amount) is float

    def __add__(self, amount):
        self._balance.amount += amount
        self.update_account_info_file()
        return self

    def __sub__(self, amount):
        if self._balance.amount >= amount:
            self._balance.amount -= amount
            self.update_account_info_file()
            return self
        else:
            self._balance.amount -= amount
            self.update_account_info_file()
            print(f"Ваша заборгованість складає {self._balance.amount} {self._balance.currency}")
            return self

    def __call__(self, value=0):
        if value>0:
            self.__add__(value)
            print(f"Ваш рахунок поповнено на суму {value} {self._balance.currency}."
                  f"Ваш баланс становить: {self._balance.amount} {self._balance.currency} ")
            self.update_account_info_file()
            return self
        elif value<0:
            self.__sub__(abs(value))
            print(f"З вашого рахунку знято кошти на суму {value} {self._balance.currency}."
                  f"Ваш баланс становить: {self._balance.amount} {self._balance.currency} ")
            self.update_account_info_file()
            return self
        else:
            print( f"Ваш баланс становить: {self._balance.amount} {self._balance.currency} ")
            self.update_account_info_file()
            return self




