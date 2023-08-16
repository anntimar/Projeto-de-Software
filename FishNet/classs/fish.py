# Fish class


class Fish:
    def __init__(self, name, icon, personality, profile):
        self.name = name
        self.icon = icon
        self.characteristics = personality
        self.profile = profile

    def printName(self):
        print(self.name)

    def printIcon(self):
        print(self.icon)

    def printPersonality(self):
        print(self.personality)

    def printprofile(self):
        print(self.profile)
