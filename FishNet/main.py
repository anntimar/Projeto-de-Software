from banner import *
from actions import *
from menus import *
from login_screen import login
from create_account_screen import create_account
from colorama import init as colorama_init

colorama_init()


clean_terminal()
while True:
    action = main_menu()
    if action == "1":
        login()
    elif action == "2":
        create_account()
    elif action == "3":
        break
