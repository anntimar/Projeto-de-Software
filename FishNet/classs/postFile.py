# list class

import json


class postFile:
    def __init__(self, file):
        self.file = file
        self.content = self.pull()

    def push(self):
        with open(
            self.file,
            "w",
        ) as file:
            json.dump(self.content, file, indent=4)

    def pull(self):
        with open(self.file) as f:
            fileContent = json.load(f)
        self.content = fileContent
        return fileContent
