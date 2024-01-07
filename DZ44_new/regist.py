import json

from functions import create_name, create_email, create_password, user_info


def register_user():
    with (open("data.json", encoding='utf-8') as file_data):
        data_users = json.load(file_data)

        user_data = {}
        id_user = 1
        if len(data_users) > 0:
            id_user = data_users[-1]["id"] + 1
        user_data['id'] = id_user
        user_data['full name'] = create_name()
        user_data['email'] = create_email(data_users)
        user_data['password'] = create_password()
        data_users.append(user_data)

    with open("data.json", "w", encoding='utf-8') as file_data:
        json.dump(data_users, file_data, indent=4, ensure_ascii=False)
        print()
        print("""
      Ласкаво просимо !
Реєстрація пройшла  успішно ! 
 """)

# register_user()
