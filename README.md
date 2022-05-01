# spider_pixiv

## Guide:

### step 1: git clone

### step 2: Dwonload the dependencies

### step 3: Modify the headers and proxies in info.py(If you don't know how, contact me)

### step 4: Check the path of the pictures to be downloaded in tools.py

### step 5: Call functions from Module tools in run.py

## version 1.0 2022.5.1

The file has been separated into three files.

info.py: Set your User-Agent and proxies

tools.py: All the functions we need

run.py: To be executed

downPic has been renamed as downAuthor_All(id).

NEW FUNCTION: downRankings_top30(date,mode,content).

## version 0.2 2022.4.25

Include tqdm, proxies

## version 0.1 2022.4.24

downPic(id): download all the works of the given artist.

Remark: id should be numbers

e.g. https://www.pixiv.net/users/30837811/artworks?p=1, The number between /users/ and /artworks is the artist's id.
