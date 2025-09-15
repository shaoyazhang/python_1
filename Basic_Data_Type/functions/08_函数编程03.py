'''
闭包：
    1. 可以让一个变量常驻于内存
    2. 可以避免全局变量被修改
    
'''

'''闭包函数'''
def func():
    a = 10
    def inner():
        nonlocal a
        # print(a)
        a += 1
        return a
    return inner

ret = func()

# inner => ret => 什么时候执行
r1 = ret()
print(r1)
# 100000
r2 = ret()
print(r2)