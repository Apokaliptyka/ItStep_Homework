class UsernameDescriptor:
    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value: str):
        if not (4 <= len(value) <= 10 and value[0].isalpha() and value.isalnum()):
            raise ValueError("Помилка формату імені !!!")
        instance._username = value


class PasswordDescriptor:
    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if len(value) < 8:
            raise ValueError("Довжина паролю повинна бутибільше 8 символів!!")
        instance._password = value


class User:
    username = UsernameDescriptor()
    password = PasswordDescriptor()

    def __init__(self, username, password):
        self.username = username
        self.password = password


if __name__ == "__main__":
    user1 = User("k112345", "hjhh11111")
    user2 = User("f12388", "hjhh1jjj1")

    print(user1.username)
    print(user1.password)
    print(user2.username)
    print(user2.password)
