import pandas as pd

# 读取drinks.csv
drinks = pd.read_csv(r"D:\\我的\\大学\\大二下\\python课\\实验08-数据分析\\data\\drinks.csv")
print(drinks)

# 2)    哪个大陆(continent)平均消耗的啤酒(beer)更多？
beer = drinks.groupby("continent")["beer_servings"].mean()
beer_max = beer[beer == beer.max()]
for i in beer_max.index:
    a = i
print(f"{a}平均消耗的啤酒更多:{beer_max[a]:.2f}")
print()

# 3)    打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值。
wine = drinks.groupby("continent")["wine_servings"].sum()
for i in wine.index:
    print(f"{i}的红酒消耗:{wine[i]}")
print()

# 4)    打印出每个大陆每种酒类别的消耗平均值。
drink_avg = drinks.groupby("continent")[["beer_servings", "spirit_servings", "wine_servings"]].mean()
for i in drink_avg.index:
    a = drink_avg.loc[i]
    print(f"{i}消耗beer平均为:{a['beer_servings']:.2f}")
    print(f"{i}消耗spirit平均为:{a['spirit_servings']:.2f}")
    print(f"{i}消耗wine平均为:{a['wine_servings']:.2f}")
print()

# 5)    打印出每个大陆每种酒类别的消耗中位数。
drink_median = drinks.groupby("continent")[["beer_servings", "spirit_servings", "wine_servings"]].median()
for i in drink_median.index:
    a = drink_median.loc[i]
    print(f"{i}消耗beer中位数为:{a['beer_servings']:.2f}")
    print(f"{i}消耗spirit中位数为:{a['spirit_servings']:.2f}")
    print(f"{i}消耗wine中位数为:{a['wine_servings']:.2f}")
print()

# 6)    打印出每个大陆对 spirit_servings 饮品消耗的平均值，最大值和最小值。
spirit_mean = drinks.groupby("continent")["spirit_servings"].mean()
spirit_max = drinks.groupby("continent")["spirit_servings"].max()
spirit_min = drinks.groupby("continent")["spirit_servings"].min()
for i in spirit_mean.index:
    print(f"{i}对 spirit_servings 饮品消耗的平均值:{spirit_mean[i]:.2f}")
for i in spirit_max.index:
    print(f"{i}对 spirit_servings 饮品消耗的最大值:{spirit_max[i]}")
for i in spirit_min.index:
    print(f"{i}对 spirit_servings 饮品消耗的最小值:{spirit_min[i]}")
