import time
from colorama import Fore
from colorama import Style
from accounts_list_actions import pull_accounts_list
from actions import clean_terminal
from fish_data import *
from banner import *


def input_int():
    try:
        return int(input(f"{Fore.CYAN} ▷  {Fore.YELLOW}"))
    except:
        return 0


def input_str():
    try:
        return input(f"{Fore.CYAN} ▷  {Fore.YELLOW} ").upper()
    except:
        return "0"


def main_menu():
    clean_terminal()
    main_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}SAIR{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}LOGIN{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}CRIAR CONTA{Style.RESET_ALL}")
    print("")
    return input_int()


def profile_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}POSTAR{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}FEED OCEANO{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}CARDUMES{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➃ {Fore.CYAN}PEIXES AMIGOS{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➄ {Fore.CYAN}EDITAR CONTA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➅ {Fore.CYAN}SAIR{Style.RESET_ALL}")
    print("")
    return input_str()


def following_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}ADICIONAR PEIXE AMIGO{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}REMOVER PEIXE AMIGO{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}VER LISTA DE PEIXE AMIGOS{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➃ {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]


def create_fish_cluster_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}ADICONAR PEIXE EM UM CARDUME{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}REMOVER PEIXE DE UM CARDUME{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}FINALIZAR{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]


def fish_cluster_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}FEED DOS CARDUMES{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}CRIAR CARDUME{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}ENTRAR EM UM CARDUME{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➃ {Fore.CYAN}SAIR DE UM CARDUME{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➄ {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
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


def feed_of_fish_cluters_menu(account):
    numbers = ["", "➀", "➁", "➂", "➃", "➄", "➅", "➆", "➇", "➈", "➉"]

    clean_terminal()
    profile_banner()

    if len(account.fish_cluters) == 0:
        print(f"{Fore.RED} ✖  VOCÊ NÃO ESTÁ EM NEM UM CARDUME!{Style.RESET_ALL}")
        time.sleep(2)
    else:
        j = 0
        for i in account.fish_cluters:
            j += 1
            print(f"{Fore.YELLOW} {numbers[j]} {Fore.CYAN}{i}{Style.RESET_ALL}")

        j += 1
        print(f"{Fore.YELLOW} {numbers[j]} {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
        print("")
        action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
        Style.RESET_ALL
        action = action.upper()
        return action[0]

    return "0"


def post_feed_of_fish_cluters_menu(account):
    numbers = ["", "➀", "➁", "➂", "➃", "➄", "➅", "➆", "➇", "➈", "➉"]

    clean_terminal()
    profile_banner()

    if len(account.fish_cluters) == 0:
        print(f"{Fore.RED} ✖  VOCÊ NÃO ESTÁ EM NEM UM CARDUME!{Style.RESET_ALL}")
        time.sleep(2)
    else:
        j = 0
        for i in account.fish_cluters:
            j += 1
            print(f"{Fore.YELLOW} {numbers[j]} {Fore.CYAN}{i}{Style.RESET_ALL}")

        j += 1
        print(f"{Fore.YELLOW} {numbers[j]} {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
        print("")
        action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
        Style.RESET_ALL
        action = action.upper()
        return action[0]

    return "0"


def delete_account_menu():
    clean_terminal()
    profile_banner()
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


def feed_menu(post):
    textSize = 140
    clean_terminal()
    typeOfFish = fishIcon[post["type_of_fish"]]
    userName = post["userName"]
    bubble = len(post["bubbles"])
    pops = len(post["pops"])
    content = post["content"]
    textNull = ""
    barText = ""

    for i in range(textSize):
        barText = barText + "═"
    for i in range(textSize - (len(userName) + 1)):
        userName = userName + " "
    for i in range((textSize - len(content)) + 3):
        content = content + " "
    for i in range(textSize):
        textNull = textNull + " "

    print(f"{Fore.YELLOW}╔════╦{barText}╗{Style.RESET_ALL}")
    print(
        f"{Fore.YELLOW}║ {typeOfFish}  ║{Fore.CYAN}{userName}{Fore.YELLOW}║{Style.RESET_ALL}"
    )
    print(f"{Fore.YELLOW}╠════╩{barText}╣{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}║ {Fore.CYAN}{content}{Fore.YELLOW} ║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}╚═════{barText}╝{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ◯  {bubble}   ✴  {pops}{Style.RESET_ALL}")
    print("")
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN} ◯  INFLAR BOLHA     {Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN} ✴  ESTOURAR BOLHA{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN} ⮜  ANTERIOR      {Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➃ {Fore.CYAN} ⮞  PRÓXIMO     {Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➄ {Fore.CYAN} ⮨  VOLTAR     {Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    # ⏱
    return action[0]


def post_menu():
    clean_terminal()
    profile_banner()
    print(f"{Fore.YELLOW} ➀ {Fore.CYAN}PORTAR NO OCEANO{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➁ {Fore.CYAN}POSTAR EM UM CARDUME{Style.RESET_ALL}")
    print(f"{Fore.YELLOW} ➂ {Fore.CYAN}VOLTAR{Style.RESET_ALL}")
    print("")
    action = input(f"{Fore.CYAN} ▷  {Fore.YELLOW}")
    Style.RESET_ALL
    action = action.upper()
    return action[0]
