# Account class

from classs.postFile import postFile


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

    # def __init__(self, account):
    #     self.user = account["user"]
    #     self.password = account["password"]
    #     self.email = account["email"]
    #     self.first_login = account["first_login"]
    #     self.type_of_fish = account["type_of_fish"]
    #     self.posts = account["posts"]
    #     self.fish_cluters = account["fish_cluters"]
    #     self.fish_friends = account["fish_friends"]

    def __init__(self, user):
        self.accounts = postFile("FishNet/accountsList.json")
        self.account = self.accounts.content[user]
        self.user = self.account["user"]
        self.password = self.account["password"]
        self.email = self.account["email"]
        self.first_login = self.account["first_login"]
        self.type_of_fish = self.account["type_of_fish"]
        self.posts = self.account["posts"]
        self.fish_cluters = self.account["fish_cluters"]
        self.fish_friends = self.account["fish_friends"]

    def pull(self):
        self.accounts.pull()
        self.account = self.accounts.content[self.user]
        self.user = self.account["user"]
        self.password = self.account["password"]
        self.email = self.account["email"]
        self.first_login = self.account["first_login"]
        self.type_of_fish = self.account["type_of_fish"]
        self.posts = self.account["posts"]
        self.fish_cluters = self.account["fish_cluters"]
        self.fish_friends = self.account["fish_friends"]

    def push(self):
        self.accounts.pull()
        self.accounts.content[self.user] = {
            "user": self.user,
            "password": self.password,
            "email": self.email,
            "first_login": self.first_login,
            "type_of_fish": self.type_of_fish,
            "posts": self.posts,
            "fish_cluters": self.fish_cluters,
            "fish_friends": self.fish_friends,
        }
        self.accounts.push()
