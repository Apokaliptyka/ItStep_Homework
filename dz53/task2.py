import  datetime

class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

class Baby(Person):
    def speak(self):
        print("Blah blah blah")

class Adult(Person):
    def speak(self):
        print(f"Hello, my name is {self.first_name} ")

class Calendar:
    def book_appointment(self,date):
        print("Booking appointment for date",date)

class OrganizedAult(Adult,Calendar):
    pass
class OrganizedBaby(Baby,Calendar):
    def book_appointment(self,date):
        print("Note that you are booking appointment with a baby.")
        super().book_appointment(date)


andres=OrganizedAult("Andres","Gomes")
boris= OrganizedBaby("Boris","Bumblebutton")
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018,1,1))


