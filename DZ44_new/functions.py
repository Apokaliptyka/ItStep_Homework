import json
import string


def create_name():
    symbols = r'0123456789!#$%&()*+,-./:;<=>?@[\]^_{|}~"'
    while True:
        user_name = input("Введіть своє ім'я та прізвище : ")
        full_name = string.capwords(user_name)
        audit_name = ""
        for item in full_name:
            if item not in symbols:
                audit_name += item
        if audit_name == full_name:
            break
        print("Помилка формату імені! Повторіть спробу")
        print()
    return full_name


def create_email( data):
    sumbols = "abcdefghijklmnopqrstuvwxyz0123456789@."
    while True:
        email_user = input("Введіть свій email: ")
        unique_email = ""
        audit_email = ""

        for item in email_user:
            if item in sumbols:
                audit_email += item
        if len(data) > 0:
            for user in data:
                if user["email"] == email_user:
                    unique_email = email_user
        if audit_email == email_user and email_user.count("@") == 1 and len(unique_email) == 0:
            break
        else:
            print("Неправильний формат email або такий email уже існує! \nПеревірте та спробуйте ввести його знову!")
            print()
    return email_user


def create_password():
    while True:
        audit_password = ""
        password_user = input("""
(пароль повинен починатися з великої літери та містити від 8 до 16 символів!)
Введіть пароль: """)
        password_user2 = input("""
Повторно введіть пароль: """)
        if password_user != password_user2:
            print()
            print("Паролі не співпадають!")
        else:

            for item in password_user:
                if item in string.printable:
                    audit_password += item
            len_pass = len(password_user)

            if password_user[0] in string.ascii_uppercase and (
                    8 <= len_pass <= 16) and audit_password == password_user:
                break
            else:
                print()
                print("Неправильний формат паролю!")
    return password_user

def user_info(email):
    with (open("data.json", "r", encoding='utf-8') as file_data):
        data_users = json.load(file_data)
        info={}
        for user in data_users:
            if user["email"] == email:
                info=user
    return info
