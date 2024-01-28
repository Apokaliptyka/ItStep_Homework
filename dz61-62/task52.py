import requests
import json
import  os


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{round(self.amount,2)} {self.currency}"


class BankAccount:
    accounts = []
    __exchange_rate = {}
    data_folder = "data"

    def __init__(self, owner_name, account_number, amount, currency):
        self.__account_number = account_number
        self._balance = Money(amount, currency)
        self.owner_name = owner_name
        try:

            if self.__account_number not in [acc.__account_number for acc in BankAccount.accounts]:
                self.__class__.accounts.append(self)
            else:
                raise ValueError(" Your account number already exists ")
        except ValueError as e:
            print(e)
        # self.update_account_info_file()


    def update_account_info_file(self):
        with open(f"data/{self.__account_number}.json","w") as file:
            acount_info={}
            acount_info["Full name"]=self.owner_name
            acount_info["amount"]=self._balance.amount
            acount_info["currency"]=self._balance.currency
            json.dump(acount_info,file,indent=4)

    def deposit(self, amount):
        self._balance.amount += amount
        # self.update_account_info_file()


    def withdraw(self, amount):
        try:
            if self._balance.amount >= amount:
                self._balance.amount -= amount
                # self.update_account_info_file()
            else:
                raise ValueError("There are not enough funds in the account")
        except ValueError as e:
            print(e)
        except TypeError as t:
            print("TypeError", t)

    def change_owner_name(self, new_owner_name):
        self.owner_name = new_owner_name
        # self.update_account_info_file()

    def display_account_info(self):
        print(f"Name:{self.owner_name}; account:{self.__account_number}; balance:{self._balance} ")

    def transfer(self, another_account, amount):
        try:
            if another_account not in BankAccount.accounts:
                raise NameError(f"This account is not defined")
            else:
                if self._balance.amount >= amount and another_account._balance.currency == self._balance.currency:
                    self.withdraw(amount)
                    another_account.deposit(amount)
                    # self.update_account_info_file()
                else:
                    print("There are not enough funds in the account")
        except NameError as n:
            print(n)

    @staticmethod
    def check_account_number(account_number):
        return print(len(str(account_number)) == 5 and str(account_number).isdigit())

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        if new_account_number not in [acc.__account_number for acc in BankAccount.accounts] \
                and BankAccount.check_account_number(new_account_number):
            self.__account_number = new_account_number
            # self.update_account_info_file()
        else:
            print("Error: Incorrect account number!")

    @classmethod
    def find_account_by_owner(cls, owner_name):
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        return print(sum([acc._balance.amount for acc in cls.accounts]) / len(cls.accounts))

    def transfer_funds(self, target_account, amount):
        try:
            if target_account not in BankAccount.accounts:
                raise NameError(f"This account is not defined")

            else:
                rate_self = BankAccount.__exchange_rate[self._balance.currency]
                rate_target_account = BankAccount.__exchange_rate[target_account._balance.currency]
                if self._balance.amount >= amount:
                    if rate_self is not None and rate_target_account is not None:
                        new_amount = (amount * rate_self) / rate_target_account
                        self.withdraw(amount)
                        target_account.deposit(round(new_amount, 2))
                        # self.update_account_info_file()
                        return f"Fund transfer is successful"
                    else:
                        raise ValueError("Exchange rates are not available")
                else:
                    raise ValueError("There are not enough funds in the account")
        except (KeyError, NameError, ValueError) as e:
            print(e)
            return f"Fund transfer failed: {e}"

    @classmethod
    def create_exchange_rate(cls):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        info = requests.get(url)
        data = info.json()
        for item in data:
            carrency = item["cc"]
            rate = item["rate"]
            cls.__exchange_rate['UAH']=1
            cls.__exchange_rate[carrency] = rate


    @classmethod
    def delete_acount(cls,account_number):
        if account_number in [acc.__account_number for acc in cls.accounts]:
            for acc in cls.accounts:
                if account_number==acc.__account_number:
                    cls.accounts.remove(acc)
                    file_path = os.path.join(cls.data_folder, f"{account_number}.json")
                    if os.path.exists(file_path):
                        os.remove(file_path)


            return (f"Bank account {account_number} has been deleted.")
        else:
            return (f"Bank account with number {account_number} not found.")


BankAccount.create_exchange_rate()




