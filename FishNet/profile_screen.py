from feed_screen import feed
from edit_account_screen import edit_account
from accounts_list_actions import *
from menus import profile_menu
from actions import clean_terminal
from colorama import Fore
from colorama import Style


def profile(perfilUser):
    accountsList = pull_accounts_list()
    while True:
        clean_terminal()
        action = profile_menu()
        if action == "1":
            break
        elif action == "2":
            feed()
        elif action == "3":
            if not edit_account(perfilUser):
                return False
        elif action == "4":
            break
    push_accounts_list(accountsList)
