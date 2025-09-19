'''
分类：
    1. 形参，在定义函数的时候，需要准备一些变量来接收信息
        a. 位置参数，按照位置一个一个的取声明变量
        b. 默认值参数，在函数声明的时候给变量一个默认值，如果实参不传递信息，此时默认值生效，否则不生效
        c. 动态传参
            1. *args，表示接收所有的位置参数的动态传参
            2. **kwargs，表示接收所有的关键字的动态传参
        顺序：位置参数 >*args > 默认值参数 > **args
            
    2. 关键字参数: 按照 位置 进行传递参数
    3. 混合参数，
        顺序：位置参数放前面，关键字参数放后面 ->否则报错
        实参在执行的时候，必须要保障形参有数据
'''

'''
位置参数
'''
# def luru(name, age, gender="男"):
#     print(name, age, gender)  
# luru("张三", 18)

'''
动态位置参数
'''
# def chi(*food): # * 表示位置参数的动态传参, *接收到的值会被统一放在一个元组里面
#     print(food)
    
# chi("大米饭", "烧茄子", "紫菜蛋花汤", "哈根达斯")
# chi("大米饭")
# chi("紫菜蛋花汤", "哈根达斯")
  
'''
关键字参数
'''  
# def chi(zhu, fu, tang, tian):
#     print(zhu, fu, tang, tian)
    
# chi(zhu = "大米饭", fu="烧茄子", tang="紫菜蛋花汤", tian="哈根达斯")

'''
动态关键字参数
'''
# def chi(**food): # ** 表示接受关键字的动态传参， 接收到的所有参数都会处理成字典
#     print(food)

# chi(fu="木须柿子", zhu="小米饭")


'''
混合使用
默认值参数 c 何时能产生默认值：*args放前面
1. 位置参数（positional）
2. 可变位置参数 *args
3. 仅限关键字参数（keyword-only, 在 * 或 *args 之后定义的）
4. 默认值参数（如果有的话）
5. 可变关键字参数 **kwargs

'''
# def func(a, b, c="哈哈哈", *args, **kwargs):
#     print(a, b, c, args, kwargs)

# def func(a, b, *args, c="哈哈哈",**kwargs):
#     print(a, b, c, args, kwargs)

# func(1,2,3,4,5,6,7,8,9) # kwargs为空，因为里面没有给关键字
# func(1,2,3,4,5,6,7,8,9, hello=456, hahalou=654)
# func(1,2, hello=456, hahalou=654)
# func(1,2,3,4,c="呵呵")


'''
*args 与 **kwargs 混用
'''
# def func(*args, **kwargs): # 没有限制的接收任何参数
#     print(args, kwargs)
    
# func()
# func(1)
# func(1,2,3,a=2)

'''
列表、字典与可变参数的使用
'''
stu_lst = ["流川枫", "樱木", "大老王", "隔壁老王"]
def func(*args):
    print(args)

# *在实参位置，把列表打三次位置参数进行传递
# ** 在实参位置，把字典打三次位置参数进行传递
func(*stu_lst)  
