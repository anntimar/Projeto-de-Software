import time

from quiz import personality_quiz
from profile_screen import profile
from classs.customTerminal import CustomTerminal as ct
from classs.account import Account
from classs.banner import Banner


def login():
    Banner.login()
    user = ct.inputStr("🐟", "NOME DE USÚARIO")

    Banner.login()
    password = ct.inputPassword("SENHA")

    Banner.login()
    try:
        account = Account(user)
        if account.password == password:
            ct.positiveMessage("LOGIN REALIZADO COM SUCESSO!")
            time.sleep(1)
            if account.first_login == True:
                time.sleep(3)
                account.first_login = False
                account.type_of_fish = personality_quiz()
                account.push()
            try:
                profile(account)
            except:
                ct.negativeMessage("ERRO NO profile_screen")
                time.sleep(2)
        else:
            ct.negativeMessage("SENHA INCORRETA!")
            time.sleep(2)
    except:
        ct.negativeMessage("USÚARIO NÃO ENCONTRADO!")
        time.sleep(2)
