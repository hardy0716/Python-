# a = '猪牛羊虫菜果'
# #break  终止循环
# for i in a:
#     if i == '虫':
#         print('这怎么有虫子，咦，真恶心，不吃了')
#         break
#     print(i)
# else:
#     print('程序正常结束')
#
# print('----------------------')
# #continue  退出本次循环，继续执行下一次循环
# for i in a:
#     if i == '虫':
#         print('这怎么有虫子，咦，真恶心')
#         continue
#     print(i)
# else:
#     print('程序正常结束')
#break 终止循环，循环并没有正常结束
#countinue退出本次循环，执行下一次循环，循环是可以正常结束的


# 公共操作
#enumerate( ) 用于将一个可遍历的数据对象（如列表，元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环中。
# 语法： enumerate( 可遍历的对象，start = 0 )
# 注意：start参数⽤用来设置遍历数据的下标的起始值，默认为0。
# a = ['孙悟空','猪八戒','沙和尚','白龙马','唐僧']
# for i in enumerate(a):
#     print(i)
# print('----------')
# for i in enumerate(a,1):
#     print(i)
#
# for i,j in enumerate(a,1):
#     print(f'下标是{i},对应的数据是{j}')

# 推导式
#创建一个由0-10组成的列表
a = []
print(a)
for i in range(0,11):
    a.append(i)
print(a)

#一、列表推导式
# 列表名 = [ 变量名 for 变量名 in range(0,11) ]
b = [i for i in range(0,11)]
print(b)

#创建[0,2,4,6,8,10]
#方法一： range步长的方式
c = [i for i in range(0,11,2)]
print(c)
#方法二： 带if的列表推导式
d = [i for i in range(0,11) if i%2 == 0]  #  %取余数
print(d)

#字典推导式 【作用:快速合并列表为字典或提取字典中目标数据】
#将两个列表快速合并成一个字典：
a = ['华为' , '小米' , '苹果','三星']
b = [520,520,14,28]
#字典名 = { 列表1[变量名]：列表2[变量名] for 变量名 in range(len(列表1)) }
dict = {a[i]:b[i] for i in range(len(a))}
print(dict)
#提取字典中的目标数据
a = {'华为': 520, '小米': 520, '苹果': 14,'三星': 24}
# 提取销售数量大于100台的字典数据
#新字典名 = { 键：值  for  键，值  in 字典名.items( ) if  值 > 100 }
b = {i:j for i,j in a.items() if j > 100}
print(b)

#四、集合推导式  【了解即可，不常用】
a = [2,2,3]
print(type(a))
b = {i ** 3 for i in a}
print(b)
print(type(b))




























