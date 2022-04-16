# 函数必须先定义再调用
# 定义函数：def 函数名 (形参) a,b,x,y
# 调用函数： 函数名 (实参)  10,100,58

# def add (a,b):
#     '''加法函数'''
#     i = a + b
#     print(i)
# add(520,1314)
#
# help(add)

# def info(name,age,sex):
#     print(f'您的姓名是{name},性别是{sex},年龄是{age}岁')
# #info('李中涛',18,'男')
# info('李中涛',age='20',sex='男')

# 默认参数
# def info(name,age,sex='男'):
#     print(f'您的姓名是{name},年龄是{age},性别是{sex}')
#
# info('李中涛',18)
# info('杨德馨',18,sex = '女')

# 可变参数(收集参数)
#1.位置可变参数(接受所有的位置参数,返回一个元组)

# def name(*args):
#     print(args)
# name(20)
# name(20,30)

#2.关键字可变参数(接受所有关键字,返回一个字典)

# def name(**kwargs):
#     print(kwargs)
# name(长=20,宽=30,高=10)


#局部变量 定义在函数内部的变量.即只在函数内部生效

# def name():
#     a = 520
#     print(a)
# name()
# print(a) #报错

#全局变量 定义在函数外部的变量
# a = 520
#
# def name():
#     print(a)
#
# name()
# print(a)

# a = 520
# def name():
#     global a #声明a是一个全局变量
#     a = 1314
#     print(a)
# name()
# print(a)  # a被修改;  global先声明后调用

# a = 1314
#
# def name1():
#     global a #声明a为全局变量
#     a = 520  #修改变量a的值
#     print(a)
#
# def name2():
#     print(a)
#
# name1()  #将a修改为520
# name2()  #打印a,输出520

#return
# def name(a,b):
#     return a + b
#
# x = name(20,30)
# print(x)


# def name1():
#     return 520
#
# def name2(a):
#     print(a)
#
# b = name1()
# print(b)
# name2(b)

#元组拆包
# def name():
#     return 520,1314
# a,b = name()
#
# print(a)
# print(b)

#字典拆包
c = {'姓名':'李中涛','年龄':20}

def name():
    return c

a,b = name()
print(a)
print(b)

print(c[a])
print(c[b])





































