import os
import praw
import sys

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

if not os.path.isfile("hated_comment_text.txt"):
    print "hated_comment_text.txt not found, making file..."
    hated_comment_text = []

if not os.path.isfile("hated_comment_parents.txt"):
    print "hated_comment_parents.txt not found, making file..."
    hated_comment_parents = []
else:
    # read file into a list and remove any empsy values
    with open("hated_comment_parents.txt", "r") as f:
        print "hated_comment_parents.txt found, reading file:"
        hated_comment_parents = f.read()
        hated_comment_parents = hated_comment_parents.split("\n")
        hated_comment_parents = list(filter(None, hated_comment_parents))

i = 0

print "Starting hate check..."
while i < (len(comments_bot_made) - 1):
    bot_hate_check = reddit.comment(comments_bot_made[i])
    print bot_hate_check.id, "Score: ", bot_hate_check.score
    if bot_hate_check.score < -1:
        parent = bot_hate_check.parent()
        if parent.id not in hated_comment_parents:
            with open("hated_comment_text.txt", "a") as h:


                h.write(parent.body)
                h.write(bot_hate_check.body)
                h.write("\n")

            with open("hated_comment_parents.txt", "a") as h:
                h.write(parent.id)
                h.write("\n")

            hated_comment_parents.append(parent.id)
        bot_hate_check.delete()
    i += 1

print "Hate check done!"

sys.exit()