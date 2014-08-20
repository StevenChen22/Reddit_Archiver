import praw
import datetime
import pprint
output_archive = open("archive.txt", "w")

user_agent = ("/u/CityofVancouver testing praw")
r = praw.Reddit(user_agent=user_agent)

user_name = "CityofVancouverWA"
user = r.get_redditor(user_name)
submission = user.get_submitted(limit = 1)
for i in submission:
    output_archive.write("Submission Date: \n" + str(i.created_utc) + "\n\n")
    output_archive.write("Permalink: \n" + str(i.permalink) + "\n\n")
    output_archive.write("Subreddit: \n" + str(i.subreddit) + "\n\n")
    output_archive.write("Post Score: \n" + str(i.score) + "\n\n")
    output_archive.write("Title: \n" + str(i.title) + "\n\n")
    # See if self post or not and write self text body or link
    if i.is_self == True:
        output_archive.write("Body: \n" + str(i.selftext) + "\n\n")
    elif i.is_self == False:
        output_archive.write("Link: \n" + str(i.url) + "\n\n")



    #print(i.selftext)
    #print("****THIS IS THE PERMALINK", i.permalink)
    #output_archive.write(i.selftext + "\n")
    #output_archive.write(i.permalink + "\n")
    #print("THIS IS THE URL", i.url)
    #timestamp = i.created_utc
    #dt = datetime.datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    #print(dt)

#submissions = r.get_subreddit('python').get_top(limit=1)
#submission = next(submissions)
#for i in submission.comments:
#    print(i.body)
#    print("****THIS IS THE PERMALINK", i.permalink)
#    output_archive.write(i.body)
#    output_archive.write(i.permalink)

output_archive.close()
