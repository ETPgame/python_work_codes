# Numpy文件读取和数据统计

import numpy as np

data = np.load("D:\\我的\\大学\\大二下\\python课\\实验08-数据分析\\data\\score1.npy")
print(data)

course = np.array(data[0, 2:5], dtype=str)
chinese = np.array(data[1:5, 2], dtype=int)
math = np.array(data[1:5, 3], dtype=int)
english = np.array(data[1:5, 4], dtype=int)

max_score = [np.max(chinese), np.max(math), np.max(english)]
min_score = [np.min(chinese), np.min(math), np.min(english)]
sub_score = [max_score[0]-min_score[0], max_score[1]-min_score[1], max_score[2]-min_score[2]]
avg_score = [np.mean(chinese), np.mean(math), np.mean(english)]
mid_score = [np.median(chinese), np.median(math), np.median(english)]
std_score = [np.round(np.std(chinese), 2), np.round(np.std(math), 2), np.round(np.std(english), 2)]

print(f"科目:{course}")
print(f"最高分:{max_score}")
print(f"最低分:{min_score}")
print(f"最值差:{sub_score}")
print(f"平均分:{avg_score}")
print(f"中位数:{mid_score}")
print(f"标准差:{std_score}")

# Numpy数据统计

math_scores = np.random.randint(40, 100, size=10)
eng_scores = np.random.randint(40, 100, size=10)
total_scores = np.add(math_scores, eng_scores)
math_avg = np.mean(math_scores)
eng_avg = np.mean(eng_scores)
total_avg = np.mean(total_scores)
math_std = np.round(np.std(math_scores), 2)
eng_std = np.round(np.std(eng_scores), 2)
total_std = np.round(np.std(total_scores), 2)

print("十名学生的数学成绩:")
print(math_scores)
print("十名学生的英语成绩:")
print(eng_scores)
print("十名学生的总分:")
print(total_scores)
print(f"平均数学成绩:{math_avg}")
print(f"平均英语成绩:{eng_avg}")
print(f"平均总分:{total_avg}")
print(f"数学成绩的标准差:{math_std}")
print(f"英语成绩的标准差:{eng_std}")
print(f"总分的标准差:{total_std}")

