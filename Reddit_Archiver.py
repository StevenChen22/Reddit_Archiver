# Copyright 2014(c) Steven Chen
# Uses PRAW to archive Reddit posts and comments from a user
# Runs once per day

# Import Python Reddit API Wrapper (PRAW) and time
import time
import praw

debug = False

# Connect to Reddit and identify user and script
user_agent = ("/u/CityofVancouver testing praw")
r = praw.Reddit(user_agent=user_agent)

# Specify Redditor
user_name = "CityofVancouverWA"
user = r.get_redditor(user_name)
if debug == True:
    print("Logged in")

# Set number of comments and submissions to pull
submitted = user.get_submitted(limit = 1)
comments = user.get_comments(limit = 1)

def archive_check(n):
    found = False
    for i in archived_list:
        return i
        if str(n) in i:
            found = True
    return found

# While loop - beause it's a Bot and it needs to run 5ever!
counter = 0
while counter < 2:
    # Build already in archive list
    archived_list = []
    already_archived = open("already_archived.txt", "r")

    for line in already_archived:
        archived_list += [line.strip()]

    already_archived.close()

    output_archive = open("archive.txt", "a+")
    already_archived = open("already_archived.txt", "a+")

# Get submissions made by Redditor
    output_archive.write("------SUBMISSIONS-------\n")
    output_archive.write("Pulled: " + time.strftime('%Y-%m-%d %H:%M:%S') + "\n\n\n")

    if debug == True:
        print("Got Submissions")

    # Archive user submitted posts to file
    for j in submitted:
        if debug == True:
            print("Started submission loop")

        if archive_check(j.id) == False:
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
    output_archive.write("------COMMENTS-------\n")
    output_archive.write("Pulled: " + time.strftime('%Y-%m-%d %H:%M:%S') + "\n\n\n")
    if debug == True:
        print("Got Comments")

    # Archive user submitted comments and the parent to file
    for i in comments:
        if debug == True:
            print("Started comment loop")
        if archive_check(i.id) == False:
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

    output_archive.close()
    already_archived.close()

    if debug == True:
        print("Finished loops!")

    # Set frequency of run
    print("Sleeping for 24 hours...")
    time.sleep(86400)
