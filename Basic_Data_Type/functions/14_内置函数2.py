'''
zip

'''


lst1 = ["赵本山", '范伟', '苏有朋']
lst2 = [40, 38, 42]
lst3 = ['卖拐', '耳朵大有福', '情深深雨蒙蒙']

# ret = []
# for i in range(len(lst1)):
#     first = lst1[i]
#     second = lst2[i]
#     third = lst3[i]
#     ret.append((first, second, third))
# print(ret)

# ret = zip(lst1, lst2, lst3)
# print(dir(ret))
# for item in ret:
#     print(item)

# lst = list(ret)
# print("list:", lst)

'''locals()'''
# a = 188
# print(locals()) # 此时locals被写在了全局作用于范围内，此时看到的就是全局作用域中的内容

# def func():
#     a = 336
#     print(locals()) # 此时locals被写在局部作用域范伟，看到的就是局部作用域的内容
    
# func() 

'''globals()'''
c = 12
print(globals())

def func():
    a = 336
    print(globals()) 