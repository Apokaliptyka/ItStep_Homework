import json


def deleted_user_data(user_index):
    with open("data.json", "r", encoding="utf-8") as file_users:
        data_users = json.load(file_users)

        data_users.pop(user_index)
        print("Обліковий запис видалено!")
    with open("data.json", "w",encoding="utf-8") as file_data:
        json.dump(data_users, file_data, indent=4, ensure_ascii=False)
