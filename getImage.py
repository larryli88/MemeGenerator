import requests
import urllib.request
from xml.etree import ElementTree

def getImg(search_text):
    # api end point
    URL = "https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&text={}&format=json&nojsoncallback=1"
    # api key
    api_key = 'fa89d0dd0ced86e202442478cfa67854'
    # format the url with api end point and api key and search text
    URL = URL.format(api_key, search_text)

    # GET from flickr api
    r = requests.get(url = URL).json()

    # save the first 4 results
    for i in range(0, 4):
        img = r['photos']['photo'][i]
        res_img = "https://farm{}.staticflickr.com/{}/{}_{}.jpg"
        res_img = res_img.format(img['farm'], img['server'], img['id'], img['secret'])
        urllib.request.urlretrieve(res_img, "./static/input" + str(i) + ".jpg")