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
                postPull(account, "ocean", Menu.post_create())
            case 3:
                account.pull()
                while True:
                    action = Menu.post_feed_of_fish_cluters(account)
                    if action == 1:
                        break
                    elif action <= len(account.fish_cluters) + 1:
                        postPull(
                            account,
                            account.fish_cluters[action - 2],
                            Menu.post_create(),
                        )
