from  task56 import UpBankAccount

acount1 = UpBankAccount("Sara", "44444", 1000, "USD", 1000, 2)
acount2 = UpBankAccount("Adam", "44448", 1000, "EUR", 1000, 2)
print("1)Порівняння двох рахунків:", acount1==acount2)
print("2)Порівняння у гривнях",acount1>acount2)
print("3) Баланс додатній? ",acount1.__bool__())
print("4) Баланс ціле число ?",acount1.__float__())
print(id(acount1))
acount1+10
acount1.display_account_info()
print(id(acount1))
acount1-1000
acount1.display_account_info()
acount1-600
acount1.display_account_info()
acount1(20000)
acount1(-19000)
acount1()