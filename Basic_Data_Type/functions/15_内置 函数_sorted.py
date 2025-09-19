'''
sorted: 排序
filter: 筛选
map: 映射
'''

'''sorted'''
# lst = [16, 22, 68, 1, 147, 256, 49]
# ret = sorted(lst, reverse=True)
# print(ret)

lst = ["秋", "张二嘎", '比克', '卡卡罗特', '超级宇宙无敌大帅B']
# def func(item): # item对应的就是列表中的每一项数据
#     return len(item)
# func = lambda x: len(x)
s = sorted(lst, key=lambda x: len(x))
# print(s)

lst2 = [
    {"id": 1, "name": '周润发', 'age': 18, 'salary': 5200},
    {"id": 2, "name": '周星驰', 'age': 28, 'salary': 56000},
    {"id": 3, "name": '周海媚', 'age': 78, 'salary': 561230},
    {"id": 4, "name": '周伯通', 'age': 12, 'salary': 56000},
    {"id": 5, "name": '周大兴', 'age': 35, 'salary': 53210},
    {"id": 1, "name": '周有辣', 'age': 47, 'salary': 560},
    {"id": 1, "name": '周扒皮', 'age': 68, 'salary': 12000}
]

# 1. 根据年龄排序
s1 = sorted(lst2, key=lambda d: d['age'])
# print(s1)

# 2. 根据工资从大到小
s2 = sorted(lst2, key=lambda d: d['salary'], reverse=True)
# print(s2)

'''filter'''
lst3 = ['张无忌', '张三丰', '张翠山', '灭绝师太', '小狐仙']
f = filter(lambda x: not x.startswith('张'), lst3)
# print(list(f))

lst4 = [1, 2, 3, 4, 5, 6, 7]
ret = [item * item for item in lst4]
# print(ret)
r = map(lambda x: pow(x, 2), lst4)
print(list(r))
