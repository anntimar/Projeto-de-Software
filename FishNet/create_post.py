from post_pull import postPull
from menus import post_menu


def createPost(perfilUser):
    while True:
        action = post_menu()
        if action == "1":
            postPull(perfilUser, "ocean", input("digite seu post"))
            break
        elif action == "2":
            break
        elif action == "3":
            break
