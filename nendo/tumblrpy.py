import pytumblr
import requests
import logging
from keys import *

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

db = 'nendo/nendo.db'
logger = logging.getLogger('AstroLog')

def run():
    feed = client.posts('good-smile-company', limit=10)
    #print(feed['posts'])
    announce = []

    for post in feed['posts']:
        #Get tag
        tag = post['tags']

        if ('nendoroid' in tag): #treatment
            #Get name of the Fig
            tab = ' '.join(tag)
            name = tab.split('nendoroid ',1)[1]
            if not isindb(name):
                #Get link
                link = post['caption'].split('<a href=\"')[1].split('\">')[0]
                #Get first picture
                for photos in post['photos']:
                    original = photos['original_size']
                    url = original['url']
                    break
                #Now we send it to image
                announce.append([url,name,link])
                logger.debug(announce)
    updatedb(announce)
    return announce


def isindb(name):
    with open(db, 'r') as data:
        for line in data:
            if name in line:
                data.close
                return True
    data.close
    return False

def updatedb(list):
    with open(db,'a') as data:
        for post in list:
            data.write(post[1] + '\n')
        data.close
