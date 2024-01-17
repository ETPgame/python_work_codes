import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 图中文字体设置为黑体
plt.rcParams['axes.unicode_minus'] = False  # 负值显示

data = pd.read_csv(r'D:\我的\大学\大二下\数据可视化\大作业\subway.csv', encoding='gbk', header=None,
				   names=['city', 'line', 'stat_name'])

# 首先汇总每个城市的地铁线路
# 一线城市
list1 = ['北京', '上海', '广州', '深圳']
# 新一线城市
list2 = ['成都', '杭州', '重庆', '武汉', '西安', '苏州', '天津',
		 '南京', '长沙', '郑州', '东莞', '青岛', '沈阳', '合肥', '佛山']
# 二线城市
list3 = ['无锡', '宁波', '昆明', '大连', '福州', '厦门',
		 '哈尔滨', '济南', '温州', '南宁', '长春', '泉州', '石家庄',
		 '贵阳', '南昌', '金华', '常州', '南通', '嘉兴', '太原', '徐州',
		 '惠州', '珠海', '中山', '台州', '烟台', '兰州', '绍兴', '海口', '扬州']
# 三线城市
list4 = ['汕头', '湖州', '盐城', '潍坊', '保定', '镇江', '洛阳', '泰州',
		 '乌鲁木齐', '临沂', '唐山', '漳州', '赣州', '廊坊', '呼和浩特', '桂林',
		 '银川', '揭阳', '三亚', '遵义', '江门', '芜湖', '济宁', '莆田', '湛江',
		 '绵阳', '淮安', '连云港', '淄博', '宜昌', '邯郸', '上饶', '柳州', '舟山',
		 '咸阳', '九江', '衡阳', '威海', '宁德', '阜阳', '株洲', '丽水', '南阳',
		 '襄阳', '大庆', '沧州', '信阳', '岳阳', '商丘', '肇庆', '清远', '滁州',
		 '龙岩', '荆州', '蚌埠', '新乡', '鞍山', '湘潭', '马鞍山', '三明', '潮州',
		 '梅州', '秦皇岛', '南平', '吉林', '安庆', '泰安', '宿迁', '包头', '郴州', '南充']

list5 = []
for i in data.city:
	if i in list1:
		list5.append('一线')
	elif i in list2:
		list5.append('新一线')
	elif i in list3:
		list5.append('二线')
	elif i in list4:
		list5.append('三线')
	else:
		list5.append('其他')
data = pd.concat([data, pd.DataFrame(list5)], axis=1)
data = data.rename(columns={0: 'level'})
data.to_csv(r'D:\我的\大学\大二下\数据可视化\大作业\subway_city.csv', encoding='gbk')

fig = plt.figure()
fig.set(alpha=0.2)
f, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
plt.subplot(2, 2, 1)
data.loc[data['level'] == '一线'].groupby('city').line.nunique().plot(kind='bar', color='lightblue')
plt.title('一线城市')
plt.subplot(2, 2, 2)
data.loc[data['level'] == '新一线'].groupby('city').line.nunique().plot(kind='bar', color='lightblue')
plt.title('新一线城市')
plt.subplot(2, 2, 3)
data.loc[data['level'] == '二线'].groupby('city').line.nunique().plot(kind='bar', color='lightblue')
plt.title('二线城市')
plt.subplot(2, 2, 4)
data.loc[data['level'] == '三线'].groupby('city').line.nunique().plot(kind='bar', color='lightblue')
plt.title('三线城市')
plt.show()

# 下面分析城市线路平均站数
data2 = pd.DataFrame(data.groupby('city').line.value_counts())
data2.columns = ['count_stat']
data2 = data2.reset_index()
data2.to_csv(r'D:\我的\大学\大二下\数据可视化\大作业\subway_avg_stat.csv', encoding='gbk')

list6 = []
for i in data2.city:
	if i in list1:
		list6.append('一线')
	elif i in list2:
		list6.append('新一线')
	elif i in list3:
		list6.append('二线')
	elif i in list4:
		list6.append('三线')
	else:
		list6.append('其他')

data2 = pd.concat([data2, pd.DataFrame(list6)], axis=1)
data2 = data2.rename(columns={0: 'level'})

fig = plt.figure()
fig.set(alpha=0.2)
f, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
plt.subplot(2, 2, 1)
data2.loc[data2['level'] == '一线'].groupby('city').count_stat.mean().plot(kind='bar', color='lightblue')
plt.title('一线城市')
plt.subplot(2, 2, 2)
data2.loc[data2['level'] == '新一线'].groupby('city').count_stat.mean().plot(kind='bar', color='lightblue')
plt.title('新一线城市')
plt.subplot(2, 2, 3)
data2.loc[data2['level'] == '二线'].groupby('city').count_stat.mean().plot(kind='bar', color='lightblue')
plt.title('二线城市')
plt.subplot(2, 2, 4)
data2.loc[data2['level'] == '三线'].groupby('city').count_stat.mean().plot(kind='bar', color='lightblue')
plt.title('三线城市')
plt.show()

# 进一步分析城市站名特点
data4 = pd.DataFrame(data.groupby('stat_name').line.count().sort_values(ascending=False))
data4 = data4.reset_index()
data4.to_csv(r'D:\我的\大学\大二下\数据可视化\大作业\subway_stat_name.csv', encoding='gbk')
a = data4[data4['line'] > 4]
plt.plot(a['stat_name'], a['line'])
plt.xticks(rotation=45)
plt.show()
