from post_list_actions import push_post_list
from actions import clean_terminal
from post_pull import postPull
from menus import post_menu
from colorama import Fore
from colorama import Style


def createPost(perfilUser):
    while True:
        action = post_menu()
        if action == "1":
            clean_terminal()
            content = input(f"{Fore.CYAN} digite seu post ▷  {Fore.YELLOW}")
            postPull(perfilUser, "ocean", content)
            perfilUser["posts"].append(
                {
                    "type_of_fish": perfilUser["type_of_fish"],
                    "userName": perfilUser["user"],
                    "bubbles": [],
                    "pops": [],
                    "content": content,
                },
            )
            break
        elif action == "2":
            break
        elif action == "3":
            break
