# def fc(a):
#     if a == 1:
#         return 1
#     b = a + fc(a-1)
#     return b
# c = fc(998)
# print(c)

# 函数式编程
# lambda表达式
# lambda 形参：表达式  #形参可省略
# def  a():
#     return 520
# print(a())
#
# #上面式子等价于
# b = lambda:520
# print(b())

#eg2
# def fc(a,b):
#     return a+b
# c = fc(520,1314)
# print(c)
# #等价于
# d= lambda a,b : a+b
# print(d(520,1314))
#
# print((lambda a,b : a+b)(520,1314))

#lambda默认参数
# def x(a,b,c=5):
#     return a+b+c
# print(x(2,6))
# print((lambda a,b,c=5:a+b+c)(2,6))#c默认为5

#可变位置参数  *args
# def x(*args):  #元组
#     return args
# print(x(1,1,5,8))
#
# print((lambda *args:args)(1,1,5,8))

#可变关键字参数 **kwargs
# def x(**kwargs):
#     return kwargs
# print(x(name='李中涛',age=18))
#
# print((lambda **kwargs:kwargs)(name='李中涛',age=20))
#返回的是一个字典


#带判断/条件的lambda
# def x(a,b):
#     return a if a > b else b
# print(x(1,2))
#
# print((lambda a,b: a if a > b else b)(1,2))

#列表中的字典排序：了解一下
# a = [{'name':'hardy','age':20},{'name':'YDX','age':18},{'name':'LZT','age':21}]
# print(a)
#
# a.sort(key = lambda x:x['age'],reverse=False)
# print(a)

#函数式编程之高阶函数
#高阶函数：就是基于已有的函数定义新的函数，以函数为参数，返回也是参数
#
# def x(a,b):
#     return abs(a) + abs(b)
# c = x(-5,3)
# print(c)
#
# def y(a,b,c):
#     return c(a) + c(b)
# d = y(-5,3,abs)
# print(d)

#函数式编程之--内置--高阶函数
#1、filter(函数名,可迭代对象) 作用：过滤序列中不符合条件的元素
# a = [1,2,3,4,5,6,7,8,9,10]
# # a = range(1,11)
# def y(x):
#     return x % 2 ==0
# b = filter(y,a)
# print(b) #打印的是对象地址
# print(list(b))
#
# print(list(filter(lambda x:x % 2 ==0,a)))
# print(list(filter(lambda x:x % 2 ==0,range(1,11))))

#2map(函数名,迭代对象)
#作用:将可迭代对象的每一个元素作为函数的参数进行运算加工,直到可迭代序列每个元素都加工完毕

#计算列表序列中个数字的2次方
# a= [1,2,3,4]
# def y(x):
#     return x ** 2
# 结果 = map(y,a)
# print(结果)
# print(list(结果))
#
# print(list(map(lambda x : x ** 2,range(1,5))))

#3.reduce(函数名(x,y),可迭代对象)
#作用:函数中必须有两个参数,每次参数计算的结果继续和序列的下一个元素做累计运算
# 计算下面列表数据之和
import  functools #导入模块
a = [1,2,3,4]
def y(a,b):
    return a+b
结果 = functools.reduce(y,a)
print(结果)

print(functools.reduce(lambda x,y: x+y,a))
print(functools.reduce(lambda x,y: x+y,range(1,5)))
print(functools.reduce(lambda x,y: x+y,range(1,101)))
# 累加时推荐使用 只需改动range(开始,结束+1,步长)
print(functools.reduce(lambda x,y: x+y,range(0,101,2)))














