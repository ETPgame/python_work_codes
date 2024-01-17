# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}


def getMessage():
	file = open("WenZhou_Weather_try1.csv", "w", newline="")
	header = ['日期', '星期', '最高气温', '最低气温', '天气', '风向', '风力']

	# 使用 join 将列表转为字符串，每个元素之间用逗号分隔
	header_str = ','.join(header)
	file.write(header_str + '\n')

	for i in range(1, 13):
		if i < 10:
			month = '0' + str(i)
		else:
			month = str(i)
		url = f'http://lishi.tianqi.com/wenzhou/2022{month}.html'
		print(f"Fetching data for {url}")
		response = requests.get(url=url, headers=headers)
		text = response.text
		soup = BeautifulSoup(text, 'lxml')

		li_list = soup.select(
			'ul[class ="thrui" ] > li')  # 从网页源代码中选择所有父级是 <ul> 且包含[class ="thrui"]的元素的 <li> 元素并取出放在li_list中

		for j in range(len(li_list)):
			a = li_list[j].text  # 将li属性中的文本放入a中
			# print(a)
			info_list = a.split()  # 将a中的每个文本分割，放入info_list
			info_list[2] = str(int(info_list[2].replace('℃', '')))  # 将最高温与最低温的℃删除，将这两列用int类保存在csv中
			info_list[3] = str(int(info_list[3].replace('℃', '')))
			info_list_str = ",".join(info_list)
			file.write(info_list_str+'\n')
	file.close()


if __name__ == "__main__":
	getMessage()
