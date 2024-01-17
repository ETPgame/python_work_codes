# -*- coding: gbk -*-
import pandas as pd

df = pd.read_csv("./WenZhou_Weather.csv", encoding="gbk")

# 温度去除℃符号
df['最高气温'] = df['最高气温'].str.rstrip('℃').astype(int)
df['最低气温'] = df['最低气温'].str.rstrip('℃').astype(int)

# 风力去除级别
df['风力'] = df['风力'].str.rstrip('级').astype(int)

# 日期处理
df['日期'] = pd.to_datetime(df['日期'], format='%Y-%m-%d')

# 提取星期信息
df['星期'] = df['日期'].dt.day_name()

# 检查缺失值
print(df.isnull().sum())

df.to_csv("./Clean_Wenzhou_Weather.csv",encoding="gbk")
