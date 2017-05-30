import wikipedia
import os
import re
import codecs

minerals = wikipedia.page("List of rock types")

print minerals.title

print minerals.url

print len(minerals.links)

# Have we run this code before? If not, create empty list
if not os.path.isfile("mineral_names_on_wiki.txt"):
    mineral_names_on_wiki = []

# If we've run code before, load list of posts we have replied to
else:
    # read file into a list and remove any empsy values
    with codecs.open("mineral_names_on_wiki.txt", "r") as f:
        mineral_names_on_wiki = f.read()
        mineral_names_on_wiki = mineral_names_on_wiki.split("\n")
        mineral_names_on_wiki = list(filter(None, mineral_names_on_wiki))

i = 0
for i in range(0,len(minerals.links)):
    current_mineral = wikipedia.page(minerals.links[i], "lxml")

    title = current_mineral.title

    print current_mineral.title, current_mineral.url

    if title.encode('utf-8') not in mineral_names_on_wiki: #UNICODE WARNING... BUUT THIS FUNCTIONS SO...
            #title.encode('utf-8')

        with open("mineral_names_on_wiki.txt", "a") as myfile:
            myfile.write(title.encode('utf-8') + "\n")

        mineral_names_on_wiki.append(current_mineral.title)

    print i # WHY DOES ADDING THIS MAKE CODE WORK?
            # IS IT DISRUPTING WHAT'S GETTING SENT TO MINERAL LINK?

# NOTE: Manual cleanup of list neccesary after code is run(some grabbed links are for unwanted things)
# Hard to get code to tell 'good' links from 'bad' as both lead to wiki pages