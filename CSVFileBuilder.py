# MinDatBot.py
# Author: The-Unraveling

import praw
import re
import os
import codecs
import wikipedia
import datetime
import time
import sys
import csv

import mwparserfromhell
import pywikibot


def main():

    print "Bot Starting..."

    reddit = praw.Reddit('MineralFinderBot') # SET UP NEW CLIENT AND ALL THAT, ALL IN PRAW.INI
    enwp = pywikibot.Site('en', 'wikipedia')

    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.datetime.now()

    print "Opening/Reading mineral name file..."
    with codecs.open("mineral_names_on_wiki.txt", "r") as f:
        mineral_names_on_wiki = f.read()
        mineral_names_on_wiki = mineral_names_on_wiki.split("\n")
        mineral_names_on_wiki = tuple(filter(None, mineral_names_on_wiki))

    print "Done!"

    #if not os.path.isfile("mineral_database_test.csv"):
        #print "mineral_database_test.csv not found, making file..."


    #else:
        # read file into a list and remove any empsy values
    with open("mineral_database_test.csv", "wb") as database:
        print "mineral_database_test.csv found, reading file:"
        wr = csv.writer(database, dialect='excel')

        i = 0
        #while i < len(mineral_names_on_wiki):
        print mineral_names_on_wiki
        for location in sorted(mineral_names_on_wiki):
            wr.writerow([location])
        #i += 1

main()