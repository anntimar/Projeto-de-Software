import time
from classs.banner import Banner
from classs.customTerminal import CustomTerminal as ct
from classs.postFile import *


def app_data():
    Banner.profile()
    text = ["NÚMERO DE CONTAS ATIVAS", "NÚMERO DE COMUNIDADES"]
    obj = [AccountsFile(), PostsFile()]

    for i in range(0, 2):
        ct.print(text[i], str(obj[i].len()))
    time.sleep(4)
