from dz76 import hotdog_ukr, hotdog_big, hotdog_france, card_payment, cash_payment
from dz76 import food_warehouse, order, chech,food_repord,file_json_name

print("Hello")
while True:

    menu = input("""
    Оберіть дію:
    1. Замовити хот-дог
    2. Увійти як адміністратор
    3. Вихід 
Зробіть свій вибір: """)

    if menu == "1":
        while True:
                create_product = input(f"""
                Оберіть хот-дог:
                
                1.Хот-дог 'Французький' ціна:{hotdog_france.get_price()} грн, склад: {hotdog_france.composition}
                2.Хот-дог 'Український' ціна:{hotdog_ukr.get_price()} грн, склад: {hotdog_ukr.composition}
                3.Хот-дог 'Подвійний Супер' ціна:{hotdog_big.get_price()} грн, склад: {hotdog_big.composition}
    Зробіть свій вибір: """)
                if create_product == "1":
                    product = hotdog_france
                    print("Ви обрати ", hotdog_france)
                if create_product == "2":
                    product = hotdog_ukr
                    print("Ви обрати ", hotdog_ukr)
                if create_product == "3":
                    product = hotdog_big
                    print("Ви обрати ", hotdog_big)
                add_ingridient = input("""
                Бажаєте додати інгредієнти??? 
                1. Так
                2. Ні 
    Зробіть свій вибір: """)
                if add_ingridient == "1":
                    data_composition = input(f"""
                        Напишіть через кому інгредієнти які хочете добавити у хот-дог.
                         Оберіть варіанти із списку 
                        {food_warehouse.get_ingredientes()}
    Зробіть свій вибір """).split(",")
                    product.add_indigridientes(data_composition)
                    print("Ваш", product)

                count_product = int(input("""Введіть кількість хот-догів: """))
                order.create_order(product, count_product)
                order.info_order()
                contin_order = input("""
                Бажаєте ще замовти?
                1 Так
                2 Ні
    Оберіть варіант: """)
                if contin_order == "1":
                    continue

                order.info_order()
                payment = input("""
                Оберіть спосіб оплати :
                1. Карта
                2. Готівка
Зробіть свій вибір:  """)
                flag = True
                input_cash = int(input("Введіті суму: "))
                if payment == "1":
                    if card_payment.process_payments(input_cash, order) is False:
                        flag = False
                if payment == "2":
                    if cash_payment.process_payments(input_cash, order) is False:
                        flag = False
                if flag == True:
                    chech.process_sals_reports(order,file_json_name)
                    order.clean()
                    print("Дякуємо за покупку.Допобачення!")

                break

    if menu == "2":
        while True:
            admin_menu=input("""
            1.Звіт по кількості проданих хот-догів
            2 Загальна сума продаж
            3 Залишок на складі
            4 Вихід
Зробіть свій вибір : """)
            if admin_menu=="1":
                print(food_repord.get_total_amount_sales(file_json_name))
                continue
            if admin_menu=="2":
                print(food_repord.get_total_product(file_json_name))
                continue
            if admin_menu=="3":
                print(food_warehouse.warehous)
                continue
            if admin_menu=="4":
                break

    if menu == "3":
        print("Дякуємо.Допобачення!")
        break
