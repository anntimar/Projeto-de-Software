# from banner import *
# from actions import *
from menus import main_menu
from login_screen import login
from create_account_screen import create_account
from colorama import init as colorama_init

colorama_init()

while True:
    match main_menu():
        case 1:
            break
        case 2:
            login()
        case 3:
            create_account()
