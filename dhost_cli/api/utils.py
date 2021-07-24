def get_user_str_input(str_input="", message=""):
    """Ask for the user input and repeate while it's empty."""
    while str_input == "" or str_input is None:
        str_input = input(message + ": ")
    return str_input


def basic_item_print(data):
    for key, value in data.items():
        print("{key}: {value}".format(key=key, value=value))


def basic_list_print(data_list):
    for item in data_list:
        basic_item_print(item)
        print()


def basic_print(data, many=False):
    if many:
        return basic_list_print(data)
    return basic_item_print(data)
