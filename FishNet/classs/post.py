# Post class


class Post:
    def __init__(self, type_of_fish, userName, content):
        self.type_of_fish = type_of_fish
        self.userName = userName
        self.bubbles = []
        self.pops = []
        self.content = content

    def json(self):
        return {
            "type_of_fish": self.type_of_fish,
            "userName": self.userName,
            "bubbles": self.bubbles,
            "pops": self.pops,
            "content": self.content,
        }

    def bubble(self, user):
        if user != self.userName:
            if user in self.pops:
                self.pops.remove(user)
            if user not in self.bubbles:
                self.bubbles.append(user)

    def pop(self, user):
        if user != self.userName:
            if user in self.bubbles:
                self.bubbles.remove(user)
            if user not in self.pops:
                self.pops.append(user)
