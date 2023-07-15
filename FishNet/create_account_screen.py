import time
import pwinput

from colorama import Fore, Style
from accounts_list_actions import *
from banner import create_account_banner


def new_account(user, password, email):
    accountsList = pull_accounts_list()
    newAccount = {
        "user": user,
        "password": password,
        "email": email,
        "first_login": True,
        "type_of_fish": "",
    }
    accountsList[user] = newAccount
    push_accounts_list(accountsList)


def create_account():
    accountsList = pull_accounts_list()
    create_account_banner()

    while True:
        userName = input(
            f"{Fore.YELLOW} ㋡ {Fore.CYAN} ESCOLHA UM NOME DE USUARIO ▷  {Fore.YELLOW}"
        )
        # ---------------------------------------
        userName = str(userName)
        userName = userName.lower()
        userName = userName.replace(" ", "_")

        while "__" in userName:
            userName = userName.replace("__", "_")

        userName = userName.removesuffix("_")
        userName = userName.removeprefix("_")
        # ---------------------------------------

        if userName in accountsList:
            print(f"{Fore.RED} ✖  NOME DE USUARIO INDISPONÍVEL{Style.RESET_ALL}")
            time.sleep(1)
        else:
            break
    print("")
    print(
        f"{Fore.YELLOW} ➥   {Fore.CYAN}SEU NOME DE USUARIO É ▷  {Fore.YELLOW}{userName}{Style.RESET_ALL}"
    )

    print(f"{Style.RESET_ALL}")

    key1 = "/"
    key2 = "*"
    while key1 != key2:
        userPassword = pwinput.pwinput(
            f"{Fore.YELLOW} 🔑 {Fore.CYAN} ESCOLHA UMA SENHA ▷  {Fore.YELLOW}"
        )
        key1 = str(userPassword)
        print(f"{Style.RESET_ALL}")

        userPassword = pwinput.pwinput(
            f"{Fore.YELLOW} 🔑 {Fore.CYAN} CONFIRME A SENHA ▷  {Fore.YELLOW}"
        )
        key2 = str(userPassword)
        print(f"{Style.RESET_ALL}")

        if key1 != key2:
            print(f"{Fore.RED} ✖  SENHAS DIFERENTES{Style.RESET_ALL}")
            print("")
        else:
            print(f"{Fore.GREEN} ✔  SENHA CONFIRMADA{Style.RESET_ALL}")
            print("")

    userPassword = str(key2)
    userPassword = userPassword.lower()

    userEmail = input(
        f"{Fore.YELLOW} ✉ {Fore.CYAN} INFORME SEU E-MAIL ▷  {Fore.YELLOW}"
    )
    userEmail = str(userEmail)
    userEmail = userEmail.lower()

    new_account(userName, userPassword, userEmail)

    print("")
    print(f"{Fore.GREEN} ✔  CONTA CRIADA COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)
