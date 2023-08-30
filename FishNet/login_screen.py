import time

from quiz import personality_quiz
from profile_screen import profile
from classs.customTerminal import CustomTerminal as ct
from classs.account import Account
from classs.banner import Banner


def login():
    Banner.login()

    user = ct.inputStr("🐟", "NOME DE USÚARIO")
    ct.jumpLine()
    password = ct.inputPassword("SENHA")
    ct.jumpLine()

    Banner.login()
    try:
        account = Account(user)
        if account.password == password:
            ct.jumpLine()
            ct.positiveMessage("LOGIN REALIZADO COM SUCESSO!")
            time.sleep(1)
            if account.first_login == True:
                time.sleep(3)
                account.first_login = False
                account.type_of_fish = personality_quiz()
                account.push()
            profile(account)
        else:
            ct.jumpLine()
            ct.negativeMessage("SENHA INCORRETA!")
            time.sleep(1)
    except:
        ct.jumpLine()
        ct.negativeMessage("USÚARIO NÃO ENCONTRADO!")
        time.sleep(1)
