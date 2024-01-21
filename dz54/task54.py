from task52 import BankAccount


class NewBankAccount(BankAccount):

    def __init__(self, owner_name, account_number, balance, currency, max_limit, max_count_transactions):
        super().__init__(owner_name, account_number, balance, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.max_count = 0

    def withdraw(self, amount):
        try:
            if self._balance.amount < amount:
                raise ValueError("There are not enough funds in the account")
            if amount > self.max_limit:
                raise ValueError("Exceeded limit")
            if self.max_count_transactions <= self.max_count:
                raise ValueError("Exceeding the transaction limit")
            else:
                super().withdraw(amount)
                self.max_count += 1

        except ValueError as e:
            print(e)
        except TypeError as t:
            print("TypeError", t)

    def transfer_funds(self, target_account, amount):
        try:
            if target_account not in BankAccount.accounts:
                raise NameError(f"This account is not defined")
            if amount > self.max_limit:
                raise ValueError("Exceeded limit")
            if self.max_count_transactions <= self.max_count:
                raise ValueError("Exceeding the transaction limit")
            if self._balance.amount < amount:
                raise ValueError("Exchange rates are not available")

            else:
                super().transfer_funds(target_account,amount)
        except (KeyError, NameError, ValueError) as e:
            print(e)
            return f"Fund transfer failed: {e}"

    def add_percent(self, percent):
        self._balance.amount += self._balance.amount * (percent / 100)
        self.update_account_info_file()

if __name__=="__main__":

    g = NewBankAccount("Sara", "44444", 10000, "UAH", 1000, 2)
    g1 = NewBankAccount("Adam", "44448", 1500, "USD", 1000, 2)


    g.transfer_funds(g1, 900)
    g.transfer_funds(g1, 1500)

    g.display_account_info()
    g1.display_account_info()
