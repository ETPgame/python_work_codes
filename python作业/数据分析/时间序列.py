import matplotlib.pyplot as plt
import pandas as pd

# 1)    将数据存为一个名叫 apple 的数据框。
apple = pd.read_csv(r"D:\\我的\\大学\\大二下\\python课\\实验08-数据分析\\data\\appl_1980_2014.csv")

# 2)    查看前 10 行内容。
print(apple[:10])

# 3)    数据集中有多少个列(columns)？
print(apple.shape[1])

# 4)    打印出全部的列名称？
print(apple.columns)

# 5)    数据集的索引是怎样的？
print(apple.index)

# 6)    查看每一列的数据类型。
print(apple.dtypes)

# 7)    将 Date 这个列转换为 datetime 类型(替换数据)。
apple.Date = pd.to_datetime(apple.Date)

# 8)    将 Date 设置为数据的索引。
apple = apple.set_index("Date")

# 9)    有重复的日期吗？
if apple.index.is_unique:
    print("无重复的日期")
else:
    print("有重复的日期")

# 10)   将 index 设置为升序。
print(apple.sort_index(ascending=True).head())

# 11)   数据集中最早的日期和最晚的日期相差多少天？
date_sub = apple.index.max()-apple.index.min()
print(date_sub)

# 12)   按照时间顺序可视化 Adj Close 值。
apple_open = apple["Adj Close"]
plt.plot(apple_open)
plt.show()
