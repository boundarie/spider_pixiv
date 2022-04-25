import requests
import json
import re
from tqdm import *
#Remember to Modify Your Header
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
# url = 'https://www.pixiv.net/'
#Remember to Modify Your proxies according to your vpn
proxies = {
    'https': 'http://127.0.0.1:7890',
    'http': 'http://127.0.0.1:7890'
}
def getAuthorAllPicId(id):
    url = 'https://www.pixiv.net/ajax/user/' + str(id) + '/profile/all'
    response = requests.get(url, headers=headers, proxies=proxies)
    print("link success")
    if response.status_code == 200:
        resdict = json.loads(response.content)['body']['illusts']
        return [key for key in resdict]

def find(text):
    search = re.search('"original":',text)
    for i in range(search.start(),search.start()+600):
        if ((text[i]=='"') and (text[i+1]=='}')):
            return text[search.end()+1:i]

def getPicLoc(id):
    ids = getAuthorAllPicId(id)
    locs = []
    for i in tqdm(range(len(ids)),desc='load_loc'):
        res = requests.get('https://www.pixiv.net/artworks/{}'.format(ids[i]),headers = headers, proxies = proxies)
        locs.append(find(res.text))
        
    return locs

def downPic(id):
    ids  = getAuthorAllPicId(id)
    locs = getPicLoc(id)
    for i in tqdm(range(len(ids)),desc='load_img'):
        headers['Referer'] = 'https://www.pixiv.net/artworks/{}'.format(ids[i])
        img = requests.get(locs[i],headers = headers, proxies = proxies)
        if img.status_code == 200:
            path = "./pics/"+str(i+68)+".png"#the path you save your pictures
            with open(path, 'wb') as fp:
                try:
                    fp.write(img.content)
                except Exception as e:
                    print(e)
                fp.close()

#downPic(24218478)