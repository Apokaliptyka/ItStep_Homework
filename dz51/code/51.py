class BankAccount:
    accounts = []

    def __init__(self, owner_name, account_number, balance):
        self.__account_number = account_number
        self._balance = balance
        self.owner_name = owner_name
        try:

            if self.__account_number not in [acc.__account_number for acc in BankAccount.accounts]:
                BankAccount.accounts.append(self)
            else:
                raise ValueError(" Your account number already exists ")
        except ValueError as e:
            print(e)

    def deposit(self, amount):
        self._balance = self._balance + amount

    def withdraw(self, amount):
        try:
            if self._balance >= amount:
                self._balance = self._balance - amount
            else:
                raise ValueError(" There are not enough funds in the account")

        except ValueError as e:
            print(e)
        except TypeError as t:
            print("TypeError", t)

    def change_owner_name(self, new_owner_name):
        self.owner_name = new_owner_name

    def display_account_info(self):
        print(f"Name:{self.owner_name}; account:{self.__account_number}; balance:{self._balance} ")

    def transfer(self, another_account, amount):
        try:
            if another_account not in BankAccount.accounts:
                raise NameError(f"This account is not defined")
            else:
                if self._balance >= amount:
                    self.withdraw(amount)
                    another_account.deposit(amount)
                else:
                    print("There are not enough funds in the account")
        except NameError as n:
            print(n)

    @staticmethod
    def check_account_number(account_number):
        return len(str(account_number)) == 5 and str(account_number).isdigit()

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        if new_account_number not in [acc.__account_number for acc in BankAccount.accounts] \
                and BankAccount.check_account_number(new_account_number):
            self.__account_number = new_account_number
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
        return sum([acc._balance for acc in cls.accounts]) / len(cls.accounts)


account1 = BankAccount("Jack", "12345", 500)
account2 = BankAccount("Alica", "12344", 1000)

print(BankAccount.get_average_balance())
