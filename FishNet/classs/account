# Account class


class Account:
    def __init__(self, user, password, email):
        self.user = user
        self.password = password
        self.email = email
        self.first_login = True
        self.type_of_fish = 0
        self.posts = []
        self.fish_cluters = []
        self.fish_friends = []

    def json(self):
        return {
            "user": self.user,
            "password": self.password,
            "email": self.email,
            "first_login": self.first_login,
            "type_of_fish": self.type_of_fish,
            "posts": self.posts,
            "fish_cluters": self.fish_cluters,
            "fish_friends": self.fish_friends,
        }
