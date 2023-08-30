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
        match Menu.fish_cluster():
            case 1:
                break
            case 2:
                feed_of_fish_cluters(account)
            case 3:
                create_fish_cluster(account)
            case 4:
                enter_user_in_fish_cluster(account)
            case 5:
                exit_user_in_fish_cluster(account)


def create_fish_cluster(account):
    postList = pull_post_list()
    account.pull()

    while True:
        Menu.profile()
        fishClusterName = ct.inputStr("🐟", "NOME DO CARDUME")

        if fishClusterName in postList:
            ct.negativeMessage("NOME DE CARDUME INDISPONÍVEL!")
            time.sleep(2)

        else:
            postList[fishClusterName] = []
            push_post_list(postList)
            account.fish_cluters.append(fishClusterName)
            account.push()
            ct.positiveMessage("NOME DE CARDUME DISPONÍVEL!")
            time.sleep(2)

            while True:
                action = Menu.create_fish_cluster()
                if action == "1":
                    add_user_in_fish_cluster(fishClusterName)
                elif action == "2":
                    remove_user_in_fish_cluster(fishClusterName)
                elif action == "3":
                    break
            Menu.profile()
            ct.positiveMessage("CARDUME CRIADO COM SUCESSO!")
            account.push()
            time.sleep(2)
            break


def add_user_in_fish_cluster(fishClusterName):
    accountsList = pull_accounts_list()

    while True:
        Menu.profile()
        userName = ct.inputStr("🐟", "NOME DO USUÁRIO")

        if userName in accountsList:
            ct.positiveMessage("USUÁRIO LOCALIZADO!")
            time.sleep(2)

            if fishClusterName not in accountsList[userName]["fish_cluters"]:
                accountsList[userName]["fish_cluters"].append(fishClusterName)
                push_accounts_list(accountsList)
                ct.positiveMessage("USUÁRIO ADICIONADO AO CARDUME!")
                time.sleep(2)
            else:
                ct.negativeMessage("USUÁRIO JÁ PERTENCE A ESSE CARDUME!")
                time.sleep(2)
            break
        else:
            ct.negativeMessage("USUÁRIO NÃO LOCALIZADO!")
            time.sleep(2)


def remove_user_in_fish_cluster(fishClusterName):
    accountsList = pull_accounts_list()

    while True:
        ct.clean()
        Menu.profile()
        userName = ct.inputStr("🐟", "NOME DO USUÁRIO")

        if userName in accountsList:
            ct.positiveMessage("USUÁRIO LOCALIZADO!")
            time.sleep(2)

            if fishClusterName in accountsList[userName]["fish_cluters"]:
                accountsList[userName]["fish_cluters"].remove(fishClusterName)
                push_accounts_list(accountsList)
                ct.positiveMessage("USUÁRIO REMOVIDO DO CARDUME!")
                time.sleep(2)
            else:
                ct.negativeMessage("USUÁRIO NÃO PERTENCE A ESSE CARDUME!")
                time.sleep(2)
            break
        else:
            ct.negativeMessage("USUÁRIO NÃO LOCALIZADO, TENTE NOVAMENTE!")
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
        fishClusterName = ct.inputStr("🐟", "NOME DO CARDUME")

        if fishClusterName in postList and fishClusterName != "ocean":
            ct.positiveMessage("CARDUME LOCALIZADO!")
            time.sleep(2)

            if fishClusterName in accountsList[perfilUser["user"]]["fish_cluters"]:
                accountsList[perfilUser["user"]]["fish_cluters"].remove(fishClusterName)
                push_accounts_list(accountsList)
                ct.positiveMessage("SAÍDA NO CARDUME COM SUCESSO!")
                time.sleep(2)
            else:
                ct.negativeMessage("VOCÊ NÃO PERTENCE A ESSE CARDUME!")
                time.sleep(2)

            break

        else:
            ct.negativeMessage("CARDUME NÃO LOCALIZADO, TENTE NOVAMENTE!")
            time.sleep(1)


def feed_of_fish_cluters(account):
    postList = pull_post_list()
    account.pull()

    while True:
        action = Menu.post_feed_of_fish_cluters(account)
        if action == 1:
            break
        elif action <= len(account.fish_cluters) + 1:
            if len(postList[account.fish_cluters[action - 2]]) > 0:
                feed(account, account.fish_cluters[action - 2])
            else:
                Menu.profile()
                ct.negativeMessage("NÃO EXISTE POSTS NESSE CARDUME!")
                time.sleep(2)
