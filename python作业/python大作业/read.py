import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./WenZhou_Weather_try.csv', encoding='gbk')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 温州2023年历史气温
temp_high = df['最高气温']
temp_low = df['最低气温']

x = pd.date_range('20220101', periods=365)
plt.plot(x, temp_high, 'r-', label='最高气温')
plt.plot(x, temp_low, 'b-', label='最低气温')
plt.legend()
plt.xlabel('日期')
plt.ylabel('气温（单位：℃）')
plt.title('温州2022年历史气温')
plt.show()

# 最大温差
temp_dev = temp_high - temp_low
x = pd.date_range('20220101', periods=365)
plt.plot(x, temp_dev, label='每日温差')
plt.legend()
plt.xlabel('日期')
plt.ylabel('温差（单位：℃）')
plt.title('温州2022年每日温差')
plt.show()

# 天气统计
weather = dict()
for i in df['天气']:
	if i in weather.keys():
		weather[i] = weather[i] + 1
	else:
		weather[i] = 1
wea_sort = sorted(weather.items(), key=lambda x: x[1], reverse=True)
x = []
y = []
for i in wea_sort:
	x.append(i[0])
	y.append(i[1])
for i in range(len(y)):
	y[i] = y[i] / 365
plt.pie(y, labels=x, autopct='%1.1f%%', shadow=False, startangle=150, explode=[0, 0, 0, 0, 0, 0.1, 0.1, 0.3, 0.5])
# plt.bar(x, y)
# plt.xlabel('天气')
# plt.ylabel('出现时间长度')
# plt.title('温州2022年天气统计')
# for a, b in zip(x, y):
# 	plt.text(a, b, '%.f'%b, ha='center', va='bottom', fontsize=10)
plt.show()

# 风向统计
wind = dict()
for i in df['风向']:
	if i in wind.keys():
		wind[i] = wind[i] + 1
	else:
		wind[i] = 1
wind_sort = sorted(wind.items(), key=lambda x: x[1], reverse=True)
x = []
y = []
for i in wind_sort:
	x.append(i[0])
	y.append(i[1])
plt.bar(x, y)
plt.xlabel('风向')
plt.ylabel('出现时间长度')
plt.title('温州2022年风向统计')
for a, b in zip(x, y):
	plt.text(a, b, '%d' % b, ha='center', va='bottom', fontsize=10)
plt.show()
