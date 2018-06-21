from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



animeId = 3453

url = "http://www.animenewsnetwork.com/encyclopedia/anime.php?id=%s" % str(animeId)


html = urlopen(url)
html = html.read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)
title =  soup.find("div", {"id": "page-title"}).find("h1", {"id": "page_header"}).contents[0]
ratingText =  soup.find("div", {"id": "ratingbox"})
ratingText = ratingText.find_all('span')
for i in ratingText:
    i = str(i)
    if 'vote' in i:
        i = i.split('<span>')[1][1::]
        print(i)
print(title)


# except urllib2.HTTPError as e:
#     logging.warning('HTTPError=%s, animeId=%s' % (str(e.code), str(animeId)))
# except urllib2.URLError as e:
#     logging.warning('URLError=%s, animeId=%s' % (str(e.reason), str(animeId)))
# except httplib.HTTPException as e:
#     logging.warning('HTTPException, animeId=%s' % str(animeId))
# except Exception:
#     import traceback
#     logging.warning('generic exception: ' + traceback.format_exc())
