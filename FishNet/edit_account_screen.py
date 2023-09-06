import time
import pwinput
from classs.account import Account
from classs.banner import Banner
from accounts_list_actions import *
from colorama import Fore
from colorama import Style
from classs.menu import Menu
from classs.customTerminal import CustomTerminal as ct


def edit_account(account):
    while True:
        match Menu.edit_account():
            case 1:
                break
            case 2:
                edit_user_name(account)
            case 3:
                edite_password(account)
            case 4:
                edite_email(account)
            case 5:
                if not delete_account(account):
                    return False
    return True


def edit_user_name(account):
    accountsList = pull_accounts_list()

    while True:
        Banner.profile()
        userName = ct.inputUserName("ESCOLHA UM NOVO NOME DE USUÁRIO")

        if userName in accountsList:
            Banner.profile()
            ct.negativeMessage("NOME DE USUÁRIO INDISPONÍVEL")
            time.sleep(1)
        else:
            break

    ct.jumpLine()
    ct.print("➥", "SEU NOME DE USUÁRIO É ▷  " + userName)
    try:
        del accountsList[account.user]
    except:
        ct.negativeMessage("CONTA NÃO APAGADA!")
        time.sleep(2)

    account.user = userName

    accountsList[userName] = account

    push_accounts_list(accountsList)

    time.sleep(2)

    ct.clean()
    ct.positiveMessage("NOME DE USUÁRIO EDITADO COM SUCESSO!")
    time.sleep(2)


def edite_password(account):
    ct.clean()
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

    accountsList[account["user"]]["password"] = userPassword
    push_accounts_list(accountsList)

    ct.clean()
    print(f"{Fore.GREEN} ✔  SENHA EDITADA COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)


def edite_email(account):
    ct.clean()
    accountsList = pull_accounts_list()

    userEmail = input(
        f"{Fore.YELLOW} ✉ {Fore.CYAN} INFORME O NOVO E-MAIL ▷  {Fore.YELLOW}"
    )
    userEmail = str(userEmail)
    userEmail = userEmail.lower()

    accountsList[account["user"]]["email"] = userEmail
    push_accounts_list(accountsList)

    ct.clean()
    print(f"{Fore.GREEN} ✔  E-MAIL EDITADA COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)


def delete_account(account):
    while True:
        action = Menu.delete_account()
        if action == "1":
            accountsList = pull_accounts_list()
            del accountsList[account["user"]]
            push_accounts_list(accountsList)
            ct.clean()
            print(f"{Fore.GREEN} ✔  CONTA EXCLUIDA COM SUCESSO{Style.RESET_ALL}")
            time.sleep(2)
            return False
        elif action == "2":
            ct.clean()
            print(
                f"{Fore.GREEN} ✔  OBRIGADO POR NÃO EXCLUIR SUA CONTA!{Style.RESET_ALL}"
            )
            time.sleep(2)
            return True
