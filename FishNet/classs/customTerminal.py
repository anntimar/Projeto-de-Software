# CustomTerminal class

import os
import pwinput
from colorama import Fore
from colorama import Style
from colorama import init as colorama_init


class CustomTerminal:
    def __init__(self):
        colorama_init()

    def positiveMessage(text):
        print(f"{Fore.GREEN} ✔  {text}")

    def negativeMessage(text):
        print(f"{Fore.RED} ✖  {text}")

    def print(icon, text):
        print(f"{Fore.YELLOW} {icon} {Fore.CYAN} {text}")

    def inputStr():
        try:
            return str(input(f"{Fore.CYAN} ▷  {Fore.YELLOW} ")).lower()
        except:
            return "0"

    def inputStr(icon, text):
        try:
            return str(
                input(f"{Fore.YELLOW} {icon} {Fore.CYAN} {text} ▷  {Fore.YELLOW}")
            ).lower()
        except:
            return "0"

    def inputInt():
        try:
            return int(input(f"{Fore.CYAN} ▷  {Fore.YELLOW}"))
        except:
            return 0

    def jumpLine():
        print("")

    def jumpLine():
        print("")

    def reset(self):
        Style.RESET_ALL

    def clean():
        os.system("cls") or None

    def post(typeOfFish, userName, content, bubble, pops):
        textSize = 140
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

    def inputPassword(text):
        try:
            return str(
                pwinput.pwinput(f"{Fore.YELLOW} 🔑{Fore.CYAN}  {text}  ▷  {Fore.YELLOW}")
            ).lower()
        except:
            return "0"

    def inputUserName(text):
        try:
            userName = str(
                input(f"{Fore.YELLOW} 🐟 {Fore.CYAN} {text}  ▷  {Fore.YELLOW}")
            )
            # ---------------------------------------
            userName = userName.replace(" ", "_")

            while "__" in userName:
                userName = userName.replace("__", "_")

            userName = userName.removesuffix("_")
            userName = userName.removeprefix("_")
            userName.lower()
            # ---------------------------------------

            return userName
        except:
            return "0"
