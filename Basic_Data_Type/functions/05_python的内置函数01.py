'''
直接能拿来用的函数
priint
input...
'''

'''
数学运算:
sum(), min(), max(), pow()
'''

'''list() '''
# s = {1, 2, 3}
# lst = list(s) # 内部有一个循环(for)
# print(lst)

'''slice(start, stop[, step])'''
# s = slice(1,4,2) # [1:4:2]
# print("呵呵呵呵哒呵呵"[s])

'''format, ord, chr'''
# a = 18
# print(format(a, "08b")) #b: 二进制

# a= "中" #python的内存中使用的是unicode
# print(ord(a)) # 中 字在unicode码位是20013
# print(chr(20013)) #给出编码位置，展示文字

# for i in range(300):
#     print(chr(i) + " ", end="")

'''enumerate,all, any'''

# print(all([0, "","呵呵"])) #当初 and 来看 f&t&t
# print(any([0, "","呵呵"])) # 当初 or 来看
lst = ["张无忌","张翠山", "张三丰"]
# for index, item in enumerate(lst):
#     print(index, item)
    
# # 相当于
# for i in range(len(lst)):
#     print(i, lst[i])

# for index, item in enumerate(lst, 2): # 可以更改索引
#     print(index, item)
    
s = "呵呵哒"
print("哈希值：", hash(s)) # 一定是一个数字 -> 想办法转化成内存地址，然后进行数据的存储 ->字典(集合)哈希表
print("id值: ", id(s))
print(dir(s)) # 当前这个数据能执行哪些数据操作