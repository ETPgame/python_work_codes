import os
import requests

path = "D:\\我的\\大学\\大二下\\python课\\实验09-网络爬虫及信息提取"
url = "https://p4.itc.cn/images01/20210805/814cbb6f46ad4bd3a1918eee34708a79.png"
png = url.split('/')[-1]
os.chdir(path)
print(os.getcwd())

r = requests.get(url)
print(r.status_code)

flog = False
while True:
   if png in os.listdir(path):
       png = png[:-4] + "(1)" + png[-4:]
       flog = True
       continue
   else:
       if flog:
           print(f"the file is already exist.the file will be saved as\n{png}")

       try:
           with open(path + "\\" + png, "wb") as f:
               f.write(r.content)
               print("image saved successfully.")
       except:
           print("image saved mistakenly.")

   break
