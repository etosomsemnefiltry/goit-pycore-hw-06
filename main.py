from collections import UserDict

class Field:
    '''Обработка любого поля.
    Все приходящие значения переводим в строку и отдаем.'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    '''Обработка имени контакта'''
    pass

class Phone(Field):
    '''Обработка номера телефона'''
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)

    @staticmethod   
    def validate(phone):
        '''Проверка номера на соответствие требованиям'''
        if len(phone) != 10:
            print("Phone must contain 10 digits")
            return False
        return True

class Record:
    '''Обработка любой записей для Книги'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, search_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == search_phone:
                return self.phones[i]

    def remove_phone(self, del_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == del_phone:
                del self.phones[i]

    def __str__(self):
       return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
     '''Реализация Книги с контактами'''
     def add_record(self, record):
        if record.name in self.data:
            print('Contact already exist')
        else:
            self.data[record.name.value] = record

     def find(self, name):
         return self.data.get(name)
     
     def delete(self, name):
         if name in self.data:
            del self.data[name]

# Создадим новую Книгу контактов
book = AddressBook()

# Создадим новый контакт 
john_record = Record("John")
john_record.add_phone("1234567855")
john_record.add_phone("5555555555")
john_record.add_phone("9999999999")
book.add_record(john_record)
print(f"\nВ книгу добавлен Новый контакт\n{john_record}")

# Создадим еще 2 контакта
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
print(f"\nВ книгу добавлен Новый контакт\n{jane_record}")

ivan_record = Record("Ivan")
ivan_record.add_phone("2134547810")
book.add_record(ivan_record)
print(f"\nВ книгу добавлен Новый контакт\n{ivan_record}")

# Поиск контакта в Книге
john = book.find("John")
print(f"\nПоиск по имени John в Книге\n{john}")

# Редактирование контакта
john.edit_phone("1234567855", "1111111111")
print(f"\nЗамена телефона в Книге c 1234567855 на 1111111111\n{john}")

# Поиск номера в списке номеров контакта
found_phone = john.find_phone("5555555555")
print(f"\nПоиск номера 5555555555 в записи John\n{found_phone}")

# Удалим телефон в списке телефонов контакта
john.remove_phone("9999999999")
print(f"\nУдаление номера 9999999999 в записи\n{john}\n")

# Удалим контакт из Книги
book.delete("John")

# Покажем что осталось в книге
print(f"\nПокажем содержимое Книги")
for name, record in book.data.items():
        print(record)
print("\n")