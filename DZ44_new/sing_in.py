import json


def sing_in(email_user, password):
    with open("data.json", "r") as file_users:
        data_users = json.load(file_users)
        result = ""

        flag = False
        for user in data_users:
            if user["email"] == email_user and user["password"] == password:
                result = "Вхід успішний"
                print(result)
                flag = True
        if flag == False:
            result = "User not found"

    return result

# sing_in("hgjhghjg@gh","Dfffffffff")


# sing_in()
