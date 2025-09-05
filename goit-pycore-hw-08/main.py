from commands import (
    add_contact, change_contact, show_phone,
    add_birthday, show_birthday, birthdays
)
from storage import save_data, load_data
from views import ConsoleView


def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def main():
    book = load_data()
    view = ConsoleView()  # тепер UI через абстракцію
    view.show_message("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            view.show_message("Good bye! Your data has been saved ✅")
            break
        elif command == "hello":
            view.show_message("How can I help you?")
        elif command == "add":
            view.show_message(add_contact(args, book))
        elif command == "change":
            view.show_message(change_contact(args, book))
        elif command == "phone":
            view.show_message(show_phone(args, book))
        elif command == "all":
            view.show_all(book)
        elif command == "add-birthday":
            view.show_message(add_birthday(args, book))
        elif command == "show-birthday":
            view.show_message(show_birthday(args, book))
        elif command == "birthdays":
            view.show_message(birthdays(args, book))
        elif command == "help":
            view.show_commands()
        else:
            view.show_message("Invalid command. Type 'help' for commands list.")
