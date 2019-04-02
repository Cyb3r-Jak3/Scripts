import praw, os, re


if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []

else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))
if not os.path.isfile("comments_replied_to.txt"):
	comments_replied_to = []
else:
	with open("comments_replied_to.txt", "r") as f:
		comments_replied_to = f.read()
		comments_replied_to = comments_replied_to.split("\n")
		comments_replied_to = list(filter(None, comments_replied_to))

reddit = praw.Reddit('bot1')
subreddit =  reddit.subreddit("usefulbottest")

for submission in subreddit.hot(limit=5):
	if submission.id not in posts_replied_to:
		if  re.search("skills", submission.title, re.IGNORECASE):
			submission.reply("Usebot says that it worked")
			print("Bot replying to : ", submission.title)
			posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")

comments = subreddit.stream.comments()

for comment in comments:
	text = comment.body
	author = comment.author
	if 'kidding' in text.lower() and comment.id not in comments_replied_to:
		comment.reply ("There is no kidding here %s" % author)
		print("Bot replying to :", text)
		comments_replied_to.append(comment.id)
		#break

with open("comments_replied_to.txt", "w") as f:
	for comment_id in comments_replied_to:
		f.write(comment_id + "\n")
