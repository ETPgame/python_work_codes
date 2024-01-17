import pandas as pd

information = {
	"学号": [111, 112, 113, 114, 115],
	"姓名": ["张一", "李二", "王三", "赵四", "孙五"],
	"语文": [91, 90, 89, 89, 83],
	"数学": [76, 87, 89, 96, 63],
	"外语": [66, 99, 95, 85, 76]
}
data = pd.DataFrame(information)
print(data)

# 增加总分列
sum_score = data["语文"] + data["数学"] + data["外语"]
data.insert(loc=len(data.columns), column="总分", value=sum_score)
print(data)

# 输出excel.
data.to_excel("D:\\我的\\大学\\大二下\\python课\\实验08-数据分析\\data.xlsx",
			  sheet_name="Sheet1", index=False)

# 语文成绩平均分
chinese_avg = data["语文"].mean()
print(f"语文成绩平均分: {chinese_avg}")

# 第三位同学的语数外三门课的平均分
avg = (data["语文"][2] + data["数学"][2] + data["外语"][2]) / 3.0
print(f"第三位同学的语数外三门课的平均分: {avg:.2f}")
