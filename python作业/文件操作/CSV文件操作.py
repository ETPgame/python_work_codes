import csv

file_path = "C:\\Users\\lenovo\\Desktop\\实验06-文件操作"
data = []
with open(file_path+"\\data.csv", "r") as f:
    reader = csv.reader(f)
    head = next(reader)
    for i in reader:
        x = float(i[1])*float(i[2])
        i.append(str(x))
        data.append(i)

with open(file_path+"\\data_new.csv", "w", newline='') as f2:
    writer = csv.writer(f2)
    head.append("销售金额")
    writer.writerow(head)
    writer.writerows(data)
