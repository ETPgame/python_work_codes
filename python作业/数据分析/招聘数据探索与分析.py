import re

import pandas as pd

# 1)    将数据存为一个名叫 job_info 的数据框。
job_info = pd.read_csv(r"D:\\我的\\大学\\大二下\\python课\\实验08-数据分析\\data\\job_info.csv",
					   encoding="GBK")
# print(job_info.head())

# 2)    将列命名为： ['公司', '岗位', '工作地点', '工资', '发布日期']。
job_info.columns = ['公司', '岗位', '工作地点', '工资', '发布日期']

# 3)    哪个岗位招聘需求最多？
need = job_info["岗位"].value_counts().idxmax()
print(f"{need}的岗位招聘需求最多")

# 4)    取出 9 月 3 日发布的招聘信息。
recruit = job_info[job_info["发布日期"] == "09-03"]
print(recruit)

# 5)    找出工作地点在深圳的数据分析师招聘信息。
info = job_info[job_info["岗位"] == "数据分析师"]
info = info[info["工作地点"].apply(lambda x: "深圳" in x)]
print(info)

# 6)    取出每个岗位的最低工资与最高工资，单位为“ 元/月” ，若招聘信息中无工资数据则无需处理（如原始数据为 2-2.5 万/月，则最低工资为 20000，最高工资为 25000）。
job_info['工资'].str[-3].value_counts()


def get_number(string=None):
	try:
		if string[-3] == '万':
			x = [float(i) * 10000 for i in re.findall('\d+\.{0,1}\d*', string)]
		elif string[-3] == '千':
			x = [float(i) * 1000 for i in re.findall('\d+\.{0,1}\d*', string)]
		if string[-1] == '年':
			x = [i / 12 for i in x]
		return x
	except:
		return None


job_info['最低月薪'] = job_info['工资'].apply(get_number).str[0]
job_info['最高月薪'] = job_info['工资'].apply(get_number).str[1]
low = job_info.groupby("岗位")["最低月薪"].min()
high = job_info.groupby("岗位")["最高月薪"].max()
for i in low.index:
	print(f"{i}的最低月薪为{low[i]}")
print()
for i in high.index:
	print(f"{i}的最高月薪为{high[i]:.2f}")
