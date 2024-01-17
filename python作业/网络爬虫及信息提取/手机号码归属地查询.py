import re

import requests

url = "https://www.ip138.com/mobile.asp?mobile="
suffix = "&action=mobile"
hd = {"User-Agent": "Mozilla/5.0"}

while True:
	mobile = input("请输入待查询的手机号码(输入Q退出):")
	try:
		if mobile != "Q" and mobile != "q":
			res = requests.get(url + mobile + suffix, headers=hd)
			html = res.content.decode("utf-8")
			print("该号码属于: " + re.findall('<td>卡号归属地</td>\n<td><span>(.*? .*?)</span></td>', html)[0])
		else:
			print("谢谢使用!")
			break
	except:
		print('电话号码有误!')
