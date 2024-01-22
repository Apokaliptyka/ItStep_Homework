import re


class AccountDescriptor:
    data_email = []

    def __init__(self, prefix="_", min_length=0, max_length=0, key=0):
        self.prefix = prefix
        self.min_lenght = min_length
        self.max_lenght = max_length
        self.key = key

    def __set_name__(self, owner, name):
        self.var = self.prefix + name

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    def __set__(self, instance, value: str):
        symbol = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # перевірка username
        if self.key == 1:
            if self.min_lenght <= len(value) <= self.max_lenght:
                if value[0].isalpha():
                    for item in value:
                        if item not in symbol:
                            raise ValueError(f"Неправильний формат {self.var}")
                        setattr(instance, self.var, value)
                else:
                    raise ValueError(f"Неправильний формат{self.var}:перший символ повинен бути буквою!")
            else:
                raise ValueError(f"Кількість символів повинна бути від {self.min_lenght} до  {self.max_lenght}")
        # перевірка first_name i last_name
        if self.key == 2:
            if self.min_lenght <= len(value) <= self.max_lenght and value.isalpha():
                setattr(instance, self.var, value)
            else:
                raise ValueError(f"Помилка формату імені ")
        # перевірка password
        if self.key == 3:
            if self.min_lenght <= len(value) <= self.max_lenght:
                if value[0].isalpha():
                    setattr(instance, self.var, value)
                else:
                    raise ValueError(f"Неправильний формат{self.var}:перший символ повинен бути буквою!")
            else:
                raise ValueError(f"Кількість символів повинна бути від {self.min_lenght} до  {self.max_lenght}")
        # перевірка email
        if self.key == 4:
            if self.min_lenght <= len(value) <= self.max_lenght:  # перевірка на довжину
                result = re.match(email_pattern, value)
                if result:  # перевірка на правильність формату
                    if value in AccountDescriptor.data_email:  # перевірка на унікальність
                        raise ValueError(f" Такий емейл {value} вже існує!!")
                    setattr(instance, self.var, value)
                    AccountDescriptor.data_email.append(value)# збереження email в базу
                else:
                    raise ValueError("Неправильний формат емейла")


class User:
    username = AccountDescriptor("_", min_length=6, max_length=15, key=1)
    first_name = AccountDescriptor("__", 2, 16, 2)
    last_name = AccountDescriptor("__", 2, 16, 2)
    password = AccountDescriptor("_", 8, 23, 3)
    email = AccountDescriptor("_", 8, 20, 4)

    def __init__(self, username, first_name, last_name, password, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email


if __name__ == "__main__":
    user1 = User("andri_i", "Andrew", "Gapyuk", "jhjkhj1212121", "andrew@gmail.com")
    user2 = User("andri11i", "Max", "Gapyuk", "jhjkhj1212121", "andre1w@gmail.com")
    user3 = User("andrii", "Ira", "Gapyuk", "jhj89898989", "andrew2@gmail.com")
    user4 = User("andrii", "mark", "Gapyuk", "jhjkhj1212121", "andr4ew@gmail.com")
    print()
    print(user1.__dict__)
    print(user2.__dict__)
    print(user3.__dict__)
    print(user4.__dict__)
    print()
    print(AccountDescriptor.data_email)
