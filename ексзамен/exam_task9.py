from abc import ABC, abstractmethod
import json
from typing import Union,Dict


class Output(ABC):
    @abstractmethod
    def display(self, student: 'Student') -> None:
        pass


class ConsoleOutput(Output):
    def display(self, student: 'Student') -> None:
        """Виводить інформацію про студента у консоль."""
        print(f"Ідентифікатор студента: {student.id_student}")
        print(f"Ім'я: {student.first_name} {student.last_name}")
        print("Курси:")
        for course_name, grades in student.courses.items():
            print(f"- {course_name}, Оцінки: {grades.grades if grades.grades else 'Оцінки відсутні'}")


class FileOutput(Output):
    def __init__(self, catalog: str):
        self.catalog = catalog

    def display(self, student: 'Student') -> None:
        """Записує інформацію про студента у файл."""
        student_info = {
            "Ідентифікатор студента": student.id_student,
            "Ім'я": student.first_name,
            "Прізвище": student.last_name,
            "Курси": {course_name: grades.to_json() for course_name, grades in student.courses.items()}
        }
        with open(fr"{self.catalog}\{student.first_name} {student.last_name}.json", "w", encoding="utf-8") as file:
            json.dump(student_info, file, indent=4, ensure_ascii=False)


class Student:
    def __init__(self, id_student: str, first_name: str, last_name: str):
        self.id_student = id_student
        self.first_name = first_name
        self.last_name = last_name
        self.courses = {}

    def add_course(self, course: 'Course', grades=None) -> None:
        """Додає курс для студента."""
        if grades is None:
            grades = Grades()
        self.courses[course.name] = grades

    def output_information(self, method: Output) -> None:
        """Виводить інформацію про студента за допомогою вказаного методу."""
        method.display(self)

    def remove_course(self, course: 'Course') -> None:
        """Видаляє курс для студента."""
        if course.name in self.courses:
            del self.courses[course.name]


class Course:
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student: 'Student') -> None:
        """Додає студента на курс."""
        self.students.append(student)

    def remove_student(self, student: 'Student') -> None:
        """Видаляє студента з курсу."""
        self.students.remove(student)


class Grades:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade: int ) -> None:
        """Додає оцінку."""
        self.grades.append(grade)

    def update_grade(self, index: int, new_grade: int) -> None:
        """Оновлює оцінку за індексом."""
        if index < len(self.grades):
            self.grades[index] = new_grade
        else:
            print("Індекс оцінки перевищує довжину списку оцінок.")

    def to_json(self) -> list:
        """Повертає список оцінок у форматі JSON."""
        return self.grades


class School:
    students = []
    courses = []

    @staticmethod
    def add_student(student: 'Student') -> None:
        """Додає студента до школи."""
        School.students.append(student)

    @staticmethod
    def del_student(student: 'Student') -> None:
        """Видаляє студента зі школи."""
        School.students.remove(student)

    @staticmethod
    def add_course(course: 'Course') -> None:
        """Додає курс до школи."""
        School.courses.append(course)

    @staticmethod
    def remove_course(course: 'Course') -> None:
        """Видаляє курс зі школи."""
        for student in School.students:
            student.remove_course(course)
        School.courses.remove(course)

    @staticmethod
    def register_to_course(student: 'Student', course: 'Course') -> None:
        """Реєструє студента на курсі."""
        if student in School.students and course in School.courses:
            course.add_student(student)
            student.add_course(course)
        else:
            print("Студент або курс не знайдені.")

    @staticmethod
    def withdraw_from_course(student: 'Student', course: 'Course') -> None:
        """Виводить студента з курсу."""
        if student in School.students and course in School.courses:
            course.remove_student(student)
            student.remove_course(course)
            print(f"Студент {student.first_name} {student.last_name} виведений з курсу {course.name}")
        else:
            print("Студент або курс не знайдені.")

    @staticmethod
    def student_info(student_id: str, method: Output) -> None:
        """Виводить інформацію про студента за допомогою вказаного методу."""
        student = School.find_student_by_id(student_id)
        if student:
            student.output_information(method)

    @staticmethod
    def course_info(course_name: str) -> Union['Course', None]:
        """Повертає інформацію про курс або None, якщо курс не знайдено."""
        for course in School.courses:
            if course.name == course_name:
                return course
        print(f"Такого курсу немає: {course_name}")
        return None




    @staticmethod
    def find_student_by_name(name: str) -> Union[Dict[str, str], None]:
        """Знаходить інформацію про студента за ім'ям або прізвищем.

        Параметри:
        name (str): Ім'я або прізвище студента, якого потрібно знайти.

        Повертає:
        Union[Dict[str, str], None]: Інформація про студента у форматі словника,
        що містить його ім'я, прізвище та ідентифікатор, або None, якщо студент не знайдений.
        """
        for student in School.students:
            if student.first_name.lower() == name.lower() or student.last_name.lower() == name.lower():
                return {
                    "Ідентифікатор студента": student.id_student,
                    "Ім'я": student.first_name,
                    "Прізвище": student.last_name
                }
        print(f"Студента з ім'ям або прізвищем '{name}' не знайдено.")
        return None

    @staticmethod
    def find_student_by_id(student_id: str) -> Union['Student', None]:
        """Знаходить студента за ідентифікатором."""
        for student in School.students:
            if student.id_student == student_id:
                return student
        print(f"Немає студента з ідентифікатором: {student_id}")
        return None

    @staticmethod
    def display_students_on_course(course_name: str, method: ConsoleOutput) -> None:
        """Виводить інформацію про студентів, які зареєстровані на вказаному курсі."""
        course = School.course_info(course_name)
        if course:
            print(f"Студенти, записані на {course_name}:")
            for student in course.students:
                student.output_information(method)
        else:
            print(f"Такого курсу немає: {course_name}")

    @staticmethod
    def display_courses_for_student(student_id: str) -> None:
        """Виводить перелік курсів, на які записаний студент."""
        student = School.find_student_by_id(student_id)
        if student:
            print(f"Курси, на які записаний студент {student_id}:")
            for course_name in student.courses:
                print(course_name)
        else:
            print(f"Немає студента з ідентифікатором: {student_id}")

    @staticmethod
    def update_grade(student_id: str, course_name: str, new_grade: int, index: int) -> None:
        """Оновлює оцінку студента за вказаним курсом і індексом оцінки."""
        student = School.find_student_by_id(student_id)
        if student:
            if course_name in student.courses:
                student.courses[course_name].update_grade(index, new_grade)
                print(f"Оцінка за курс {course_name} оновлена для студента {student_id}")
            else:
                print(f"Студент {student_id} не записаний на курс {course_name}")
        else:
            print(f"Немає студента з ідентифікатором: {student_id}")

    @staticmethod
    def add_grade(student_id: str, course_name: str, grade: int) -> None:
        """Додає оцінку студенту за вказаним курсом."""
        student = School.find_student_by_id(student_id)
        if student:
            if course_name in student.courses:
                student.courses[course_name].add_grade(grade)
                print(f"Оцінка за курс {course_name} додана для студента {student_id}")
            else:
                print(f"Студент {student_id} не записаний на курс {course_name}")



# Каталог де буде зберігатися інформаціяпро кожного студента
catalog = "student_info"

# Екземпляри для виводу інформації
file_output = FileOutput(catalog)
console_output = ConsoleOutput()
# Клас який керує студентами та курсами
school = School()
# Створюємо студентів
student1 = Student("1111", "Andrew", "Gapyuk")
student2 = Student("2222", "John", "Doe")
# Створюємо курси
course_math = Course("Математика")
course_geogr = Course("Географія")
course_history = Course("Історія")
# Додаємо студентів до школи
school.add_student(student1)
school.add_student(student2)
# додаємо курси в школу
school.add_course(course_history)
school.add_course(course_geogr)
school.add_course(course_math)
# Реєструємо студента на курс
school.register_to_course(student1, course_math)
school.register_to_course(student1, course_history)
school.register_to_course(student1, course_geogr)
school.register_to_course(student2, course_geogr)
# Додаємо оцінки студенту за перний курс
school.add_grade("1111", course_geogr.name, 10)
school.add_grade("1111", course_geogr.name, 12)
# Виводимо інформацію через клас студент
student1.output_information(console_output)
# Змінюємо оцінку студенту
school.update_grade("1111", course_geogr.name, 9, 0)
# Виводимо список курсів на які записаний студент
school.display_courses_for_student("1111")
# Виводимо інформацію про  студентів які записані на курс
school.display_students_on_course(course_geogr.name,console_output)
# Виводимо інформацію про студента
school.student_info("1111",console_output)
school.student_info("1111",file_output)
# Виваляємо студента з курсу Географія
school.withdraw_from_course(student1, course_geogr)
# Виваляємо курс Географію із школи
school.remove_course(course_geogr)
# Виводимо список курсів які є в школі
for course in school.courses:
    print(course.name)
# Виводимо інформацію про студента в файл і в консоль
# school.student_info("1111",console_output)
# school.student_info("1111",file_output)

print(school.find_student_by_name("Andrew"))