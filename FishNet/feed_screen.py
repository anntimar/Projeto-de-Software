from actions import clean_terminal
from menus import feed_menu
from post_list_actions import *


def feed():
    indexPost = 0
    while True:
        clean_terminal()
        postList = pull_post_list()
        posts = postList["geral"][indexPost]
        action = feed_menu(posts)
        if action == "3":
            if indexPost == 0:
                indexPost = len(postList["geral"]) - 1
            else:
                indexPost -= 1
        elif action == "4":
            if indexPost == len(postList["geral"]) - 1:
                indexPost = 0
            else:
                indexPost += 1
        elif action == "5":
            break
