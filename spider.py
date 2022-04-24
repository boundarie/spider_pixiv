import requests
import json
import re

#Remember to Modify Your Header
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
# url = 'https://www.pixiv.net/'

def getAuthorAllPicId(id):
    url = 'https://www.pixiv.net/ajax/user/' + str(id) + '/profile/all'
    response = requests.get(url, headers=headers)
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
    for i in range(0,len(ids)):
        res = requests.get('https://www.pixiv.net/artworks/{}'.format(ids[i]),headers = headers)
        locs.append(find(res.text))
    return locs

def downPic(id):
    ids  = getAuthorAllPicId(id)
    locs = getPicLoc(id)
    for i in range(0,len(ids)):
        headers['Referer'] = 'https://www.pixiv.net/artworks/{}'.format(ids[i])
        img = requests.get(locs[i],headers = headers)
        if img.status_code == 200:
            path = str(i)+".png"
            with open(path, 'wb') as fp:
                try:
                    fp.write(img.content)
                except Exception as e:
                    print(e)
                fp.close()


#e.g. downPic(30837811)
