def parse_input(user_input: str):
    """
    Takes a string of user input and splits it into words using the split() method.
    It returns the first word as the command 'cmd' and the rest as a list of arguments *args.
    :param user_input:
    :return the first word as 'cmd' and the rest as a list of arguments:
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict):
    """
    Adding a new contact to the contact dictionary.
    :param args:
    :param contacts:
    :return "Contact added." if the addition was successful:
    """
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added.\n"
    except ValueError:
        print("Enter a valid command in this format --->>> <add> <name> <phone number> ")
        return ""


def change_contact(args: list, contacts: dict):
    """
    Stores in memory a new phone number for the username contact that already exists in the notebook.
    Creates a new contact if it does not exist.
    :param args:
    :param contacts: 
    :return "Contact changed." if the changing was successful: 
    """
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact changed.\n"
    except ValueError:
        print("Enter a valid command in format --->>> <change> <name> <new phone number> ")
        return ""


def get_phone(args: list, contacts: dict):
    """
    Returns the name and phone number if the contact is found.
    :param args:
    :param contacts:
    :return The name and phone number if the contact is found:
    """
    try:
        return f"{args[0]}'s phone number is {contacts[args[0]]}\n".capitalize()
    except (KeyError, IndexError):
        print('This contact was not found in the system. Try again.')
        return "Enter a command in this format --->>> <phone> <name>"


def get_all_phones(contacts: dict):
    """
    Return all saved contacts with phone numbers to the console, if any.
    :param contacts:
    :return all saved contacts:
    """
    if len(contacts) == 0:
        print("There are still no entries in your notebook. Try making one.\n")
    else:
        for k, v in contacts.items():
            print(f"{k}'s phone number is {v}".capitalize())
        print("")


def read_file(path='contacts.txt'):
    """
    Read users from the given file. By default, 'contacts.txt'.
    :param path:
    :return dict(contacts):
    """
    try:
        with open(path, 'r') as file:
            contacts = {}
            for line in file.readlines():
                name, phone = line.split(',')
                contacts[name] = phone.replace("\n", "")
            return contacts
    except FileNotFoundError:
        with open('contacts.txt', 'w'):
            return {}


def main():
    contacts = read_file()
    print("Welcome to the assistant bot!\nPrint 'Help' to see all commands.\n")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            print("Good bye!")
            with open('contacts.txt', 'w') as file:
                for k, v in contacts.items():
                    file.write(f"{k},{v}\n")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            get_all_phones(contacts)
        elif command == "help":
            print("""
                1. 'Add' <name> <phone number> --> Adding a new contact to the contact dictionary.
                2. 'Change' <name> <phone number> --> Stores in memory a new phone number for the username.
                3. 'Phone' <name> --> Returns the name and phone number.
                4. 'All' -> Return all saved contacts with phone numbers.
                5. 'Close' or 'Exit' -> Exit the program.
            """)
        else:
            print("Invalid command. Print 'Help' to see all commands.")


if __name__ == "__main__":
    main()
