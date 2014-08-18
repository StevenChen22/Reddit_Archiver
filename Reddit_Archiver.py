# Copyright 2014(c) Steven Chen
# Uses PRAW to archive Reddit posts from u/CityofVancouver

import praw

user_agent = ("Reddit Archiver 1.0 by /u/CityofVancouver"\
                "https://github.com/StevenChen22/Reddit_Archiver")

r = praw.Reddit(user_agent=user_agent)

user_name = "CityofVancouver"
user = r.get_redditor(user_name)

comments = user.get_comments()
submitted = user.get_submitted()

#for i in comments and submnitted:
    # add it to a file?
