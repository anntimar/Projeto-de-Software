from profile_screen import profile
from banner import *
from accounts_list_actions import *
from actions import *
from quiz import *

import time
import pwinput

from colorama import Fore
from colorama import Style


def login():
    accountsList = pull_accounts_list()
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
        userName in accountsList
        and accountsList[userName]["user"] == userName
        and accountsList[userName]["password"] == userPassword
    ):
        print("")
        print(f"{Fore.GREEN} ✔  LOGIN REALIZADO COM SUCESSO!{Style.RESET_ALL}")
        time.sleep(1)
        if accountsList[userName]["first_login"] == True:
            accountsList[userName]["type_of_fish"] = personality_quiz()
            time.sleep(3)
            accountsList[userName]["first_login"] = False
            push_accounts_list(accountsList)
        profile(accountsList[userName])
    else:
        print("")
        print(f"{Fore.RED} ✖  USUARIO OU SENHA INCORRETOS!{Style.RESET_ALL}")
        time.sleep(1)
