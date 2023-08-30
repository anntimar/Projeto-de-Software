from actions import clean_terminal
from menus import feed_menu
from post_list_actions import *


def feed(account, feedlist):
    indexPost = 0
    while True:
        clean_terminal()
        postList = pull_post_list()
        posts = postList[feedlist][indexPost]
        action = feed_menu(posts)
        if action == "1":
            if account.user != postList[feedlist][indexPost]["userName"]:
                if account.user in postList[feedlist][indexPost]["pops"]:
                    postList[feedlist][indexPost]["pops"].remove(account.user)
                if account.user not in postList[feedlist][indexPost]["bubbles"]:
                    postList[feedlist][indexPost]["bubbles"].append(account.user)

        elif action == "2":
            if account.user != postList[feedlist][indexPost]["userName"]:
                if account.user in postList[feedlist][indexPost]["bubbles"]:
                    postList[feedlist][indexPost]["bubbles"].remove(account.user)
                if account.user not in postList[feedlist][indexPost]["pops"]:
                    postList[feedlist][indexPost]["pops"].append(account.user)
        elif action == "3":
            if indexPost == 0:
                indexPost = len(postList[feedlist]) - 1
            else:
                indexPost -= 1
        elif action == "4":
            if indexPost == len(postList[feedlist]) - 1:
                indexPost = 0
            else:
                indexPost += 1
        elif action == "5":
            break
        push_post_list(postList)
