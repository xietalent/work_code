from urllib.parse import quote

base_url = 'https://s.taobao.com/search?q='
keyword = "ipad"
url = base_url + quote(keyword)

print(url)

