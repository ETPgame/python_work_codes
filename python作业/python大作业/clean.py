# -*- coding: gbk -*-
import pandas as pd

df = pd.read_csv("./WenZhou_Weather.csv", encoding="gbk")

# �¶�ȥ�������
df['�������'] = df['�������'].str.rstrip('��').astype(int)
df['�������'] = df['�������'].str.rstrip('��').astype(int)

# ����ȥ������
df['����'] = df['����'].str.rstrip('��').astype(int)

# ���ڴ���
df['����'] = pd.to_datetime(df['����'], format='%Y-%m-%d')

# ��ȡ������Ϣ
df['����'] = df['����'].dt.day_name()

# ���ȱʧֵ
print(df.isnull().sum())

df.to_csv("./Clean_Wenzhou_Weather.csv",encoding="gbk")
