def get_user_str_input(str_input='', message=''):
    """Ask for the user input and repeate while it's empty"""
    while str_input == '' or str_input is None:
        str_input = input(message + ': ')
    return str_input
