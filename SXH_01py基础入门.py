print('你好，世界',end="\t") #输出 end=\n 系统默认 等于回车
# end=\t 即table 输出四个空格
print('你好，中国')

print("你好","中国",sep=" ") #sep=" " 默认
print("你好","中国",sep="-")

print("你好，世界"*3)
print("520"+"1314")
print(520+1314)

print("I love you")
print('I "Love" you')
print("I 'Love' you")

print(r"C:\abc\def\npd.xls") #推荐使用转义字符r

'''
1.学习
2.成功
3.信心
'''  #多行注释 '''  '''

# 1.学习
# 2.成果
# 3.信心  #ctrl+/ 多行注释

a,b,c=7,3,0
print(a)
print(b)
print(c)

a=b=c=2
print(a)

x = 5
y = 2
print(x)
print(y)
print('----')
x,y = y,x #交换变量赋值
print(x)
print(y)
print('----------')

姓名 = '李中涛'
年龄 = 20
print(f'我的名字是{姓名}，今年年龄是{年龄}')   #f格式化字符串
print(f'我的名字是{姓名}，明年年龄是{年龄+1}')

#五、输入  input
姓名 = input("请输入你的姓名：")
# 年龄 = input("请输入你的年龄：")
# print(f"你的姓名是{姓名}，你今年的年龄是{年龄}")

# print(f"你的姓名是{姓名}，明年的年龄是{年龄+1}") 报错 解决方法：把年龄转换为数值型（input默认是字符串）
年龄 = int(input("请输入你的年龄："))
print(f"你的姓名是{姓名}，明年的年龄是{年龄+1}")

#六、数据类型转换
# int() 转整数型； float()浮点型； str()字符串
#七、检查数据类型 type()
