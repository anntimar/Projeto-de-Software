import time
import pwinput
from accounts_list_actions import *
from menus import *
from actions import clean_terminal
from colorama import Fore
from colorama import Style


def edit_account(perfilUser):
    while True:
        action = edit_account_menu()
        if action == "1":
            edit_user_name(perfilUser)
        elif action == "2":
            edite_password(perfilUser)
        elif action == "3":
            edite_email(perfilUser)
        elif action == "4":
            if not delete_account(perfilUser):
                return False
        elif action == "5":
            break

    return True


def edit_user_name(perfilUser):
    clean_terminal()
    accountsList = pull_accounts_list()

    while True:
        userName = input(
            f"{Fore.YELLOW} ㋡ {Fore.CYAN} ESCOLHA UM NOVO NOME DE USUÁRIO ▷  {Fore.YELLOW}"
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
            print(f"{Fore.RED} ✖  NOME DE USUÁRIO INDISPONÍVEL{Style.RESET_ALL}")
            time.sleep(1)
        else:
            break
    print("")
    print(
        f"{Fore.YELLOW} ➥   {Fore.CYAN}SEU NOME DE USUÁRIO É ▷  {Fore.YELLOW}{userName}{Style.RESET_ALL}"
    )
    print(f"{Style.RESET_ALL}")

    del accountsList[perfilUser["user"]]

    perfilUser["user"] = userName

    accountsList[userName] = perfilUser
    push_accounts_list(accountsList)

    time.sleep(2)

    clean_terminal()
    print(f"{Fore.GREEN} ✔  NOME DE USUÁRIO EDITADO COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)


def edite_password(perfilUser):
    clean_terminal()
    accountsList = pull_accounts_list()
    key1 = "/"
    key2 = "*"
    while key1 != key2:
        userPassword = pwinput.pwinput(
            f"{Fore.YELLOW} 🔑 {Fore.CYAN} ESCOLHA UMA NOVA SENHA ▷  {Fore.YELLOW}"
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

    userPassword = str(key2)
    userPassword = userPassword.lower()

    accountsList[perfilUser["user"]]["password"] = userPassword
    push_accounts_list(accountsList)

    clean_terminal()
    print(f"{Fore.GREEN} ✔  SENHA EDITADA COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)


def edite_email(perfilUser):
    clean_terminal()
    accountsList = pull_accounts_list()

    userEmail = input(
        f"{Fore.YELLOW} ✉ {Fore.CYAN} INFORME O NOVO E-MAIL ▷  {Fore.YELLOW}"
    )
    userEmail = str(userEmail)
    userEmail = userEmail.lower()

    accountsList[perfilUser["user"]]["email"] = userEmail
    push_accounts_list(accountsList)

    clean_terminal()
    print(f"{Fore.GREEN} ✔  E-MAIL EDITADA COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)


def delete_account(perfilUser):
    while True:
        action = delete_account_menu()
        if action == "1":
            accountsList = pull_accounts_list()
            del accountsList[perfilUser["user"]]
            push_accounts_list(accountsList)
            clean_terminal()
            print(f"{Fore.GREEN} ✔  CONTA EXCLUIDA COM SUCESSO{Style.RESET_ALL}")
            time.sleep(2)
            return False
        elif action == "2":
            clean_terminal()
            print(
                f"{Fore.GREEN} ✔  OBRIGADO POR NÃO EXCLUIR SUA CONTA!{Style.RESET_ALL}"
            )
            time.sleep(2)
            return True
