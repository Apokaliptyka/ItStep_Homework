import os
import json
import datetime
from abc import ABC,abstractmethod

# Абстрактний клас, що надає доступ до набору чисел
class NumberSet(ABC):
    @abstractmethod
    def get_numbers(self):
        pass

# Реальний суб'єкт, який представляє файл з набором чисел
class FileNumberSet(NumberSet):
    data_summa=[]
    def __init__(self, filename):
        self.filename = filename

    # Метод який повертає останнє число з файла
    def get_numbers(self):
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    data = file.readlines()
                    if len((data))==0:
                        return None
                    else:
                        for x in data:# Запис суми числа в контейнер
                            summa = sum([int(item) for item in x.replace("\n", "")])
                            self.data_summa.append(summa)
                        return data[-1]


    def get_summa(self):# Отримання суми останнього числа
        if self.get_numbers() is not None:
             return self.data_summa[-1]
        return "File is not find!!"

    def update_file(self,new_number):# Оновлення даних,запис нового числа в файл
        if os.path.exists(self.filename):
            with open(self.filename, 'a') as file:
                file.write(new_number + "\n")


class NumberSetProxy(FileNumberSet):

    def __init__(self, real_subject:FileNumberSet, log_filename,filename):
        super().__init__(filename=filename)
        self.real_subject = real_subject
        self.log_filename = log_filename


    # Отримання суми з проксі
    def get_summa(self):
        if os.path.exists(self.real_subject.filename):
            summa = self.real_subject.get_summa()
            self.log(summa)
            return summa
        else:
            with open(self.log_filename, "r") as f:
                data = json.load(f)
            if data:
                last_entry = max(data.keys())
                return data[last_entry]
            else:
                return None


    # Запис суми в лог-файл
    def log(self,summa):
        try:
            with open(self.log_filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}

        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data[now_time] = summa

        with open(self.log_filename, "w") as f:
            json.dump(data, f, indent=4)

if __name__ == '__main__':

    num_file="numbers.txt"
    log_life="data_log.json"
    res=FileNumberSet(num_file)
    proxy=NumberSetProxy(res,log_life,num_file)

    res.update_file("12")
    # proxy.update_file("16")


    print("Отримання числа",proxy.get_numbers())
    print("Отримання суми",proxy.get_summa())
