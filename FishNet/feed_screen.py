from classs.menu import Menu
from classs.postFile import postFile
from classs.customTerminal import CustomTerminal as ct

post_file = postFile("FishNet/file_data/post_list.json")


def feed(account, feedlist):
    indexPost = 0
    while True:
        ct.clean()
        post_file.pull()
        posts = post_file.content[feedlist][indexPost]
        action = Menu.feed(posts)
        if action == "1":
            if account.user != post_file.content[feedlist][indexPost]["userName"]:
                if account.user in post_file.content[feedlist][indexPost]["pops"]:
                    post_file.content[feedlist][indexPost]["pops"].remove(account.user)
                if (
                    account.user
                    not in post_file.content[feedlist][indexPost]["bubbles"]
                ):
                    post_file.content[feedlist][indexPost]["bubbles"].append(
                        account.user
                    )

        elif action == "2":
            if account.user != post_file.content[feedlist][indexPost]["userName"]:
                if account.user in post_file.content[feedlist][indexPost]["bubbles"]:
                    post_file.content[feedlist][indexPost]["bubbles"].remove(
                        account.user
                    )
                if account.user not in post_file.content[feedlist][indexPost]["pops"]:
                    post_file.content[feedlist][indexPost]["pops"].append(account.user)
        elif action == "3":
            if indexPost == 0:
                indexPost = len(post_file.content[feedlist]) - 1
            else:
                indexPost -= 1
        elif action == "4":
            if indexPost == len(post_file.content[feedlist]) - 1:
                indexPost = 0
            else:
                indexPost += 1
        elif action == "5":
            break
        post_file.push()
