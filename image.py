import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
import os
def StartSearch():
    search = input("search for:")
    params = {"q": search}
    dir_name =search.replace(" ", "_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    r = requests.get("https://www.bing.com/images/search" , params =params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    for item in links:
        try:

            img_obj = requests.get(item.attrs["href"])
            print("getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-2]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("can not save image")
        except:
            print("can not complete the request")

    StartSearch()
StartSearch()