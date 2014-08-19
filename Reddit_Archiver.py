# Copyright 2014(c) Steven Chen
# Uses PRAW to archive Reddit posts from u/CityofVancouver

# Import Python Reddit API Wrapper (PRAW)
import praw

# Connect to Reddit and identify user and script
user_agent = ("Reddit Archiver 1.0 by /u/CityofVancouver"\
                "https://github.com/StevenChen22/Reddit_Archiver")
r = praw.Reddit(user_agent=user_agent)

# Specify Redditor
user_name = "CityofVancouver"
user = r.get_redditor(user_name)

# List of already archived submissions
already_archived = []

# While loop - beause it's a Bot
while True:
    # Get comments and submissions made by user
    comments = user.get_comments(limit = 25)
    submitted = user.get_submitted(limit = 10)
    # Check to see if it has been already archived
    for submission in comments:
        if submission.id not in already_archived:
            # Add it to a file
            already_archived.append(submission.id)
    for submission in submitted:
        if submission.id not in already_archived:
            # Add it to a file
            already_archived.append(submission.id)
    # Set frequency of run
    time.sleep(86400)
