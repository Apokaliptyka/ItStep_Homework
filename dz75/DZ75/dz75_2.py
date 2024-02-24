from abc import ABC, abstractmethod
import json
import datetime


# Абстрактний клас створення масиву
class Array(ABC):
    @abstractmethod
    def create_array(self, string: str):
        pass


# клас створення масиву з клавіатури
class ArrayConsole(Array):

    def create_array(self, string: str):
        array = string.split(" ")
        return array


# клас створення масиву в файл для початкових даних
class ArrayByFile(Array):

    def __init__(self, filename):
        self.filename = filename

    def create_array(self, string: str):
        with open(self.filename, 'w') as f:
            for item in string:
                f.write(str(item))

    def read_arrry(self):
        with open(self.filename, "r") as file:
            arr = file.readlines()
            for el in arr:
                data = [item for item in el.split(" ")]

            return data


# Абстрактний для виведення масиву
class DisplayArray(ABC):

    @abstractmethod
    def output_array(self, array=None, filename=None):
        pass


# Клас виведення масиву в json
class JSONDisplay(DisplayArray):
    def output_array(self, filename=None, array=None):
        with open(filename, "w") as f:
            json.dump(array, f)


# Клас виведення масиву в txt
class TXTDisplay(DisplayArray):

    def output_array(self, filename=None, array=None):
        with open(filename, 'w') as f:
            for item in array:
                f.write(str(item) + " ")


# Клас виведення масиву в консоль
class ConsoleDisplay(DisplayArray):

    def output_array(self, array=None, filename=None):
        print(array)


# Абстрактний клас для сортування  масиву
class Sort(ABC):

    @abstractmethod
    def sort(self, arr: list):
        pass


# клас для сортування  масиву по зростанню
class SortBYHeight(Sort):

    def sort(self, arr: list):
        return sorted(arr, reverse=False)


# клас для сортування  масиву по спаданню
class SortBYReverse(Sort):

    def sort(self, arr: list):
        return sorted(arr, reverse=True)


# Абстрактний клас для додавання елементу в масив
class AddToArray(ABC):
    @abstractmethod
    def add_element(self, element, array=None):
        pass


# Абстрактний клас для видалення  елемента з масива
class DelWhithArray(ABC):
    @abstractmethod
    def delete_element(self, array=None):
        pass


#  клас для додавання   елемента на початок масиву
class AddTOBeginning(AddToArray):
    def add_element(self, element, array: list = None):
        array.insert(0, element)
        return array


#  клас для видалення  елемента з початоку масива
class DelWhithBeginning(DelWhithArray):

    def delete_element(self, array: list = None):
        array.remove(array[0])
        return array


# Абстрактний  клас для сповіщення
class NotificationCenter(ABC):

    @abstractmethod
    def notification(self):
        pass


# клас для сповіщення в консоль
class NotificationConsole(NotificationCenter):
    def notification(self):
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Список змінено в {now_time}")


#  клас для сповіщення в лог-файл
class NotificationLogFile(NotificationCenter):

    def notification(self):
        try:
            with open("log.json", "r") as file1:
                notification_dict = json.load(file1)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            notification_dict = {}

        info = "Update data"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notification_dict[now_time] = info

        with open("log.json", "w") as file2:
            json.dump( notification_dict, file2, indent=4)



# Абстрактний клас операції над масивом
class ArrayOperations(ABC):

    def __init__(self, array: list):
        self.array = array

    @abstractmethod
    def types_element(self):
        pass

    @abstractmethod
    def outputting_to_file(self, typefile: DisplayArray, filename: str):
        pass

    @abstractmethod
    def sort_array(self, metodsort: Sort):
        pass

    @abstractmethod
    def add_element(self, new_element, notification):
        pass

    @abstractmethod
    def remove_element(self, notification):
        pass

    @abstractmethod
    def count_elements(self, element):
        pass


#  інтерфейс для обчислення середнє арифметичне
class Avg(ABC):
    @abstractmethod
    def get_avg(self):
        pass


#  клас операції над масивом звичайним

class Operations(ArrayOperations):

    def types_element(self):
        first_type = type(self.array[0])
        for el in self.array:
            if not isinstance(el, first_type):
                return False
        return True

    def outputting_to_file(self, typefile: DisplayArray, filename=None):
        typefile.output_array(filename=filename, array=self.array)

    def sort_array(self, metodsort: Sort):
        self.array = metodsort.sort(self.array)
        return self.array

    def add_element(self, new_element, notification: NotificationCenter):
        self.array = AddTOBeginning().add_element(new_element, self.array)
        notification.notification()
        return self.array

    def remove_element(self, notification: NotificationCenter):
        self.array = DelWhithBeginning().delete_element(self.array)
        notification.notification()
        return self.array

    def count_elements(self, element):
        return self.array.count(element)


#  клас операції над масивом з числами
class OperationsWithNum(Operations, Avg):

    def get_avg(self):
        return sum(self.array) / len((self.array))


file = "file.txt"

d = "Learn online real native-level language learning"

# створення з клавіатури
console_list = ArrayConsole().create_array(d)
# print(console_list)

# створення з списку в файл
file_list = ArrayByFile("nun.txt")
file_list.create_array(d)
# витягуємо список з файлу
array_file = file_list.read_arrry()
# print(array_file)

# Типи файлів
txt_display = TXTDisplay()
json_display = JSONDisplay()
consol_display = ConsoleDisplay()
# Типи сортування
sort_h = SortBYHeight()
sort_d = SortBYReverse()
add = AddTOBeginning()
# типи сповіщення
consol_notification = NotificationConsole()
log_notification = NotificationLogFile()
# Операнд
operation = Operations(array_file)
# реалізація виводу масиву у вайли
operation.outputting_to_file(txt_display, "vyvidTXT.txt")
operation.outputting_to_file(json_display, "jsonfile.json")

# operation.outputting_to_file(consol_display)
# operation.sort_array(sort_h)
operation.outputting_to_file(consol_display)
# operation.sort_array(sort_d)
# operation.outputting_to_file(consol_display)
operation.outputting_to_file(json_display, "jsonfile.json")
# operation.add_element(12, consol_notification)
operation.add_element(14, log_notification)
operation.add_element(15, log_notification)
operation.outputting_to_file(consol_display)
operation.remove_element(log_notification)
operation.outputting_to_file(consol_display)
print("Перевірка на однотипність всіх елементів", operation.types_element())
print("Кількість елементів", operation.count_elements(12))
number = [1, 2, 3, 3, 3]
print("------------------------------------------------------------------------")
operation_num = OperationsWithNum(number)
print("Перевірка на однотипність всіх елементів", operation_num.types_element())
print("Кількість елементів", operation_num.count_elements(3))
print("Avg=", operation_num.get_avg())
