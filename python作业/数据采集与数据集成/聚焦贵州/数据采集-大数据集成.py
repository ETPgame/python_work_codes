import requests

url = "https://www.gz.chinanews.com.cn/jjgz/index.shtml"
hd = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"}

r = requests.get(url, headers=hd)

print(r.headers)

# http://www.gz.chinanews.com/jjgz/2023-11-21/doc-ihcvewkm2168789.shtml
# http://www.gz.chinanews.com/jjgz/2023-11-19/doc-ihcuyruu2837883.shtml