# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from instagrapi import Client
from auth_file import inst_login, inst_password
import psycopg2
from psycopg2 import Error
from peewee import *


def loveRate(user_id, user_info, count_of_posts) -> float:
    followers_count = user_info.follower_count
    medias = cl.user_medias(user_id, count_of_posts)
    likes = 0
    for media in medias:
        likes += media.like_count
        # print("done")
    return likes / (count_of_posts * followers_count) * 100


# TODO: add a Love Rate - likes/subscribers * 100%


def talkRate(user_id, user_info, count_of_posts) -> float:
    followers_count = user_info.follower_count
    medias = cl.user_medias(user_id, count_of_posts)
    comments = 0
    for media in medias:
        comments += media.comment_count
        # print("done")
    return comments / (count_of_posts * followers_count) * 100


# TODO: add a Talk Rate - comments/subscribers * 100%


def engagementRate(user_id, user_info, count_of_posts):
    followers_count = user_info.follower_count
    medias = cl.user_medias(user_id, count_of_posts)
    reactions = 0
    for media in medias:
        reactions += media.like_count
        reactions += media.comment_count
    return reactions / (count_of_posts * followers_count) * 100


# TODO: add an Engagement Rate - Reactions/(count of post * followers)


def engagementRateReach(user_id, user_info, count_of_posts):
    medias = cl.user_medias(user_id, count_of_posts)
    reactions = 0
    reach = 0
    for media in medias:
        reactions += media.like_count
        reactions += media.comment_count
        reach += media.view_count
    avg_reach = reach / count_of_posts
    return reactions / (count_of_posts * avg_reach) * 100

# It works only with Business accounts!!!
# TODO: add an Engagement Rate Reach - Reactions/(count of post * average_reach)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cl = Client()
    cl.login(inst_login, inst_password)
    user_id = cl.user_id_from_username("hse_gsb")
    user_info = cl.user_info(user_id)
    media_count = 18
    print("setup is ready")
    print(user_info.is_private)
    print(user_info.media_count)
    print(user_info.biography)
    print(f"{round(loveRate(user_id, user_info, media_count), 1)}% - likes per 100 follower")
    print(f"{round(talkRate(user_id, user_info, media_count), 1)}% - comments per 100 follower")
    print(f"{round(engagementRate(user_id, user_info, media_count), 1)}% - reactions per 100 follower")
    print(user_info.is_business)
    # if not user_info.is_business:
    #     print("This account isn't a business account")
    # else:
    #     print(f"{round(engagementRateReach(user_id, user_info, media_count), 1)}% - reactions per 100 reached")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
