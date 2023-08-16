# list class
import json


class postList:
    def __init__(self, file):
        self.file = file

    def push(self, postList):
        with open(
            self.file,
            "w",
        ) as file:
            json.dump(postList, file, indent=4)

    def pull(self):
        with open(self.file) as f:
            postList = json.load(f)
        return postList
