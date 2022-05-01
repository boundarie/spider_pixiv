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
def initialize():
    return headers,proxies