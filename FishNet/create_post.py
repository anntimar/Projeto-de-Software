import time

from classs.banner import Banner
from classs.menu import Menu
from post_pull import postPull
from colorama import Fore
from colorama import Style
from classs.customTerminal import CustomTerminal as ct


def createPost(account):
    while True:
        action = Menu.post()
        if action == "1":
            post_nenu(account, "ocean")
        elif action == "2":
            post_feed_of_fish_cluters(account)
        elif action == "3":
            break


def post_nenu(account, fishCluters):
    Banner.profile()
    content = input(f"{Fore.CYAN} DIGITE SEU POST ▷  {Fore.YELLOW}")
    postPull(account, fishCluters, content)
    Banner.profile()
    print(f"{Fore.GREEN} ✔  POST ENVIADO COM SUCESSO!{Style.RESET_ALL}")
    time.sleep(2)


def post_feed_of_fish_cluters(account):
    account.pull()

    while True:
        action = int(Menu.post_feed_of_fish_cluters(account))
        if action == 0:
            return
        if action <= len(account.fish_cluters):
            post_nenu(account, account.fish_cluters[action - 1])

        elif action == len(account.fish_cluters) + 1:
            break
