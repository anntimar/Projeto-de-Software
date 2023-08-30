import json


def push_post_list(postList):
    with open(
        "FishNet/file_data/post_list.json",
        "w",
    ) as file:
        json.dump(postList, file, indent=4)


def pull_post_list():
    with open("FishNet/file_data/post_list.json") as f:
        postList = json.load(f)
    return postList
