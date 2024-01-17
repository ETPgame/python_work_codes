import requests as requests

url = "https://movie.douban.com/"
hd = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"}
cookie_new = {'Cookie': 'll="118174"; bid=9nzdDMr4vJI; __utmc=30149280; __utmc=223695111; _pk_id.100001.4cf6=b83183a8a1bfb32a.1686705894.; ap_v=0,6.0; __yadk_uid=4f9n8QxE6dSbfW2CamT3zaR63QWvTsq4; _vwo_uuid_v2=D7B1B3B6593A5CC0F8B5D47387ED00156|59251b0e0481bd224a6021e36dc89f98; push_noty_num=0; push_doumail_num=0; __utmv=30149280.27137; __gads=ID=32ccab7fc86db7ef-2244ee967ae100d1:T=1686707136:RT=1686707136:S=ALNI_MbTWgefxz3EWAzhVth--XghWbH6aw; __gpi=UID=00000c4eac5b1b11:T=1686707136:RT=1686707136:S=ALNI_MZ5wt7_0bLOnw67wD_O9IlXmVXi4Q; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1686709430%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.99834782.1686705890.1686705890.1686709442.2; __utmz=30149280.1686709442.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=30149280.2.10.1686709442; __utma=223695111.311217722.1686705894.1686705894.1686709443.2; __utmb=223695111.0.10.1686709443; __utmz=223695111.1686709443.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="271374399:6flan5hjH10"; ck=VNDy'}

r = requests.get(url, headers=hd, cookies=cookie_new)
session = requests.Session()
response = requests.Session().get(url, headers=hd, cookies=cookie_new)
if "ETP的帐号" in response.text:
    print("Cookie登录成功")
else:
    print("Cookie登录失败")
