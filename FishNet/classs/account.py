# Account class

from classs.postFile import postFile


class Account:
    def __init__(self, user, password="_none", email="_none"):
        # self.__accounts = postFile("FishNet/file_data/accountsList.json")
        self.__accounts = postFile(
            "C:/Users/thiag/OneDrive/Documentos/PROJETOS UFAL/FishNet/Projeto-de-Software/FishNet/file_data/accountsList.json"
        )

        if password == "_none" and email == "_none":
            self.__account = self.__accounts.content[user]

            self.user = self.__account["user"]
            self.password = self.__account["password"]
            self.email = self.__account["email"]
            self.first_login = self.__account["first_login"]
            self.type_of_fish = self.__account["type_of_fish"]
            self.posts = self.__account["posts"]
            self.fish_cluters = self.__account["fish_cluters"]
            self.fish_friends = self.__account["fish_friends"]
        else:
            self.user = user
            self.password = password
            self.email = email
            self.first_login = True
            self.type_of_fish = 0
            self.posts = []
            self.fish_cluters = []
            self.fish_friends = []
            self.push()

    def pull(self):
        self.__accounts.pull()
        self.__account = self.__accounts.content[self.user]
        self.user = self.__account["user"]
        self.password = self.__account["password"]
        self.email = self.__account["email"]
        self.first_login = self.__account["first_login"]
        self.type_of_fish = self.__account["type_of_fish"]
        self.posts = self.__account["posts"]
        self.fish_cluters = self.__account["fish_cluters"]
        self.fish_friends = self.__account["fish_friends"]

    def push(self):
        self.__accounts.pull()
        self.__accounts.content[self.user] = {
            "user": self.user,
            "password": self.password,
            "email": self.email,
            "first_login": self.first_login,
            "type_of_fish": self.type_of_fish,
            "posts": self.posts,
            "fish_cluters": self.fish_cluters,
            "fish_friends": self.fish_friends,
        }
        self.__accounts.push()
