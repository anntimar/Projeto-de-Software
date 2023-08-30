import time
from menus import post_feed_of_fish_cluters_menu
from banner import profile_banner
from accounts_list_actions import pull_accounts_list
from post_list_actions import pull_post_list
from post_list_actions import push_post_list
from actions import clean_terminal
from post_pull import postPull
from menus import post_menu
from colorama import Fore
from colorama import Style


def createPost(account):
    while True:
        action = post_menu()
        if action == "1":
            post_nenu(account, "ocean")
        elif action == "2":
            post_feed_of_fish_cluters(account)
        elif action == "3":
            break


def post_nenu(account, fishCluters):
    profile_banner()
    content = input(f"{Fore.CYAN} DIGITE SEU POST ▷  {Fore.YELLOW}")
    postPull(account, fishCluters, content)
    profile_banner()
    print(f"{Fore.GREEN} ✔  POST ENVIADO COM SUCESSO!{Style.RESET_ALL}")
    time.sleep(2)


def post_feed_of_fish_cluters(account):
    account.pull()

    while True:
        action = int(post_feed_of_fish_cluters_menu(account))
        if action == 0:
            return
        if action <= len(account.fish_cluters):
            post_nenu(account, account.fish_cluters[action - 1])

        elif action == len(account.fish_cluters) + 1:
            break
