from post_list_actions import *


def postPull(account, feedlist, text):
    postList = pull_post_list()
    postList[feedlist].append(
        {
            "type_of_fish": account.type_of_fish,
            "userName": account.user,
            "bubbles": [],
            "pops": [],
            "content": text,
        },
    )
    push_post_list(postList)
