import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}

with open('WenZhou_Weather.csv', 'w', newline='') as file:
    w = csv.writer(file)
    w.writerow(['日期', '星期', '最高气温', '最低气温', '天气', '风向', '风力'])
    for i in range(1, 13):
        if i < 10:
            month = '0'+str(i)
        else:
            month = str(i)
        url = f'http://lishi.tianqi.com/wenzhou/2022{month}.html'
        response = requests.get(url=url, headers=headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')      # 用lxml的方式解释text的内容
        li_list = soup.select('ul[class ="thrui" ] > li')    # 从网页源代码中选择所有父级是 <ul> 且包含[class ="thrui"]的元素的 <li> 元素并取出放在li_list中

        ''' 
         <li class="hide">
        <div class="th200">2022-01-30 星期日 </div>
        <div class="th140">8℃</div>
        <div class="th140">1℃</div>
        <div class="th140">晴</div>
        <div class="th140">北风 2级</div>
        <!-- <div class="th150"></div> -->
        </li>
        '''

        for j in range(len(li_list)):
            a = li_list[j].text     # 将li属性中的文本放入a中
            # print(a)
            info_list = a.split()   # 将a中的每个文本分割，放入info_list
            # info_list[2] = int(info_list[2].replace('℃', ''))   # 将最高温与最低温的℃删除，将这两列用int类保存在csv中
            # info_list[3] = int(info_list[3].replace('℃', ''))
            print(info_list)
            w.writerow(info_list)
        print('2022' + month + '的数据写入成功！')
    print("写入文件成功！")