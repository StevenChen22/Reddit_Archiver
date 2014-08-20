# Copyright 2014(c) Steven Chen
# Uses PRAW to archive Reddit posts from u/CityofVancouver

# Import Python Reddit API Wrapper (PRAW) and time
import praw
import time
import datetime

debug = False

output_archive = open("archive.txt", "w")
already_archived = open("already_archived", "r+")

# Define print to external source function


# def add_comment_to_file(c):
# Submit Date
# Subreddit
# PermaLink to comment
# PermaLink to thread
# Text
# Parent or child comments?
# Points?

# Connect to Reddit and identify user and script
user_agent = ("Reddit Archiver 1.0 by /u/CityofVancouver"\
                "https://github.com/StevenChen22/Reddit_Archiver")
r = praw.Reddit(user_agent)

# Specify Redditor
user_name = "CityofVancouver"
user = r.get_redditor(user_name)

# List of already archived submissions
if debug == True:
    print("Logged in")

# Get comments and submissions made by user
comments = user.get_comments(limit = 25)
if debug == True:
    print("Got Comments")
submitted = user.get_submitted(limit = 10)
if debug == True:
    print("Got Submissions")

# While loop - beause it's a Bot
while True:
    if debug == True:
        print("Started Loop")

    # Check comments
    for i in comments:
        if debug == True:
            print("Started comment loop")
        if i.id not in already_archived:
            # Add it to a file:
            # Title
            # Submit Date
            # Subreddit
            # praw.objects.Comment.permaLink
            # Self text or URL
            # Comments?
            # Points?
            already_archived.append(i.id)
            #output_archive.write(i.selftext + "\n")

    # Check submitted posts
    for j in submitted:
        if debug == True:
            print("Started submission loop")

        if j.id not in already_archived:
            already_archived.write(j.id + "\n")
            # Get submission datetime
            timestamp = j.created_utc
            dt = datetime.datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
            # Write to archive
            output_archive.write("Submission Date: \n" + dt + "\n\n")
            output_archive.write("Permalink: \n" + str(j.permalink) + "\n\n")
            output_archive.write("Subreddit: \n" + str(j.subreddit) + "\n\n")
            output_archive.write("Post Score: \n" + str(j.score) + "\n\n")
            output_archive.write("Title: \n" + str(j.title) + "\n\n")
            # See if self post or not and write self text body or link
            if j.is_self == True:
                output_archive.write("Body: \n" + str(j.selftext) + "\n\n")
            elif j.is_self == False:
                output_archive.write("Link: \n" + str(j.url) + "\n\n")

    # Set frequency of run
    if debug == True:
        print("Finished loops!")

#    time.sleep(86400)

output_archive.close()
