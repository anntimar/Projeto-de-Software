# Cluster class

import time
from fish_data import *
from classs.banner import *

from classs.customTerminal import CustomTerminal as ct


class Menu:
    def main():
        Banner.main()
        ct.print("➀", "SAIR")
        ct.print("➁", "LOGIN")
        ct.print("➂", "CRIAR CONTA")
        ct.jumpLine()
        return ct.inputInt()

    def profile():
        Banner.profile()
        ct.print("➀", "SAIR")
        ct.print("➁", "POSTAR")
        ct.print("➂", "FEED OCEANO")
        ct.print("➃", "CARDUMES")
        ct.print("➄", "PEIXES AMIGOS")
        ct.print("➅", "EDITAR CONTA")
        ct.jumpLine()
        return ct.inputInt()

    def following():
        Banner.profile()
        ct.print("➀", "ADICIONAR PEIXE AMIGO")
        ct.print("➁", "REMOVER PEIXE AMIGO")
        ct.print("➂", "VER LISTA DE PEIXE AMIGOS")
        ct.print("➃", "VOLTAR")
        ct.jumpLine()
        return ct.inputStr()

    def create_fish_cluster():
        Banner.profile()
        ct.print("➀", "ADICONAR PEIXE EM UM CARDUME")
        ct.print("➁", "REMOVER PEIXE DE UM CARDUME")
        ct.print("➂", "FINALIZAR")
        ct.jumpLine()
        return ct.inputStr()

    def fish_cluster():
        Banner.profile()
        ct.print("➀", "VOLTAR")
        ct.print("➁", "FEED DOS CARDUMES")
        ct.print("➂", "CRIAR CARDUME")
        ct.print("➃", "ENTRAR EM UM CARDUME")
        ct.print("➄", "SAIR DE UM CARDUME")
        ct.jumpLine()
        return ct.inputInt()

    def edit_account():
        Banner.profile()
        ct.print("➀", "EDITAR NOME DE USUÁRIO")
        ct.print("➁", "EDITAR SENHA")
        ct.print("➂", "EDITAR EMAIL")
        ct.print("➃", "EXCLUIR CONTA")
        ct.print("➄", "VOLTAR")
        ct.jumpLine()
        return ct.inputStr()

    def post():
        Banner.profile()
        ct.print("➀", "VOLTAR")
        ct.print("➁", "PORTAR NO OCEANO")
        ct.print("➂", "POSTAR EM UM CARDUME")
        ct.jumpLine()
        return ct.inputInt()

    def post_feed_of_fish_cluters(account):
        numbers = ["", "➀", "➁", "➂", "➃", "➄", "➅", "➆", "➇", "➈", "➉"]

        Banner.profile()

        if len(account.fish_cluters) == 0:
            ct.negativeMessage("VOCÊ NÃO ESTÁ EM NEM UM CARDUME!")
            time.sleep(2)
        else:
            j = 1
            ct.print(numbers[j], "VOLTAR")
            for i in account.fish_cluters:
                j += 1
                ct.print(numbers[j], i)

            ct.jumpLine()
            return ct.inputInt()

        return "0"

    def delete_account():
        Banner.profile()
        ct.print("☹", "TEM CERTEZA QUE DESEJA EXCLUIR A CONTA?")
        ct.jumpLine()
        ct.print("➀", "SIM")
        ct.print("➁", "NÃO")
        ct.jumpLine()
        return ct.inputStr()

    def feed(post):
        ct.clean()
        typeOfFish = fishIcon[post["type_of_fish"]]
        userName = post["userName"]
        content = post["content"]
        bubble = len(post["bubbles"])
        pops = len(post["pops"])

        ct.post(typeOfFish, userName, content, bubble, pops)
        ct.jumpLine()
        ct.print("➀", " ◯  INFLAR BOLHA     ")
        ct.print("➁", " ✴  ESTOURAR BOLHA")
        ct.print("➂", " ⮜  ANTERIOR      ")
        ct.print("➃", " ⮞  PRÓXIMO     ")
        ct.print("➄", " ⮨  VOLTAR     ")
        ct.jumpLine()
        return ct.inputStr()
