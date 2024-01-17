import json

file_path = "C:\\Users\\lenovo\\Desktop\\实验06-文件操作"
information = [
    {'小区名称': '小区A', '均价': 8000, '月交易量': 20},
    {'小区名称': '小区B', '均价': 8500, '月交易量': 35},
    {'小区名称': '小区C', '均价': 12000, '月交易量': 50},
    {'小区名称': '小区D', '均价': 20000, '月交易量': 18}]

with open(file_path+"\\house.json", "w") as f:
    json.dump(information, f, ensure_ascii=False, indent=4, separators=[",", ":"])

with open(file_path+"\\house.json", "r") as f:
    read = json.load(f)
    for i in read:
        print(i)
