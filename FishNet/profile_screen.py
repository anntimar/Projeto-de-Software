from create_post import createPost
from feed_screen import feed
from fish_friends import fish_friends
from create_fish_cluster_screen import fish_cluter_screen
from edit_account_screen import edit_account

from classs.menu import Menu


def profile(account):
    account.pull()
    while True:
        match Menu.profile():
            case 1:
                break
            case 2:
                createPost(account)
            case 3:
                feed(account, "ocean")
            case 4:
                fish_cluter_screen(account)
            case 5:
                fish_friends(account)
            case 6:
                if not edit_account(account):
                    return False
    account.push()
