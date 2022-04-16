#一、文件的三种操作

# 1、文件打开
#文件对象 = open('文件名','访问模式')
#访问模式
#① “r”只读：不存在将报错，不支持写   默认
#② “w"写入：如果不存在则新建，写入时覆盖原有内容
#③ ”a“追加：不存在将新建，写入时在原有内容上追加新内容

#访问模式的特点（‘b’二进制；'+'可读可写）

# r、rb、r+、rb+：只要文件不存在都报错，文件指针（光标的位置）放在文件开头
# w、wb、w+、wb+：只要文件不存在就新建文件，文件指针在开头，用新内容覆盖原内容
# a、ab、a+、ab+：只要文件不存在新建文件，文件指针在结尾



# 2、读写操作
# 文件对象.write('内容')

# a = open("1.txt","w")
# a.write("""aaaa
# bbbb
# cccc""")
# a.close()

# 文件对象.read(num)  #换行符占一个字节 end = \n
# a = open("1.txt","r")
# print(a.read())
# a.close()

#文件对象.readlines() #一次性读取所有内容 换行符也会读取
# a = open("1.txt","r")
# b = a.readlines()
# a.close()
# print(b)

#文件对象.readline()  #一次性读取一行内容
# a = open("1.txt","r")
# b = a.readline()
# c = a.readline()
# a.close()
# print(b)
# print(c)

# 3、关闭
#文件对象.close


#4、seek() 移动文件指针
#文件对象.seek(偏移量,起始位置)
# a = open('1.txt','r+')
# a.seek(2,0)
# print(a.read())
# a.close()

#5、文件备份
#1.输入目标文件： 文件名=input(‘请输入您要备份的文件名’)
#文件名 = input('请输入您要备份的文件名：')
#（2）规划备份文件的名字
# （2.1）提取后缀，找到名字中最右侧的点，名字和后缀分离
# 点的位置 = 文件名.rfind('.')
# 点的位置 = 文件名.rfind('.')
# # (2.2)组织新名字 = 原名字 + [备份] + 后缀
# if 点的位置 > 0:
#     后缀 = 文件名[点的位置:0]
# else:
#     print('文件名输入错误')
# 新名字 = 文件名[0:点的位置] + '[备份]' + 后缀
#
# 旧文件对象 = open(文件名,'rb')
# 新文件对象 = open(新名字,'wb')
#
# while True:
#     读取数据 = 旧文件对象.read(6)
#     if len(读取数据) == 0:  #读完了
#         break
#     新文件对象.write(读取数据)
# 旧文件对象.close()
# 新文件对象.close()



# 6、文件和文件夹操作
# （1）os模块：操作文件和文件夹
# import os    # 导入模块
# os.函数名( )  # 使用os模块相关功能
import  os

# （2）文件和文件夹重命名
# os.rename('旧文件名'，'新文件名')   # 目标文件名可以写路径，否则默认当前文件夹下面
# os.rename('旧文件夹名','新文件夹名')

#os.rename('1.txt','李中涛.txt')
# os.rename('空','孙兴华')

# （3）删除文件 （没有指定文件会报错）
# os.remove(目标文件名)  #不能删除文件夹

# os.remove('李中涛.txt')

# （4）创建文件夹 (重复创建相同名字的文件夹报错)
# os.mkdir(文件夹名字)

#os.mkdir('沙和尚')

# （5）删除文件夹 （没有指定文件夹报错）
# os.rmdir(文件夹名字)

#os.rmdir('孙兴华')

# （6）获取当前文件所在目录路径
# os.getcwd( )
# 例如：print(os.getcwd( ))

print(os.getcwd())

# （7）改变默认目录
# os.chdir(目录)
# 用于改变当前工作目录到指定的路径
# 例如：在当前文件夹aa目录下创建bb目录

# os.chdir('aa')
# os.mkdir('bb')


# （8）获取某个文件夹下所有文件和文件夹的名字，返回一个列表
# os.listdir(目录)
# 例如：print(os.listdir( ))   # 返回当前文件夹下
# 例如：print(os.listdir( '文件夹名' ))  # 返回指定文件夹下

print(os.listdir( ))
print(os.listdir('aa'))






































































