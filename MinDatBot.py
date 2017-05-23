# MinDatBot.py
# Author: The-Unraveling


# WILL RUN FOREVER, REMEMBER TO CTRL-C TO EXIT IF NEED TO KILL
import praw
import re
import os
import codecs
import wikipedia


import pdb

reddit = praw.Reddit('MinDatBot')

with codecs.open("mineral_names_on_wiki.txt", "r") as f:
    mineral_names_on_wiki = f.read()
    mineral_names_on_wiki = mineral_names_on_wiki.split("\n")
    mineral_names_on_wiki = tuple(filter(None, mineral_names_on_wiki))

subreddit = reddit.subreddit('pythonforengineers')

# Have we run this code before? If not, create empty list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we've run code before, load list of posts we have replied to
else:
    # read file into a list and remove any empsy values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

for comment in subreddit.stream.comments():

    if comment.id not in comments_replied_to:

    #print(submission title)

        i = 0

        for i in range(0, len(mineral_names_on_wiki)):

            possible_mineral_match = re.search(mineral_names_on_wiki[i], comment.body, re.IGNORECASE)



            if possible_mineral_match:
                #print possible_mineral_name
                break
            #print possible_mineral_name

        if possible_mineral_match:
            possible_mineral_name = re.findall(mineral_names_on_wiki[i], comment.body, re.IGNORECASE)

            for i in range(i+1,len(mineral_names_on_wiki)):
                possible_mineral_name_next = re.findall(mineral_names_on_wiki[i], comment.body, re.IGNORECASE)
                if all(possible_mineral_name_next):
                    possible_mineral_name.extend(possible_mineral_name_next)

            print possible_mineral_name
            name = possible_mineral_name[0]

            # SET UP 

            print name
            #print possible_mineral_name
            author = comment.author
            print(author.name)

            if not re.match('throwAwayBotToday',author.name):

                print"Bot replying to : ", comment.id
                print "\n", comment.body

                wikidata = wikipedia.page(name)

                wiki_images = wikidata.images

                # CANT USE WIKI IMAGES, TOO MUCH RANDOMNESS...
                # GRAB GOOGLE SEARCH IMAGES??
                # First 2-5 images? should be able to pick up
                # By searching '"NAME" mineral"

                #imageamt = len(wiki_images)
                imageamt = len(wikidata.images)
                print imageamt
                if imageamt <= 3:
                    mineral_reply = "Looking for " + name + "? Here's some information " \
                                                            "about that mineral! " + "[" + name + \
                                    " on Wikipedia](" + wikidata.url + ") "

                else:
                    mineral_reply = "Looking for " + name + "? Here's some information " \
                                                    "about that mineral! " + "[" + name + \
                                                    " on Wikipedia](" + wikidata.url + ") " + \
                                                    wikidata.images[imageamt - 3] + " " + \
                                                    wikidata.images[imageamt - 1]

                print(mineral_reply)
                print(comment.id)

                #comment.reply(mindat_reply)
                #with open("comments_replied_to.txt","a") as myfile:
                    #myfile.write(comment.id + "\n")
                #comments_replied_to.append(comment.id)

                print comments_replied_to


print(comments_replied_to)
