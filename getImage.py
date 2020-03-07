import requests
import urllib.request
from xml.etree import ElementTree

def getImg(search_text):
    # api end point
    URL = "https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&text={}&format=json&nojsoncallback=1"
    # api key
    api_key = 'fa89d0dd0ced86e202442478cfa67854'
    # string to be searched
    #search_text = 'banana'

    URL = URL.format(api_key, search_text)

    # get from flickr api
    r = requests.get(url = URL).json()

    # use the first photo in search result
    imgs = []
    for i in range(0, 4):
        img = r['photos']['photo'][i]
        res_img = "https://farm{}.staticflickr.com/{}/{}_{}.jpg"
        res_img = res_img.format(img['farm'], img['server'], img['id'], img['secret'])
        urllib.request.urlretrieve(res_img, "./static/input" + str(i) + ".jpg")
    
    """
    for img in imgs, i in range(0, 4):
        res_img = "https://farm{}.staticflickr.com/{}/{}_{}.jpg"
        res_img = res_img.format(img['farm'], img['server'], img['id'], img['secret'])
        urllib.request.urlretrieve(res_img, "./static/input" + i + ".jpg")
    """
    #print(img['farm'])
    #print(root.tag)
    #data = r.json()
    #print(r['farm']['photo'][0])
    print(res_img)
    
    #return res_img