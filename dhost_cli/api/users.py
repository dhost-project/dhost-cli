def me(self):
    uri = 'v1/users/me/'
    response = self.get(uri=uri)
    print_user(response.json())


def print_user(user_data):
    print('ID: {}'.format(user_data['id']))
    print('username: {}'.format(user_data['username']))
    print('email: {}'.format(user_data['email']))
    print('avatar: {}'.format(user_data['avatar']))
