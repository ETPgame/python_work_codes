import os

print(os.getcwd())
os.chdir("D:\\")
print(os.getcwd())
dir_count = 0
file_count = 0
for root, dirs, filenames in os.walk("D:\\"):
    for dir in dirs:
        dir_count += 1
    for file in filenames:
        file_count += 1
print('dir_count ', dir_count)
print('file_count ', file_count)
os.chdir("C:\\Windows")
for i in os.listdir():
    if i[-4:] == ".exe":
        print(i)
