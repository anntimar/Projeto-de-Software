from colorama import Fore
from colorama import Style
from actions import clean_terminal
from banner import *


def main_menu():
    clean_terminal()
    main_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}LOGIN{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}CRIAR CONTA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}SAIR{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]


def profile_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}POSTAR{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}FEED{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}EDITAR CONTA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➃ {Fore.CYAN}SAIR{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]


def edit_account_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}EDITAR NOME DE USUÁRIO{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}EDITAR SENHA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}EDITAR EMAIL{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➃ {Fore.CYAN}EXCLUIR CONTA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➄ {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]


def delete_account_menu():
    clean_terminal()
    print(
        f"{Fore.YELLOW} ☹  {Fore.CYAN}TEM CERTEZA QUE DESEJA EXCLUIR A CONTA?{Style.RESET_ALL}"
    )
    print("")
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}SIM{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}NÃO{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]


# edit_account_menu()  # teste unitario
# profile_menu()  # teste unitario
# main_menu()  # teste unitario
