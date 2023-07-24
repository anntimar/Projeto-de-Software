import time
from colorama import Fore
from colorama import Style
from banner import profile_banner
from menus import *
from post_list_actions import *
from accounts_list_actions import *
from actions import *


def fish_cluter_screen(perfilUser):
    while True:
        action = fish_cluster_menu()
        if action == "1":
            break
        elif action == "2":
            crate_fish_cluster(perfilUser)
        elif action == "3":
            enter_user_in_fish_cluster(perfilUser)
        elif action == "4":
            exit_user_in_fish_cluster(perfilUser)
        elif action == "7":
            enter_user_in_fish_cluster(perfilUser)
            break


def crate_fish_cluster(perfilUser):
    accountsList = pull_accounts_list()
    postList = pull_post_list()

    while True:
        clean_terminal()
        profile_banner()
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
            accountsList[perfilUser["user"]]["fish_cluters"].append(fishClusterName)
            push_post_list(postList)
            print(f"{Fore.GREEN} ✔  NOME DE CARDUME DISPONÍVEL!{Style.RESET_ALL}")
            time.sleep(1)
            while True:
                action = create_fish_cluster_menu()
                if action == "1":
                    add_user_in_fish_cluster(fishClusterName)
                elif action == "2":
                    remove_user_in_fish_cluster(fishClusterName)
                elif action == "3":
                    break
            clean_terminal()
            profile_banner()
            print(f"{Fore.GREEN} ✔  CARDUME CRIADO COM SUCESSO!{Style.RESET_ALL}")
            time.sleep(1)
            break


def add_user_in_fish_cluster(fishClusterName):
    accountsList = pull_accounts_list()

    while True:
        clean_terminal()
        profile_banner()
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
        clean_terminal()
        profile_banner()
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
        clean_terminal()
        profile_banner()
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
        clean_terminal()
        profile_banner()
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
