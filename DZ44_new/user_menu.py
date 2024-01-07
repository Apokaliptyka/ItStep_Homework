from change_data import change_user_data
from dell_data import deleted_user_data
import json


def menu_user(login):
    with open("data.json", "r", encoding="utf-8") as file_users:
        data_users = json.load(file_users)
        user_index = 0
        for user in data_users:
            if user["email"] == login:
                user_index = data_users.index(user)
    while True:
        user_menu = input("""
        Меню користувача:
    
                        1.Зміна облікових даних
                        2.Видалення облікового запису
                        3.Повернутися на головну сторінку
        Введіть варінт: """)
        if user_menu == "1":
            change_user_data(data_users, user_index)
        if user_menu == "2":
            deleted_user_data(user_index)
            break
        if user_menu == "3":
            break
