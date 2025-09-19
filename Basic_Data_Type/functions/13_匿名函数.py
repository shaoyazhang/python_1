'''
匿名函数：
    lambda表达式
    语法：
        变量 = lambda 参数， 参数2，参数3,....: 返回值
'''

'''计算a+b的结果'''
def func(a, b):
    return a + b

fn = lambda a, b: a+b
# print(fn)

ret = fn(1, 2)
print(ret)