import requests as requests

url = "https://www.jd.com/"
hd = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"}

r = requests.get(url, headers=hd)
print(r.text[70:200])
print()
print(r.request.headers)
