from abc import ABC, abstractmethod
from addressbook import AddressBook


class AbstractView(ABC):
    @abstractmethod
    def show_message(self, msg: str):
        pass

    @abstractmethod
    def show_all(self, book: AddressBook):
        pass

    @abstractmethod
    def show_commands(self):
        pass


class ConsoleView(AbstractView):
    def show_message(self, msg: str):
        print(msg)

    def show_all(self, book: AddressBook):
        if not book.data:
            print("No contacts found.")
        else:
            for record in book.values():
                print(record)

    def show_commands(self):
        commands = """
Available commands:
- add <name> <phone>
- change <name> <old_phone> <new_phone>
- phone <name>
- all
- add-birthday <name> <DD.MM.YYYY>
- show-birthday <name>
- birthdays
- hello
- exit / close
"""
        print(commands)
