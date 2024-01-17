import requests
from bs4 import BeautifulSoup
import chardet
import pandas as pd
import re

url = "http://www.gz.chinanews.com.cn/jjgz/index.shtml"

# 创建一个空的 DataFrame 用于存储数据
data = {}
df = pd.DataFrame(data)

# 发送请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    encoding = chardet.detect(response.content)['encoding']
    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)

    # 找到class="listClass"下的所有class="h4"的元素
    h4_elements = soup.select('.listClass .h4')

    # 提取链接和文本内容
    for h4_element in h4_elements:
        link = h4_element.find('a')['href']
        text_content = h4_element.get_text(strip=True)  # 获取元素的文本内容，strip=True去除多余空白
        print(f"链接: {link}")
        print(f"文本内容: {text_content}")

        # 访问链接并获取页面文本内容
        link_response = requests.get(link)
        if link_response.status_code == 200:
            link_soup = BeautifulSoup(link_response.content, 'html.parser',
                                      from_encoding=chardet.detect(link_response.content)['encoding'])

            # 获取class="title"下class="h4c"的文本内容
            title_h4c_text = link_soup.select_one('.title .h4c').get_text(strip=True, separator=' ')
            print(f"title_h4c文本内容: {title_h4c_text}")

            # 获取class="nav meta"下所有class="pubtime"的文本内容
            all_pubtime_elements = link_soup.select('.nav.meta .pubtime')
            all_pubtime_text = [pubtime.get_text(strip=True) for pubtime in all_pubtime_elements]
            print(f"所有pubtime文本内容: {all_pubtime_text}")

            # 获取class="share visible-md-block visible-lg-block"下所有的<p>标签的文本内容
            all_p_elements = link_soup.select('.article p')
            all_p_text = [p.get_text(strip=True) for p in all_p_elements]
            print(f"所有p标签文本内容: {all_p_text}".encode('utf-8'))

            # 获取class="bianji"的文本内容
            bianji_text = link_soup.select_one('.bianji').get_text(strip=True, separator=' ')

            # 使用正则表达式提取":"和"】"之间的文本
            extracted_text = re.search(r'：(.*?)】', bianji_text)
            if extracted_text:
                extracted_text = extracted_text.group(1).strip()

            print(f"bianji文本内容: {bianji_text}")
            print(f"提取的文本内容: {extracted_text}")

            print("-" * 50)
            # 将数据添加到 DataFrame 中
            df = df._append({'url': link, 'title': title_h4c_text,
                            'pubtime': all_pubtime_text[0],'source':all_pubtime_text[1], 'content': all_p_text, 'edit': extracted_text},
                           ignore_index=True)

            # # 将 DataFrame 存储为 CSV 文件
            # df.to_csv('output.csv', index=False, encoding='utf-8-sig')
            # break;
        else:
            print(f"访问链接失败，状态码: {link_response.status_code}")

else:
    print("请求失败，状态码：" + str(response.status_code))

# 将 DataFrame 存储为 CSV 文件
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
