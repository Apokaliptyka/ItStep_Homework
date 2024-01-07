import json

from regist import create_name, create_password, create_email


def change_user_data(data_users, user_index):
    with open("data.json", "r", encoding="utf-8") as file_users:
        data = json.load(file_users)


        while True:
            change_nemu = input(""" Оберіть дію:
            1.Зміна імені
            2.Зміна Email
            3.Зміна паролю
            4.Зберегти та вийти
            Зробіть свій вибір:  """)



            if change_nemu == "1":
                data_users[user_index]["full name"] = create_name()
                print("Зміни успішні!")
            if change_nemu == "2":
                data_users[user_index]["email"] = create_email(data_users)
                print("Зміни успішні!")
            if change_nemu == "3":
                data_users[user_index]["password"] = create_password()
                print("Зміни успішні!")
            if change_nemu == "4":
                print("Зміни збережено!")
                break

        for k, v in data_users[user_index].items():
            print(k, v)
    with open("data.json", "w", encoding="utf-8") as file_data:
        json.dump(data_users, file_data, indent=4, ensure_ascii=False)
