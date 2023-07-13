from banner import *
from actions import *
from quiz import *
from menus import *

import time
import pwinput

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()


import json

accountDict = {}

with open("FishNet/accountsList.json") as f:
    accountDict = json.load(f)


# =================================================================
def newAccount(user, password, email):
    global accountDict
    newAccountDict = {
        "user": user,
        "password": password,
        "email": email,
        "first_login": True,
        "type_of_fish": "",
    }
    accountDict[user] = newAccountDict
    attAccountDict()


# =================================================================
def attAccountDict():
    with open(
        "FishNet/accountsList.json",
        "w",
    ) as file:
        json.dump(accountDict, file, indent=4)


# =================================================================
def login():
    clean_terminal()
    login_banner()

    userName = input(f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DE USUARIO ▷  {Fore.YELLOW}")
    userName = str(userName).lower()
    print(f"{Style.RESET_ALL}")

    userPassword = pwinput.pwinput(
        f"{Fore.YELLOW} 🔑{Fore.CYAN}  SENHA  ▷  {Fore.YELLOW}"
    )
    userPassword = str(userPassword).lower()
    print(f"{Style.RESET_ALL}")

    clean_terminal()
    login_banner()

    if (
        userName in accountDict
        and accountDict[userName]["user"] == userName
        and accountDict[userName]["password"] == userPassword
    ):
        print("")
        print(f"{Fore.GREEN} ✔  LOGIN REALIZADO COM SUCESSO!{Style.RESET_ALL}")
        time.sleep(1)
        if accountDict[userName]["first_login"] == True:
            personality_quiz()
            accountDict[userName]["type_of_fish"] = personality_quiz()
            attAccountDict()

            accountDict[userName]["first_login"] = False
            with open(
                "FishNet/accountsList.json",
                "w",
            ) as file:
                json.dump(accountDict, file, indent=4)
        d = 0
        while d == 0:
            clean_terminal()
            print("PRESSIONE Q PARA SAIR")
            print()
            action = input("ESCOLHA UMA OPÇÃO:")
            action = action.lower()
            action = action[0]
            clean_terminal()
            if action == "q":
                d = 1
            clean_terminal()
    else:
        print("")
        print(f"{Fore.RED} ✖  USUARIO OU SENHA INCORRETOS!{Style.RESET_ALL}")
        time.sleep(1)


# =================================================================


# =================================================================
def create_account():
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

        if userName in accountDict:
            print(f"{Fore.RED} ✖  NOME DE USUARIO INDISPONÍVEL{Style.RESET_ALL}")
            time.sleep(1)
        else:
            break
    print("")
    print(
        f"{Fore.YELLOW} ➥   {Fore.CYAN}SEU NOME DE USUARIO É ▷  {Fore.YELLOW}{userName}{Style.RESET_ALL}"
    )

    # if userName in accountDict:

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

    newAccount(userName, userPassword, userEmail)

    print("")
    print(f"{Fore.GREEN} ✔  CONTA CRIADA COM SUCESSO{Style.RESET_ALL}")

    time.sleep(2)


# =================================================================


clean_terminal()
time.sleep(1)

while True:
    action = main_menu()
    clean_terminal()

    if action == "1":
        login()
    elif action == "2":
        create_account()
    elif action == "3":
        break
