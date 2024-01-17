import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
data = pd.read_excel("D:\\我的\\大学\\大二下\\python课\\实验07-数据处理与可视化\\score.xlsx")

# 设置字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
course = ["语文", "数学", "物理", "计算机"]

# 1)	画出班级所有学生的总分的散点图
plt.scatter(data["姓名"].values, data["总分"].values)
plt.xticks(rotation=90)
plt.show()

# 2)	画出所有学生的四门课程成绩的折线图；
chinese, = plt.plot(data["姓名"].values, data["语文"].values)
math, = plt.plot(data["姓名"].values, data["数学"].values)
physics, = plt.plot(data["姓名"].values, data["物理"].values)
computer, = plt.plot(data["姓名"].values, data["计算机"].values)
plt.legend(handles=[chinese, math, physics, computer], labels=course, loc="best")
plt.xticks(rotation=90)
plt.show()

# 3)	画出四门课程平均分的柱形图；
sum_chinese = sum(data["语文"].values) / len(data["语文"])
sum_math = sum(data["数学"].values) / len(data["数学"])
sum_physics = sum(data["物理"].values) / len(data["物理"])
sum_computer = sum(data["计算机"].values) / len(data["计算机"])

plt.bar(range(4), [sum_chinese, sum_math, sum_physics, sum_computer])
plt.xticks(range(4), course)
for a, b in zip(range(4), [sum_chinese, sum_math, sum_physics, sum_computer]):
	plt.text(a, b, "{:.2f}".format(b), ha="center", va="bottom", fontsize=7)
plt.show()

# 4)	在一个画布上用六个子图画出前六名学生的四门课程成绩的饼图；
data.sort_values(by="总分", inplace=True, ascending=False)
first_to_sixth = data.iloc[:6:, ]

for i in range(1, 7):
	plt.subplot(2, 3, i)
	data1 = first_to_sixth.iloc[i - 1, [3, 4, 5, 6]]
	data2 = first_to_sixth.iloc[i - 1, [7]]
	data1["语文"] = data1["语文"] / data2["总分"]
	data1["数学"] = data1["数学"] / data2["总分"]
	data1["物理"] = data1["物理"] / data2["总分"]
	data1["计算机"] = data1["计算机"] / data2["总分"]
	plt.pie(data1, labels=course, autopct="%.1f%%")
	name = first_to_sixth.iloc[i - 1, [1]]
	plt.title(name["姓名"])
plt.show()

# 5)	画出四门课程所有学生成绩分布的箱线图，如果有异常值，输出该分数。
plt.boxplot((data["语文"], data["数学"], data["物理"], data["计算机"]), labels=course)
plt.show()

for n in range(4):
	score = data[course[n]]
	# 上四分位
	Q3 = score.quantile(0.75)
	# 下四分位
	Q1 = score.quantile(0.25)
	# 上限值
	val_up = Q3 + 1.5 * (Q3 - Q1)
	# 下限值
	val_down = Q3 - 1.5 * (Q3 - Q1)

	for i in range(len(score)):
		if score[i] < val_down or score[i] > val_up:
			name = data.loc[data[course[n]] == score[i]]
			for k in name["姓名"]:
				a: object = k
			print(f"{course[n]}科目出现异常分数，最低分为：{score[i]}")
			print(f"{course[n]}科目出现异常分数的姓名为：{a}")
