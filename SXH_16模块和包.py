# 定义模块
# def 函数名(a,b):
#
#     print(a + '是' + b + '的师傅')
#     #print(f'{a}是{b}的师傅')  #与上面一样
#
# if __name__ == '__main__':
#     函数名('小甲鱼', '孙兴华')
#
# # print(__name__)   # 输出为 __main__

#导入模块三种方法

#1.import 模块名
# import random
# print(random.randint(1,10))


#2. from 模块名 import 功能1，功能2,功能3
# from random import randint  #从random里导入randint
# print(randint(1,10))


#3.from 模块名 import *
# from random import *
# print(randint(1,10))

# as 定义别名：  与SQl 的as一致
# 模块定义别名
#import 模块名 as 别名
# import random as 随机数
# print(随机数.randint(1,10))

# 功能定义别名
# from 模块 import 功能 as 别名
# from random import randint as 随机参数
# print(随机参数(1,10))

######
#   _all_  all列表
# 如果一个模块文件中有_all_变量，当使用from xxx import *导入时只能导入这个列表中的元素
# __all__ = ['猴']
#
# def 猴():
#     print('齐天大圣-孙悟空')
# def 猪():
#     print('天蓬元帅-猪八戒')
# from all列表 import *
# 猴()
# 猪()  #报错

#-------------- 包
#    LV
#导入包 两种方法
#方法1
# import 包名.模块名  #导入
# 包名.模块名.目标    #调用

# import LV.LV001
# LV.LV001.lv1()

#方法2  必须在__init__.py文件中添加_all_=[],控制允许导入的模块列表
#from 包名 import * #导入
# 模块名.目标 #调用

# from LV import *
# LV001.lv1()



























