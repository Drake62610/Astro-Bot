import feedparser
import time
from subprocess import check_output
import sys
import logging

feed_name = 'Nya'
url = 'https://nyaa.si/?page=rss'

db = 'nyaa/feeds.db'
limit = 12 * 3600 * 1000
logger = logging.getLogger('AstroLog')

search = [['Tsubasa','VOSTFR']]

current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

def isindb(post):
    with open(db, 'r') as data:
        logger.debug('nyaa db opened')
        for line in data:
            if post.title in line:
                data.close
                return True
    data.close
    logger.debug('nyaa db closed')
    return False

def updatedb(list):
    with open(db,'a') as data:
        logger.debug('nyaa db opened')
        for post in list:
            link = post.description.split('<a href=\"')[1].split('\">')[0]
            tmp = post.title + "|" + str(current_timestamp) + "|" + link
            data.write(tmp + "\n")
            logger.debug(tmp + ' added to nyaa db')
        logger.debug('nyaa db closed')
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
