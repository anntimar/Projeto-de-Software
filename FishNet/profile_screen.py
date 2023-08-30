from fish_friends import *
from create_fish_cluster_screen import *
from create_post import createPost
from feed_screen import feed
from edit_account_screen import edit_account
from accounts_list_actions import *
from menus import profile_menu
from actions import clean_terminal


def profile(account):
    account.pull()
    while True:
        action = profile_menu()
        if action == "1":
            createPost(account)
        elif action == "2":
            feed(account, "ocean")
        elif action == "3":
            fish_cluter_screen(account)
        elif action == "4":
            fish_friends(account)
        elif action == "5":
            if not edit_account(account):
                return False
        elif action == "6":
            break
    account.push()
