import pytumblr
import requests
from keys import *

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

def run():
    feed = client.posts('good-smile-company', limit=1)

    #print(feed['posts'])
    announce = []

    for post in feed['posts']:
        #Get tag
        tag = post['tags']
        if ('nendoroid' in tag): #treatment
            #Get name of the Fig
            name = ' '.join(tag).split('nendoroid ')[1]
            #Get link
            link = post['caption'].split('<a href=\"')[1].split('\">')[0]
            #Get first picture
            for photos in post['photos']:
                original = photos['original_size']
                url = original['url']
                break

            #Now we send it to image
            announce.append([url,name,link])
    return announce
