COMMANDS_LIST = ["add", "change", "close", "hello", "phone", "show all"]
CLOSE_COMMANDS_LIST = ["good bye", "close", "exit"]
CONTACTS = {}


def input_error(function):

    def wrapper(*args):

        try:
            result = function(*args)
            return result
        except ValueError:
            print(f"You've entered wrong command. Chose one of those: {', '.join(COMMANDS_LIST)}, {', '.join(CLOSE_COMMANDS_LIST)}.")
        except IndexError:
            print("Enter user name and phone number.")
        except KeyError:
            print("This user name doesn't exist.")
        except NameError:
            print("Enter user name.")
        
    return wrapper


def main():

    while True:

        user_text = input("Enter command: ")
        a = parser(user_text)

        if not a:
            continue
        
        command, user_information = parser(user_text)

        if command in CLOSE_COMMANDS_LIST:
            print("Good bye!")
            break

        get_handler(command)(user_information)

        
@input_error
def parser(user_text):
     
    lower_user_text = user_text.lower()
    command, *user_information = lower_user_text.split()

    if command in ["show", "good"] and len(user_information) > 0:
        command = f"{command} {user_information[0]}"

    if command not in (COMMANDS_LIST + CLOSE_COMMANDS_LIST):
        raise ValueError
    
    return command, user_information


def get_handler(command):

    return COMMANDS[command]


@input_error
def add(user_information):

    if user_information[0] not in CONTACTS:
        CONTACTS[user_information[0]] = user_information[1]
    else:
        print("This contact exists.")


@input_error
def change(user_information):

    CONTACTS[user_information[0]]
    CONTACTS[user_information[0]] = user_information[1]


def greeting(*args):

    print("How can I help you?")


@input_error
def phone(user_information):
    
    if not user_information:
        raise NameError
    
    print(CONTACTS[user_information[0]])


def show_all(*args):

    list(map(lambda x: print(f"{x[0]}: {x[1]}"), CONTACTS.items()))


COMMANDS = {
    'add': add,
    'change': change,
    'hello': greeting,
    'phone': phone,
    'show all': show_all,
}


main()