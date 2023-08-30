import time

from classs.banner import Banner
from classs.account import Account
from classs.postFile import postFile
from classs.customTerminal import CustomTerminal as ct


accounts = postFile("FishNet/file_data/accountsList.json")


def create_account():
    while True:
        Banner.create_account()
        userName = ct.inputUserName("INFORME SEU NOME DE USÚARIO")

        if userName in accounts.content:
            Banner.create_account()
            ct.negativeMessage("NOME DE USÚARIO INDISPONÍVEL")
            time.sleep(2)
        else:
            break

    Banner.create_account()
    ct.positiveMessage("SEU NOME DE USÚARIO É ▷  " + userName)

    time.sleep(2)

    key1 = "/"
    key2 = "*"
    while key1 != key2:
        Banner.create_account()
        key1 = ct.inputPassword("ESCOLHA UMA SENHA")

        Banner.create_account()
        key2 = ct.inputPassword("CONFIRME A SENHA")

        if key1 != key2:
            Banner.create_account()
            ct.negativeMessage("SENHAS DIFERENTES!")
            time.sleep(2)
        else:
            Banner.create_account()
            ct.positiveMessage("SENHA CONFIRMADA!")
            time.sleep(2)

    Banner.create_account()
    userEmail = ct.inputStr("✉", "INFORME SEU E-MAIL")

    Banner.create_account()
    ct.positiveMessage("E-MAIL CONFIRMADO!")
    time.sleep(2)

    Account(userName, key2, userEmail)

    Banner.create_account()
    ct.positiveMessage("CONTA CRIADA COM SUCESSO")
    time.sleep(2)
