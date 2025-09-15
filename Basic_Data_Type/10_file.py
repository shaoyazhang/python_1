'''
1. 找到这个文件，双击打开它

open(文件路径, mode="", encoding="")
    文件路径：
        1. 绝对路径
            d:/test/xxxx.txt
        2. 相对路径
            相对于当前的程序所在的文件夹
            
    mode:
        r: read
        w: write
        a: append 追加写入
        b: 读取的是非文本文件 ->bytes
    
    with:
        上下文，不需要手动去关闭文件
        
'''

import os
import time # 和系统操作相关的模块引入
# print("当前工作目录:", os.getcwd())
# f = open("国产自拍.txt", mode="r", encoding="utf-8")
# content = f.read()
# print(content)


'''
读取一行
'''
# line = f.readline().strip()
# print(line)

# line = f.readline().strip()
# print(line)

# line = f.readline().strip()
# print(line)

# line = f.readline().strip()
# print(line)

# line = f.readline().strip()
# print(line)

# line = f.readline().strip()
# print(line)

'''
读取多行
'''
# content = f.readlines()
# print(content)

# 最重要的一种文本读取方式
# for line in f:  # 从f中读取每一行
#     print(line.strip())
    
'''
写入文件
'''  
# w模式下，每一次open文件都会情况文件中的内容
# f = open("嫩模.txt", mode="w", encoding="utf-8")
# f.write("胡辣汤")
# f.close()

# lst = ["张无忌", "汪峰", "章子怡", "赵敏"]
# f = open("打架.txt", mode="w", encoding="utf-8")
# for item in lst:
#     f.write(item)
#     f.write("\n")
    
# f.close()

# f = open("打架.txt", mode="a", encoding="utf-8")
# f.write("你好厉害")
# f.close()

# with open
# with open("国产自拍.txt", mode="r", encoding="utf-8") as f:
#     for item in f:
#         print(item.strip())

'''
读取图片
'''
# with open("赵丽颖.png", mode="rb") as f:
#     for line in f:
#         print(line)

'''
文件的复制：
从源文件中去读取内容，写入到新路径去
'''
# with open("赵丽颖.png", mode="rb") as f1, \
#     open("胡一菲.png", mode="wb") as f2:
#         for line in f1:
#             f2.write(line)

'''
文件修改
把文件中的周 -> 张
'''
with open("人名单.txt", mode="r", encoding="utf-8") as f1, \
    open("人名单_副本.txt", mode="w", encoding="utf-8") as f2:
        for line in f1:
            line = line.strip() # 去掉换行
            if line.startswith("周"):
                line = line.replace("周", "张")
            f2.write(line)
            f2.write("\n")
            
# 删除源文件
time.sleep(3)
os.remove("人名单.txt")
time.sleep(3)
# 把副本文件重命名成源文件
os.rename("人名单_副本.txt", "人名单.txt")

