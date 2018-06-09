import feedparser
import time
from subprocess import check_output
import sys

feed_name = 'Nya'
url = 'https://nyaa.si/?page=rss'

db = 'feeds.db'
limit = 12 * 3600 * 1000

search = [['Tsubasa','VOSTFR']]

current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

def isindb(post):
    with open(db, 'r') as data:
        for line in data:
            if post.title in line:
                data.close
                return True
    data.close
    return False

def updatedb(list):
    with open(db,'a') as data:
        for post in list:
            link = post.description.split('<a href=\"')[1].split('\">')[0]
            data.write(post.title + "|" + str(current_timestamp) + "|" + link + "\n")
        data.close

def run():
    #
    # get the feed data from the url
    #
    feed = feedparser.parse(url)

    add = []
    for post in feed.entries:
        if not isindb(post):
            add.append(post)

    updatedb(add)
    for i in add:
        print(i.title)

    bool = True
    announce = []
    for post in add:
        for sherlock in search:
            for props in sherlock:
                if not props in post.title:
                    bool=False
                    break
            if bool == True:
                announce.append(post)
            else:
                bool=True
    return announce
