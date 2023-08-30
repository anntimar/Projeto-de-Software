import time
from colorama import Fore
from colorama import Style
from feed_screen import feed

from post_list_actions import *
from accounts_list_actions import *
from classs.menu import Menu
from classs.customTerminal import CustomTerminal as ct


def fish_cluter_screen(account):
    while True:
        action = Menu.fish_cluster()
        if action == "1":
            feed_of_fish_cluters(account)
        elif action == "2":
            crate_fish_cluster(account)
        elif action == "3":
            enter_user_in_fish_cluster(account)
        elif action == "4":
            exit_user_in_fish_cluster(account)
        elif action == "5":
            break


def crate_fish_cluster(account):
    postList = pull_post_list()
    account.pull()

    while True:
        Menu.profile()
        fishClusterName = input(
            f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DO CARDUME ▷  {Fore.YELLOW}"
        )
        fishClusterName = str(fishClusterName).lower()
        print(f"{Style.RESET_ALL}")
        if fishClusterName in postList:
            print(
                f"{Fore.RED} ✖  NOME DE CARDUME INDISPONÍVEL, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(2)
        else:
            postList[fishClusterName] = []
            push_post_list(postList)
            account.fish_cluters.append(fishClusterName)
            account.push()
            print(f"{Fore.GREEN} ✔  NOME DE CARDUME DISPONÍVEL!{Style.RESET_ALL}")
            time.sleep(1)
            while True:
                action = Menu.create_fish_cluster()
                if action == "1":
                    add_user_in_fish_cluster(fishClusterName)
                elif action == "2":
                    remove_user_in_fish_cluster(fishClusterName)
                elif action == "3":
                    break
            Menu.profile()
            print(f"{Fore.GREEN} ✔  CARDUME CRIADO COM SUCESSO!{Style.RESET_ALL}")
            account.push()
            time.sleep(1)
            break


def add_user_in_fish_cluster(fishClusterName):
    accountsList = pull_accounts_list()

    while True:
        Menu.profile()
        userName = input(
            f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DO USUÁRIO ▷  {Fore.YELLOW}"
        )
        userName = str(userName).lower()
        print(f"{Style.RESET_ALL}")

        if userName in accountsList:
            print(f"{Fore.GREEN} ✔  USUÁRIO LOCALIZADO!{Style.RESET_ALL}")
            time.sleep(2)

            if fishClusterName not in accountsList[userName]["fish_cluters"]:
                accountsList[userName]["fish_cluters"].append(fishClusterName)
                push_accounts_list(accountsList)
                print(
                    f"{Fore.GREEN} ✔  USUÁRIO ADICIONADO AO CARDUME!{Style.RESET_ALL}"
                )
                time.sleep(2)
            else:
                print(
                    f"{Fore.RED} ✖  USUÁRIO JÁ PERTENCE A ESSE CARDUME!{Style.RESET_ALL}"
                )
                time.sleep(2)
            break
        else:
            print(
                f"{Fore.RED} ✖  USUÁRIO NÃO LOCALIZADO, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(1)


def remove_user_in_fish_cluster(fishClusterName):
    accountsList = pull_accounts_list()

    while True:
        ct.clean()
        Menu.profile()
        userName = input(
            f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DO USUÁRIO ▷  {Fore.YELLOW}"
        )
        userName = str(userName).lower()
        print(f"{Style.RESET_ALL}")

        if userName in accountsList:
            print(f"{Fore.GREEN} ✔  USUÁRIO LOCALIZADO!{Style.RESET_ALL}")
            time.sleep(2)

            if fishClusterName in accountsList[userName]["fish_cluters"]:
                accountsList[userName]["fish_cluters"].remove(fishClusterName)
                push_accounts_list(accountsList)
                print(f"{Fore.GREEN} ✔  USUÁRIO REMOVIDO DO CARDUME!{Style.RESET_ALL}")
                time.sleep(2)
            else:
                print(
                    f"{Fore.RED} ✖  USUÁRIO NÃO PERTENCE A ESSE CARDUME!{Style.RESET_ALL}"
                )
                time.sleep(2)
            break
        else:
            print(
                f"{Fore.RED} ✖  USUÁRIO NÃO LOCALIZADO, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(1)


def enter_user_in_fish_cluster(perfilUser):
    postList = pull_post_list()
    accountsList = pull_accounts_list()

    while True:
        ct.clean()
        Menu.profile()
        fishClusterName = input(
            f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DO CARDUME ▷  {Fore.YELLOW}"
        )
        fishClusterName = str(fishClusterName).lower()
        print(f"{Style.RESET_ALL}")

        if fishClusterName in postList and fishClusterName != "ocean":
            print(f"{Fore.GREEN} ✔  CARDUME LOCALIZADO!{Style.RESET_ALL}")
            time.sleep(2)
            if fishClusterName not in accountsList[perfilUser["user"]]["fish_cluters"]:
                accountsList[perfilUser["user"]]["fish_cluters"].append(fishClusterName)
                push_accounts_list(accountsList)
                print(
                    f"{Fore.GREEN} ✔  ENTRADA NO CARDUME COM SUCESSO!{Style.RESET_ALL}"
                )
                time.sleep(2)
            else:
                print(
                    f"{Fore.RED} ✖  VOCÊ JÁ PERTENCE A ESSE CARDUME!{Style.RESET_ALL}"
                )
                time.sleep(2)

            break

        else:
            print(
                f"{Fore.RED} ✖  CARDUME NÃO LOCALIZADO, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(1)


def exit_user_in_fish_cluster(perfilUser):
    postList = pull_post_list()
    accountsList = pull_accounts_list()

    while True:
        ct.clean()
        Menu.profile()
        fishClusterName = input(
            f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DO CARDUME ▷  {Fore.YELLOW}"
        )
        fishClusterName = str(fishClusterName).lower()
        print(f"{Style.RESET_ALL}")

        if fishClusterName in postList and fishClusterName != "ocean":
            print(f"{Fore.GREEN} ✔  CARDUME LOCALIZADO!{Style.RESET_ALL}")
            time.sleep(2)
            if fishClusterName in accountsList[perfilUser["user"]]["fish_cluters"]:
                accountsList[perfilUser["user"]]["fish_cluters"].remove(fishClusterName)
                push_accounts_list(accountsList)
                print(f"{Fore.GREEN} ✔  SAÍDA NO CARDUME COM SUCESSO!{Style.RESET_ALL}")
                time.sleep(2)
            else:
                print(
                    f"{Fore.RED} ✖  VOCÊ NÃO PERTENCE A ESSE CARDUME!{Style.RESET_ALL}"
                )
                time.sleep(2)

            break

        else:
            print(
                f"{Fore.RED} ✖  CARDUME NÃO LOCALIZADO, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(1)


def feed_of_fish_cluters(account):
    postList = pull_post_list()
    account.pull()

    while True:
        action = int(Menu.post_feed_of_fish_cluters(account))
        if action == 0:
            return
        if action <= len(account.fish_cluters):
            if len(postList[account.fish_cluters[action - 1]]) > 0:
                feed(account, account.fish_cluters[action - 1])
            else:
                ct.clean()
                Menu.profile()
                print(f"{Fore.RED} ✖  NÃO EXISTE POSTS NESSE CARDUME!{Style.RESET_ALL}")
                time.sleep(2)
        elif action == len(account.fish_cluters) + 1:
            break
