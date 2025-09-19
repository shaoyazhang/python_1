'''
内容回顾：
    1. 函数可以作为参数进行传递
    2. 函数可以作为返回值进行返回
    3. 函数名称可以当成变量意义进行赋值操作
    
装饰器：-> 要求记住最后的结论
    装饰器本质上是一个闭包
    作用：在不改变原有函数调用的情况下，给函数增加新的功能
    直白：可以在函数前后增加功能，但是不改变原来的代码
    
    使用情况：
    在用户登录的地方，日志
    通用装饰器的写法:
        def wrapper(fn): wrapper: 装饰器 fn: 目标函数
            def inner(*args, **kwargs):
                #在目标函数执行之前..
                ret = fn(*args, **kwargs) # 执行目标函数
                # 在目标函数执行之后..
                return ret
            return inner
            
        @wrapper
        def target():
            pass
        target() => inner()
        
    一个函数可以被多个装饰器装饰
    规则和规律：wrapper1 wrapper2 TARGET wrapper2 wrapper1
'''

'''装饰器基本应用'''
# def guanjia(game):
#     def inner():
#         print("打开外挂")
#         game()
#         print("关闭外挂")
#     return inner
    
# @guanjia    # 相当于 play_dnf = guanjia(play_dnf)
# def play_dnf():
#     print("你好啊，我叫赛利亚，今天又是美好的一天!")

# @guanjia 
# def play_lol():
#     print("德玛西亚")
   


# print("开挂") 
# play_dnf()
# print("关闭外挂")
# print("开挂")
# play_lol()
# print("关闭外挂")

# play_dnf = guanjia(play_dnf) # 让管家把游戏重新封装一遍，我这边把原来的游戏替换了
# play_dnf() # 此时运行的是管家给的内层函数inner
# play_lol = guanjia(play_lol)
# print("===========================")
# play_lol()

'''装饰器参数问题'''
# def guanjia(game):
#     # *, ** 表示接收所有参数，打包成元组和字典
#     def inner(*args, **kwargs): # inner添加了参数，args一定是一个元组，kwargs一定是字典
#         print("打开外挂")
#         # *, ** 表示把args元组和kwargs字典打散成位置参数和关键字参数传递进去
#         game(*args, **kwargs) # 
#         print("关闭外挂")
#     return inner

# @guanjia
# def play_dnf(username, password):
#     print("我要开始玩dnf了", username, password)
#     print("你好啊，我叫赛利亚，今天又是美好的一天!")

# @guanjia
# def play_lol(username, password, hero):
#     print("我要开始玩lol了", username, password, hero)
#     print("德玛西亚")
    
# play_dnf("admin", "password") # inner
# print("===========================================")
# play_lol("admin", "password", "打盖伦")


'''装饰器返回值问题'''
# def guanjia(game):
#     # *, ** 表示接收所有参数，打包成元组和字典
#     def inner(*args, **kwargs): # inner添加了参数，args一定是一个元组，kwargs一定是字典
#         print("打开外挂")
#         # *, ** 表示把args元组和kwargs字典打散成位置参数和关键字参数传递进去
#         ret = game(*args, **kwargs) # 这里是目标函数的执行，这里是能够拿到从目标函数返回的返回值的
#         print("关闭外挂")
#         return ret
#     return inner

# @guanjia
# def play_dnf(username, password):
#     print("我要开始玩dnf了", username, password)
#     print("你好啊，我叫赛利亚，今天又是美好的一天!")
#     return '一把屠龙刀'

# def play_lol(username, password, hero):
#     print("我要开始玩lol了", username, password, hero)
#     print("德玛西亚")
    
# ret = play_dnf("admin", "password") # inner
# print(ret)


'''多个装饰器'''
# def wrapper1(fn):   # fn:wrapper2.inner
#     def inner(*args, **kwargs): 
#         print('这里是warpper1进入') # 1
#         ret = fn(*args, **kwargs) # wrapper2.inner
#         print('这里是warpper1出去') # 5
#         return ret
#     return inner

# def wrapper2(fn):   # fn: target
#     def inner(*args, **kwargs):
#         print('这里是warpper2进入') # 2
#         ret = fn(*args, **kwargs) # target
#         print('这里是warpper2出去') # 4
#         return ret
#     return inner
# @wrapper1  # target = wrapper1(wrapper2.inner)， 此时 target => wrapper1.inner
# @wrapper2 #  target = wrapper2(target) 此时 target => wrapper2.inner
# def target():
#     print('我是目标') # 3
    
# target()

'''装饰器实战'''
login_flag = False

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag == False:
            # 这里完成登录校验
            while 1:
                username = input("用户名>>>>")
                pwd = input("密码>>>")
                if username == "admin" and pwd == "123":
                    print("登录成功")
                    login_flag = True
                    break
                else:
                    print("用户名或密码错误")

        ret = fn(*args, **kwargs) # 后续的程序
        return ret
    return inner


@login_verify
def add():
    print("添加员工信息")

@login_verify   
def delete():
    print("删除员工信息")

@login_verify   
def update():
    print("修改员工信息")

@login_verify  
def search():
    print("查询员工信息")
    

add()
update()
delete()
search()