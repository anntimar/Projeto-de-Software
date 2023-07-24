import time
from colorama import Fore
from colorama import Style
from actions import clean_terminal
from banner import profile_banner
from menus import following_menu
from accounts_list_actions import *


def fish_friends(perfilUser):
    while True:
        action = following_menu()
        if action == "1":
            add_fish_friend(perfilUser)
        elif action == "2":
            remove_fish_friend(perfilUser)
        elif action == "3":
            see_fish_friend(perfilUser)
        elif action == "4":
            break


def add_fish_friend(perfilUser):
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

            if userName not in accountsList[perfilUser["user"]]["fish_friends"]:
                accountsList[perfilUser["user"]]["fish_friends"].append(userName)
                push_accounts_list(accountsList)
                print(
                    f"{Fore.GREEN} ✔  USUÁRIO ADICIONADO AOS SEUS PEIXES AMIGOS!{Style.RESET_ALL}"
                )
                time.sleep(2)
            else:
                print(
                    f"{Fore.RED} ✖  USUÁRIO JÁ PERTENCE AOS SEUS PEIXES AMIGOS!{Style.RESET_ALL}"
                )
                time.sleep(2)
            break
        else:
            print(
                f"{Fore.RED} ✖  USUÁRIO NÃO LOCALIZADO, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(1)


def remove_fish_friend(perfilUser):
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

            if userName in accountsList[perfilUser["user"]]["fish_friends"]:
                accountsList[perfilUser["user"]]["fish_friends"].remove(userName)
                push_accounts_list(accountsList)
                print(
                    f"{Fore.GREEN} ✔  USUÁRIO REMOVIDO DO SEUS PEIXES AMIGOS!{Style.RESET_ALL}"
                )
                time.sleep(2)
            else:
                print(
                    f"{Fore.RED} ✖  USUÁRIO NÃO PERTENCE A0 SEUS PEIXES AMIGOS!{Style.RESET_ALL}"
                )
                time.sleep(2)
            break
        else:
            print(
                f"{Fore.RED} ✖  USUÁRIO NÃO LOCALIZADO, TENTE NOVAMENTE!{Style.RESET_ALL}"
            )
            time.sleep(1)


def see_fish_friend(perfilUser):
    accountsList = pull_accounts_list()
    clean_terminal()
    profile_banner()
    if len(accountsList[perfilUser["user"]]["fish_friends"]) == 0:
        print(f"{Fore.RED} ✖  VOCÊ NÃO TEM NEM UM PEIXE AMIGO!{Style.RESET_ALL}")
        time.sleep(2)
        return

    while True:
        clean_terminal()
        profile_banner()
        for i in accountsList[perfilUser["user"]]["fish_friends"]:
            print(f"{Fore.YELLOW} 🐟 {Fore.CYAN} {i}  {Fore.YELLOW}")

        print("")
        print(f"{Fore.YELLOW} ➀ {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
        print("")
        action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
        if action == "1":
            break
