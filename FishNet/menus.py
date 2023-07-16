from colorama import Fore
from colorama import Style
from actions import clean_terminal
from dic import *
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


# post = {
#     "type_of_fish": "𓆛",
#     "userName": "thiago_fellype",
#     "bubble": 5,
#     "pops": 5,
#     "content": "Viver é a coisa mais rara do mundo. A maioria das pessoas apenas existe",
# }

# feed_menu(post)
# edit_account_menu()  # teste unitario
# profile_menu()  # teste unitario
# main_menu()  # teste unitario
