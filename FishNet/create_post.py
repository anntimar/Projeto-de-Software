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


def createPost(perfilUser):
    while True:
        action = post_menu()
        if action == "1":
            clean_terminal()
            profile_banner()
            content = input(f"{Fore.CYAN} digite seu post ▷  {Fore.YELLOW}")
            postPull(perfilUser, "ocean", content)
            clean_terminal()
            profile_banner()
            print(f"{Fore.GREEN} ✔  POST ENVIADO COM SUCESSO!{Style.RESET_ALL}")
            time.sleep(2)
        elif action == "2":
            post_feed_of_fish_cluters(perfilUser)
        elif action == "3":
            break


def post_feed_of_fish_cluters(perfilUser):
    accountsList = pull_accounts_list()
    postList = pull_post_list()
    while True:
        action = int(post_feed_of_fish_cluters_menu(perfilUser))
        if action == 0:
            return

        if action <= len(accountsList[perfilUser["user"]]["fish_cluters"]):
            clean_terminal()
            profile_banner()
            content = input(f"{Fore.CYAN} DIGITE SEU POST ▷  {Fore.YELLOW}")
            postPull(
                perfilUser,
                accountsList[perfilUser["user"]]["fish_cluters"][action - 1],
                content,
            )
            clean_terminal()
            profile_banner()
            print(f"{Fore.GREEN} ✔  POST ENVIADO COM SUCESSO!{Style.RESET_ALL}")
            time.sleep(2)

        elif action == len(accountsList[perfilUser["user"]]["fish_cluters"]) + 1:
            break
