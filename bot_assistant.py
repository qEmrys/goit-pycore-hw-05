def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."
    return inner

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact updated."
    
@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    return contacts[name]
    
@input_error
def show_all(contacts: dict) -> str:
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def exit_command(_):
    print("Good bye!")
    raise SystemExit

def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    command_list = {
        "hello": lambda args: "How can I help you?",
        "add": lambda args: add_contact(args, contacts),
        "change": lambda args: change_contact(args, contacts),
        "phone": lambda args: show_phone(args, contacts),
        "all": lambda: show_all(contacts),
        "exit": exit_command,
        "close": exit_command
    }

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        handler = command_list.get(command)

        if handler:
            print(handler(args))        
        else:           
            print("Invalid command.")


if __name__ == "__main__":
    main()
