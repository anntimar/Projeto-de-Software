import time

from classs.banner import Banner
from classs.menu import Menu
from post_pull import postPull
from classs.customTerminal import CustomTerminal as ct


def createPost(account):
    while True:
        match Menu.post():
            case 1:
                break
            case 2:
                post_nenu(account, "ocean")
            case 3:
                post_feed_of_fish_cluters(account)


def post_nenu(account, fishCluters):
    Banner.profile()
    postPull(account, fishCluters, ct.inputStr("✎", "DIGITE SEU POST"))

    Banner.profile()
    ct.positiveMessage("POST ENVIADO COM SUCESSO!")
    time.sleep(2)


def post_feed_of_fish_cluters(account):
    account.pull()

    while True:
        action = Menu.post_feed_of_fish_cluters(account)
        if action == 1:
            break
        elif action <= len(account.fish_cluters) + 1:
            post_nenu(account, account.fish_cluters[action - 2])
