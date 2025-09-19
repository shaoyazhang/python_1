'''
iterable 可迭代的东西
iterator 迭代器
str, list, uple, dict, open()...
可迭代的数据类型都会提供一个叫迭代器的东西，这个迭代器可以帮我们把数据类型中的所有数据逐一拿到

获取迭代器的两种方案：
    1. next()内置函数
    2. __iter__() 特殊方法
    
for里面一定是要拿迭代器的，所以所有不可迭代的东西不能用for循环
for循环里面一定有__next__出现

总结：迭代器统一了所有不同数据类型的遍历工作

迭代器本身也是可迭代的

迭代器本身特性：
    1. 只能向前，不能反复
    2. 特别省内存
    3. 惰性机制
    
'''

# it = iter("你叫什么名字")
# print(next(it))

# it = "呵呵哒".__iter__()
# print(it)

'''拿迭代器的两种方式'''
# print(it.__next__())
# print(it.__next__())
# print(next(it))

'''模拟for循环工作原理'''
# s = '我是数据'
# it = s.__iter__()
# while 1:
#     try:
#         data = it.__next__()
#         print(data)
#     except StopIteration:
#         break
# print(123456)


'''迭代器本身也是可迭代的'''
s = '你好啊，我叫赛利亚'
it = s.__iter__()

for mm in it:
    print(mm)