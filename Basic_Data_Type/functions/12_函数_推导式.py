'''
推导式：
    简化代码
    语法：
        1. 列表推导式：[数据 for循环 (if判断)]
        2. 集合推导式: {数据 for循环 (if判断)}
        3. 字典推导式：{k:v for循环 (if判断)}
        
    (数据 for循环 (if判断)) -> 不是元祖推导式，根本没有元祖推导式，叫生成器表达式
    
    生成器表达式：-> 一次性的
        语法： (数据 for循环 (if判断))
'''
# lst = [i for i in range(10)]
# print(lst)

'''1. 创建一个列表[1,3,5,7,9]'''
# lst = [i for i in range(1, 10, 2)]
# lst = [i for i in range(10) if i % 2 == 1]
# print(lst)

'''2. 生成50件衣服'''
lst = [f"衣服{i}" for i in range(50)]

'''3. 将如下列表中所有的英文字母修改成大写'''
lst1 = ["allen", "tony", "kevin", "skyler"]
lst2 = [item.upper() for item in lst1]
# print(lst2)

'''集合推导式'''
s = {i for i in range(10)} # 集合

'''字典推导式：请将下列的列表修改成字典，要求 索引作为key，数据作为value'''
lst3 = ["赵本山", '潘长江', '高达', '奥特曼']
dic = {k:lst3[k] for k in range(len(lst2))}
# print(dic)

gen = (i**2 for i in range(10))
# print(gen.__next__())
# for item in gen:
#     print(item)
    
# lst4 = list(gen)
# print(lst4)

# s = list("周杰伦") #list => for => next()
# print(s)