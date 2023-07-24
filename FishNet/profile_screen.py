from fish_friends import *
from create_fish_cluster_screen import *
from create_post import createPost
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
            createPost(perfilUser)
        elif action == "2":
            feed(perfilUser, "ocean")
        elif action == "3":
            fish_cluter_screen(perfilUser)
        elif action == "4":
            fish_friends(perfilUser)
        elif action == "5":
            if not edit_account(perfilUser):
                return False
        elif action == "6":
            break
    push_accounts_list(accountsList)
