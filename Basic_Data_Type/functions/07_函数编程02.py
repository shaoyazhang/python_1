'''
global: 在全局，引入全局变量
nonlocal: 在局部，引入外层的局部变量
'''

a = 10
def func1():
    # a = 20 # 创建一个局部变量，并没有去改变全局变量中的a
    global a # 把外面的全局变量引入到局部
    a = 20 

func1()
# print(a)

def func2():
    a = 30
    def func2():
        # global a  # 这里找的是函数外面的变量a
        nonlocal a  # 向外找一层，看看有没有该变量，如果有就引入，没有，继续向外一层，直到全局（不包括）
        a = 50
    func2()
    print(a) # 打印的是函数自己声明的a

# func2() # 50
# print(a)

