import time
import pwinput
from classs.postFile import *
from profile_screen import profile
from banner import *
from actions import *
from quiz import *
from colorama import Fore
from colorama import Style
from classs.account import Account


def login():
    login_banner()

    user = input(f"{Fore.YELLOW} 🐟 {Fore.CYAN} NOME DE USÚARIO ▷  {Fore.YELLOW}")
    user = str(user).lower()
    print(f"{Style.RESET_ALL}")
    password = pwinput.pwinput(f"{Fore.YELLOW} 🔑{Fore.CYAN}  SENHA  ▷  {Fore.YELLOW}")
    password = str(password).lower()
    print(f"{Style.RESET_ALL}")

    login_banner()
    try:
        account = Account(user)
        if account.password == password:
            print("")
            print(f"{Fore.GREEN} ✔  LOGIN REALIZADO COM SUCESSO!{Style.RESET_ALL}")
            time.sleep(1)
            if account.first_login == True:
                time.sleep(3)
                account.first_login = False
                account.type_of_fish = personality_quiz()
                account.push()
            profile(account)
        else:
            print("")
            print(f"{Fore.RED} ✖ SENHA INCORRETA!{Style.RESET_ALL}")
            time.sleep(1)
    except:
        print("")
        print(f"{Fore.RED} ✖  USÚARIO NÃO ENCONTRADO!{Style.RESET_ALL}")
        time.sleep(1)
