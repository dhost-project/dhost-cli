def me(self):
    uri = 'v1/users/me/'
    response = self.get(uri=uri)
    print(response.json())
