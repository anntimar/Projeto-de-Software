from colorama import Fore
from colorama import Style
from actions import clean_terminal
from banner import main_banner


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


# main_menu()  # teste unitario
