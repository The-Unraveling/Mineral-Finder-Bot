import os
import praw

reddit = praw.Reddit('MineralFinderBot')  # SET UP NEW CLIENT AND ALL THAT, ALL IN PRAW.INI

if not os.path.isfile("comments_bot_made.txt"):
    print "comments_bot_made.txt not found, making file..."
    comments_bot_made = []

else:
    # read file into a list and remove any empsy values
    with open("comments_bot_made.txt", "r") as f:
        print "comments_bot_made.txt found, reading file:"
        comments_bot_made = f.read()
        comments_bot_made = comments_bot_made.split("\n")
        comments_bot_made = list(filter(None, comments_bot_made))


i = 0

print "Starting hate check..."
while i < (len(comments_bot_made) - 1):
    bot_hate_check = reddit.comment(comments_bot_made[i])
    print bot_hate_check.score
    if bot_hate_check.score < -1:
        bot_hate_check.delete()
    i += 1

print "Hate check done!"