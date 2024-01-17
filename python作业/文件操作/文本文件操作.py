import os

file_path = "C:\\Users\\lenovo\\Desktop\\实验06-文件操作"
os.chdir(file_path)
with open(file_path+"\\素材\\data.txt", "r") as f:
    file1 = f.read()
    a = list(map(int, file1.split()))
a.sort()
file2 = open(file_path+"\\data_asc.txt", "w")
for i in a:
    file2.write(str(i)+"\n")
    print(str(i)+"\n", end="")
file2.close()
