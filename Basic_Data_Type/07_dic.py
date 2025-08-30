
# 首先，字典是以键值对的形式进行存储数据的
# 字典的表示方式 {key:value, ...}

# dic = {"jay":"周杰伦", "金毛狮王":"谢逊"}
# val = dic["金毛狮王"] # 用起来只是把索引换成了key
# print(val)

# 字典的key必须是可哈希的数据类型(不可变)

# str = "第一名"
# dic = {str:123}
# dic = {[]:123} # 不允许
# print(dic)

# 字典的value可以放任何数据类型
# dic = {"汪峰的孩子":["孩子1", "孩子2"]}
# print(dic)


# 字典的增删改查
# dic = dict()

# dic["jay"] = "周杰伦"
# dic[1] = 123

# dic["jay"] = "昆凌" # 此时，字典中已经有了jay，此时执行的就是修改操作了
# print(dic)

# dic.setdefault("tom", "胡辣汤") # 设置默认值，如果一起已经有了tom了，setdefault就不起作用了
# dic.setdefault("tom", "呵呵哒") # 不起作用
# print(dic)

# 删除
# dic.pop("jay")
# print(dic)

# del dic["tom"] # 不建议用
# print(dic)


# 查询
# print(dic["jay"]) # 如果key不存在，会报错 --》当你确定你dkey是没问题
# print(dic.get("jay")) # 如果key不存在，程序返回 none --》当你步确定你dkey是没问题

# none
# a = None # 单纯的就是空，表示没有的意思
# print(type(a))


# 举例
# dic = {
#     "赵四": "特别能歪嘴",
#     "刘能": "老，老四啊...",
#     "大脚": "跟这个和那个搞对象",
#     "大脑袋": "瞎折腾..."
# }

# name = input("亲输入你想知道的我们村的人的名字: ")
# val = dic.get(name)
# if val is None:
#     print("没这个人")
# else:
#     print(val)


# 字典的循环和嵌套
 
# dic = {
#     "赵四": "特别能歪嘴",
#     "刘能": "老，老四啊...",
#     "大脚": "跟这个和那个搞对象",
#     "大脑袋": "瞎折腾..."
# }

# 1. 可以用for循环，直接拿到key
# for key in dic:
#     print(key, dic[key])
    
# 2. 希望把所有的key全都保存在一个列表中
print(list(dic.keys())) # 拿到所有的key

# 3. 希望把所有value防止一个列表中
# print(list(dic.values()))


# 4. 直接拿到字典中的key和value
# print(dic.items())
# for key, val in dic.items(): # 可以直接拿到字典所有的key和value
#     # key = item[0]
#     # val = item[1]
#     # print(key, val)
#     # key, val = item
#     # print(item) # 确定，item中只有两项元素，是元组
#     print(key, val)
    
# a, b = (1, 2) # 元组或者列表都可以执行该操作，该操作被称为解构（解包）
# print(a)
# print(b)


# 字典的嵌套
# wangfeng = {
#     "name": "汪峰",
#     "age": "18",
#     "wife": {
#         "name": "章子怡",
#         "hobby": "演戏",
#         "assistant": {
#             "name": "樵夫",
#             "age": 25,
#             "hobby": "打游戏",
#         }
#     },
#     "kids": [
#         {"name": "孩子1", "age": 13},
#         {"name": "孩子2", "age": 10},
#         {"name": "孩子3", "age": 18}
#     ]
# }

# 汪峰妻子的助手的名字
# name = wangfeng["wife"]["assistant"]["name"]
# print(name)

# 给汪峰的第二个孩子加1随
# wangfeng["kids"][1]["age"] = wangfeng["kids"][1]["age"]+1
# print(wangfeng)

# 补充
dic = {
    "赵四": "特别能歪嘴",
    "刘能": "老，老四啊...",
    "大脚": "跟这个和那个搞对象",
    "大脑袋": "瞎折腾..."
}

temp = []
for key in dic:
    # print(key) # 这里只有key
    if key.startswith("大"):
        temp.append(key)

for t in temp:
    dic.pop(t)
    
print(dic)
