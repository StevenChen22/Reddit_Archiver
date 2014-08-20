# Copyright 2014(c) Steven Chen
# Uses PRAW to archive Reddit posts from u/CityofVancouver

# Import Python Reddit API Wrapper (PRAW) and time
import praw
import time

debug = False

output_archive = open("archive.txt", "w")
already_archived = open("already_archived.txt", "r+")

# Connect to Reddit and identify user and script
user_agent = ("Reddit Archiver 1.0 by /u/CityofVancouver"\
                "https://github.com/StevenChen22/Reddit_Archiver")
r = praw.Reddit(user_agent)

# Specify Redditor
user_name = "CityofVancouver"
user = r.get_redditor(user_name)
if debug == True:
    print("Logged in")

# While loop - beause it's a Bot
while True:
    if debug == True:
        print("Started Loop")

    # Get submissions made by Redditor
    submitted = user.get_submitted(limit = 10)
    output_archive.write("------SUBMISSIONS-------\n\n\n")
    if debug == True:
        print("Got Submissions")

    # Archive user submitted posts
    for j in submitted:
        if debug == True:
            print("Started submission loop")

        if j.id not in already_archived:
            already_archived.write(j.id + "\n")
            # Get submission datetime
            timestamp = j.created_utc
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp)))
            # Write to archive (should I add comments?)
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
            output_archive.write("-----------------------------------\n\n\n")


    # Get user submitted comments made by Redditor
    comments = user.get_comments(limit = 5)
    output_archive.write("------COMMENTS-------\n\n\n")
    if debug == True:
        print("Got Comments")

    # Archive user submitted comments and the parent
    for i in comments:
        if debug == True:
            print("Started comment loop")
        if str(i.id) not in already_archived:
            already_archived.write(i.id + "\n")
            # Get submission datetime
            timestamp = i.created_utc
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp)))
            # Write to archive (should I add comments?)
            output_archive.write("Submission Date: \n" + dt + "\n\n")
            # Permalink to comment
            output_archive.write("Permalink: \n" + str(i.permalink) + "\n\n")
            output_archive.write("Subreddit: \n" + str(i.subreddit) + "\n\n")
            output_archive.write("Post Score: \n" + str(i.score) + "\n\n")
            # Get the parent ID
            parent = r.get_info(thing_id=i.parent_id)
            # Print the parent body if comment or selftext if submission
            if i.is_root == True:
                output_archive.write("Post Parent: \n" + str(parent.selftext) + "\n\n")
            elif i.is_root == False:
                output_archive.write("Comment parent: \n" + str(parent.body) + "\n\n")
            output_archive.write("Comment Body: \n" + str(i.body) + "\n\n")
            output_archive.write("-----------------------------------\n\n\n")

    # Set frequency of run
    if debug == True:
        print("Finished loops!")
    False
#    time.sleep(86400)

already_archived.close()
output_archive.close()
