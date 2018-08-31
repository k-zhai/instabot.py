import os
import time
import getpass

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

users = []
pws = []
more = "Y"

def getInput(txt):
    while True:
        try:
            userInput = int(input(txt))
        except ValueError:
            print("Value must be a positive integer")
            continue
        else:
            if userInput > 0:
                break
            else:
                print("Value must be positive")

while (more == "Y" or more == "y"): 
    user = input("Enter username: ")
    pw = getpass.getpass("Enter password: ")
    users.append(user)
    pws.append(pw)
    more = input("Enter another account (Y/N)? ")

likes = input("Enter likes/day (<1000): ")
comments = input("Enter comments/day: ")
follows = input("Enter follows/day: ")
tags = [int(x) for x in input("Enter tags, separated by commas: ").replace(' ', '').split(',')]

comments = [["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],

for i in range (len(users)):
    bot = InstaBot(
        login=users[i],
        password=pws[i],
        like_per_day=likes,
        comments_per_day=comments,
        follow_per_day=follows,
        tag_list=tags,
        comment_list=comments,
        max_like_for_one_tag=50,
    )
    bot.new_auto_mod()
