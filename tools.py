import requests
import json
import re
from tqdm import *
import info

headers,proxies = info.initialize()
#This Part for specific Author
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
def findArt(text,start):
    for i in range(start,len(text)):
        if (text[i:i+8]=='artworks'):
            return text[i+9:i+17],i+17

def getPicLoc(ids):
    locs = []
    for i in tqdm(range(len(ids)),desc='load_loc'):
        res = requests.get('https://www.pixiv.net/artworks/{}'.format(ids[i]),headers = headers, proxies = proxies)
        locs.append(find(res.text))
        
    return locs
######################HERE IS THE PATH


def down(ids,locs):
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


#######################
def downAuthor_All(id):
    ids  = getAuthorAllPicId(id)
    locs = getPicLoc(ids)
    down(ids,locs)

#mode = daily, weekly, monthly, rookie, original, male, female
def getRankingsPicId(date,mode,content):
    if (content=='插画'):
        content = '&content=illust'
    else:
        content = ''
    url = "https://www.pixiv.net/ranking.php?mode="+str(mode)+content+"&date="+str(date)
    res = requests.get(url,headers = headers,proxies = proxies)
    count = 0
    next = 0
    ids = []
    while True:
        id,next = findArt(res.text,next)
        if id not in ids:
            ids.append(id)
            count+=1
        if (count == 30):#YOU CAN ALSO MODIFY THE COUNT
            break
    return ids

def downRankings_top30(date,mode,content):
    ids = getRankingsPicId(date,mode,content)
    locs = getPicLoc(ids)
    down(ids,locs)
#downRankings_top30(20220430,'daily','插画')
#print(getRankingsPicId(20220430,'daily','ss'))