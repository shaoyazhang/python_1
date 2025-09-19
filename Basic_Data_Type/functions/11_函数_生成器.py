'''
生成器：
    生成器本质是迭代器
    创建生成器两种方案：
        1. 生成器函数
        2. 生成器表达式
        
    生成器函数
        关键字yield
        生成器函数执行的时候，并不会执行函数，得到的是生产器
        
        yield: 只要函数中出现了yield，它就是一个生成器函数
        作用：
            1. 可以返回数据
            2. 可以分段执行函数中的内容，通过__next()__可以执行到下一个yield位置
            
        优势：用好了，特别节省内存
'''

# def func():
#     print(123456)
#     yield 999 # yield也有返回的意思，只有执行next的时候才会返回数据
    
# ret = func()
# print(ret)
# ret.__next__() # 
# print(ret.__next__())

'''yield可以分段执行函数'''
# def func():
#     print(123)
#     yield 666
#     print(456)
#     yield 999
    
# ret = func()
# print(ret.__next__())
# print(ret.__next__())

# 去工厂定制10000件衣服
# def order():
#     for i in range(10000):
#         list.append(f"衣服{i}")
#     return list

'''生成器函数节省内存'''
def order():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst 
            # 下一次拿数据
            lst =  []
            
gen = order()
print(gen.__next__())
print(gen.__next__())

