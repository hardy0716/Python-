# a = int(input('请输入被除数（分子）：'))
# b = int(input('请输入除数（分母）：'))
#
# try:
#     print(a/b)
# except Exception as 出错信息:
#     print(f'出错了，出错信息是{出错信息}')
# else:
#     print('我是else，看到我证明这个程序没有异常')




# try:
#     变量名 = open('1999绝密文档.txt','r')
# except:
#     变量名 = open('1999绝密文档.txt','w')
#     print('没有这个文件，我新建了一个')
# else:
#     print('没有异常，我很开心')
# finally:     # 无论是否异常都要执行的语句 例如：关闭文件
#     变量名.close()

# with  打开文件不需要手动关闭，但是要注意缩进
# with 表达式 as 变量:
#       代码块
# try:
#     with open('1999绝密文档.txt','w') as 变量名:
#         for 遍历文件 in 变量名:
#             print(遍历文件)
# except Exception as 错误信息:
#     print(f'出错了，出错原因是{错误信息}')



#异常传递 了解即可
# import time
# try:
#     打开文件 = open('1999绝密文档.txt')
#
#     try:
#         while True:
#             读取内容 = 打开文件.readline()
#             if len(读取内容) == 0:
#                 break
#             time.sleep(2)
#             print(读取内容)
#     except:
#         #如果在读取过程中产生了异常就会捕捉到
#         #比如按下了ctrl + c
#         print('发生了意外终止')
#     finally:
#         打开文件.close()
#         print('文件关闭')
# except:
#     print('没有这个文件')




#######raise 自定义异常  raise 异常类对象
# # 作用：将不满足程序逻辑的情况，反馈给用户，就是用来报错，不是语法错误，而是不满足程序逻辑要求的错误。
# # 例如：输入密码长度不符合要求，很多网站都要求不能低于8位，要求大小写字母，要求有特殊字符等。

#自定义异常类，继承Exception

# class 密码(Exception):
#     def __init__(self,长度,最小长度):
#         self.长度 = 长度
#         self.最小长度 = 最小长度
#     def __str__(self):
#         return f'您输入的长度为{self.长度},不能少于{self.最小长度}个字符'
# def 自定义异常():
#     try:
#         用户输入 = input('请输入密码')
#         if len(用户输入) < 8:
#             raise 密码(len(用户输入),8)  #抛出异常
#     except Exception as 错误信息:
#         print(错误信息)
#     else:
#         print('密码已经输入完成')
# 自定义异常()


#存储数据 json模块
#(1)json.dump(要存储的数据,用于存储数据的文件对象) 存储数据到json格式的文件
#(2)json.load(用于存储数据的文件对象) 从json格式的文件读取到内存

# import json
#
# 列表 = [5,2,3,7,0,5]
# 文件名 = 'li1234567.json'
# with open('li1234567.json','w') as 变量名:
#     json.dump(列表,变量名)  #存储数字列表
#
# 文件名 = 'li1234567.json'
# with open(文件名) as 变量名:
#     变量名2 = json.load(变量名)  #将这个列表读取到内存
# print(变量名2)


#保存和读取用户生成的数据

#先存储用户输入的名字
# import json
# #将我们输入的名字存入【姓名】变量中
# 用户名 = input('请输入您的名字:')
#
# 文件名 = 'liname.json'
#
# with open(文件名,'w') as 文件对象:
#     #调用json.dump 将姓名和一个文件对象传递给他，从而将姓名存入这个文件当中
#     json.dump(用户名,文件对象)
#     print(f'{用户名}等你回来我会记得你')

#再写一个程序，向已经存储了名字的用户发出问候

# import json
# 文件名 = 'liname.json'
# with open(文件名) as 文件对象:
#     用户名 = json.load(文件对象)
#     print(f'{用户名}欢迎回来')  #{用户名}（上面已经存储过的，这次会直接报出）欢迎回来



#将上面两个程序合并起来
#如果意钱存取了用户名，就加载它
#否则，就提示用户输入用户名并存储它
import json
def 函数名():
    """问候用户，并指出名字"""
    文件名 = 'liname.json'   #尝试打开名为 liname.json的文件，如有则读取到内存当中，再执行下方的else语句
    try:
        with open(文件名) as 文件对象:
            用户名 = json.load(文件对象)
    # 用户首次运行上面部分的程序时，文件liname.json不存在将引发异常，为FileBotFoundError
    # 但是用Exception的意思是只要出错就执行下面的代码，让用户输入用户名，再用json,dumo存储用户名并打印
    except Exception:
        用户名 = input('请输入您的姓名：')
        with open(文件名,'w') as 文件对象:
            json.dump(用户名,文件对象)
            print(f'{用户名}下次回来我会记得你')

    else:
        print(f'{用户名}欢迎回来')
函数名()































