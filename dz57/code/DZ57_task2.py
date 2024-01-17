class Book:
    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name):
        print(f"call __getattr__{name=}")
        if name not in self._attributes:
            raise AttributeError(f"'Book' object has no atribute '{name}'")
        return self._attributes[name]

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=} {value=}")
        if name == "_attributes":
            object.__setattr__(self, name, value)
        else:
            self._attributes[name] = value

    def __delattr__(self, name):
        try:
            if str(name) not in self._attributes:
                raise KeyError(f"Attribute is '{name}' not found!!'")
            del self._attributes[str(name)]
        except KeyError as k:
            print(k)

    # def __getattribute__(self, name):
    #     print(f"Call __getattribute__ with {name=}")
    #     if name in ("_attributes","__dict__"):
    #         return super().__getattribute__(name)
    #     else:
    #         raise AttributeError("Error ")
    def __getattribute__(self, name):
        print(f"Виклик __getattribute__ з атрибутом {name=}")
        try:
            if name == "secret":
                raise AttributeError("Доступ заборонено до атрибуту 'secret'")
            return super().__getattribute__(name)
        except AttributeError as a:
            return a


print("1----------------------")
book = Book("Python Programming", "John Zelle")
print("2----------------------")
book.year = 2016
print("3----------------------")
print(book.__dict__)
print("4----------------------")
print("book.year=", book.year)
print(book.secret)

# print("book.title=", book.title)
# print("book.author=", book.author)
# book.year = 2016
# print(book.__dict__)
# print("book.year=", book.year)
# book2 = Book("Python", "John Zelle")
# del book2.author
# print(book2.__dict__)
