from task62 import LinkedList

linked_list = LinkedList()
while True:

    menu = input(""" Оберіть свій варіант:
1.	Додати елемент у хвіст списку 
2.	Додати елемент до списку на початок
3.	Вставити новий елемент із деяким значенням безпосередньо після елемента із даними, що є у списку.  
4.	Видалити елемент з хвоста списку
5.	Видалити елемент з голови списку
6.	Видалити елемент із деяким значенням у списку . 
7.	Замінити значення у списку на нове значення 
8.	Визначте розмір списку
9.	Показати вміст списку (прохід по всьому списку).
10. Вихід
 Введіть варіант: """)

    if menu == "1":
        data = int(input("Введіть значення:"))
        linked_list.append(data)
        print(f"Вузол створено")
    if menu == "2":
        data = int(input("Введіть значення:"))
        linked_list.prepend(data)
        print(f"Вузол створено")
    if menu == "3":
        target_data = int(input("Введіть значення перед яким хочете вставити:"))
        new_data = int(input("Введіть нове значення:"))
        linked_list.insert_after(target_data, new_data)
        print(f"Вузол створено")
    if menu == "4":
        linked_list.delete_tail()
        print(f"Вузол з хвоста видалено")
    if menu == "5":
        linked_list.delete_head()
        print(f"Вузол з голови видалено")
    if menu == "6":
        data = int(input("Введіть значення:"))
        count = int(input("Введіть кількість:"))
        linked_list.delete_by_value(data, count)
        print(f"Вузол  видалено")
    if menu == "7":
        old_value = int(input("Введіть старе значення :"))
        new_value = int(input("Введіть нове значення:"))
        replace_all = (input("""Змінити всі значення ?:"
  1. Так
  2. Ні 
Введіть варіант: """))
        if replace_all == "1":
            linked_list.replace_value(old_value, new_value, replace_all=True)
            print(f"Значення змінені !!")

        elif replace_all == "2":
            linked_list.replace_value(old_value, new_value, replace_all=False)
            print(f"Значення змінені !!")
        else:
            print("Невірний варіант!!")

    if menu == "8":
        print("Розмір списку:", linked_list.size())

    if menu == "9":
        linked_list.display()
    if menu == "10":
        print("Допобачення")
        break
