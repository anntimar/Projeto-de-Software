from post_list_actions import *


def postPull(perfilUser, feedlist, text):
    postList = pull_post_list()
    postList[feedlist].append(
        {
            "type_of_fish": perfilUser["type_of_fish"].upper(),
            "userName": perfilUser["user"],
            "bubbles": [],
            "pops": [],
            "content": text,
        },
    )
    push_post_list(postList)
