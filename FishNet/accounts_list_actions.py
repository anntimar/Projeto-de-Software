import json


def push_accounts_list(accountsList):
    with open(
        "FishNet/file_data/accountsList.json",
        "w",
    ) as file:
        json.dump(accountsList, file, indent=4)


def pull_accounts_list():
    with open("FishNet/file_data/accountsList.json") as f:
        accountsList = json.load(f)
    return accountsList
