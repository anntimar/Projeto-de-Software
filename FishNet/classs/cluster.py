# Cluster class
from post_list_actions import *
from accounts_list_actions import *


class Cluster:
    def __init__(self, clusterName, creatorUser):
        accountsList = pull_accounts_list()
        postList = pull_post_list()

        self.clusterName = clusterName
        self.creatorUser = creatorUser
        postList[clusterName] = []
        accountsList[creatorUser]["fish_cluters"].append(clusterName)

        push_accounts_list(accountsList)
        push_accounts_list(postList)

    def post(self, post):
        postList = pull_post_list()
        postList[self.clusterName] = post
        push_accounts_list(postList)
