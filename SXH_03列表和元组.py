变量名 = ['孙行者','行者孙','者行孙','孙悟空']
print(变量名)
# print(变量名[0])
# print(变量名[1])
# print(变量名[2])
# print(f'{变量名[3]},我叫你一声你敢答应吗')
#
# #切片 变量名[开始位置下标:结束位置下标:步长]
# print(变量名[1:3:1])
# print(变量名[1:4:2])
# print(变量名[1::2])

#index  变量名.index(数据, 开始位置下标, 结束位置下标)       如果找不到报错
# print(变量名.index('唐僧'))
# print(变量名.index('孙悟空'))

# 4、count   统计指定数据在当前列表中出现的次数    语法：变量名.count(数据)
# print(变量名.count("孙悟空"))

# 5、len  返回列表长度。语法：len(变量名)
# print(len(变量名))

# 增
#1、变量名.append(数据)     列表结尾追加数据【追加单个数据】
# 变量名.append("白龙马")
# print(变量名)

# 2、变量名.extend(数据)      列表结尾追加数据【追加多个数据】
# 变量名.extend(["唐僧","沙和尚"])
# print(变量名)

# 3、变量名.insert(位置下标，数据)  在指定位置新增数据
# 变量名.insert(2,"猪八戒")
# print(变量名)

# 删 del
#1、del 变量名
# del 变量名
# print(变量名)

#2、del 变量名[下标]
# del 变量名[2]
# print(变量名)
# del 变量名[1]
# print(变量名)

#3、变量名.pop() #默认删除最后一个
# print(变量名.pop(1))
# print(变量名)

# # 4、变量名.remove(数据)          移除列表中某个数据的第一个匹配项
# 变量名.remove("孙悟空")
# print(变量名)
# # 5、变量名.clear( ) 	        清空列表，返回结果是 [ ]
# 变量名.clear()
# print(变量名)

# 1、修改指定下标的数据
# 变量名[1] = '孙悟空'
# print(变量名)
# 2、reverse( )  把整个列表倒序排列     语法：变量名.reverse( )
# 变量名.reverse()
# print(变量名)
#
# a = [1,3,5,9,6,2]
# print(a)
# a.reverse()
# print(a)
# 3、sort( ) 排序   语法：变量名.sort(reverse=False)  默认升序，降序改成True
# a = [1,3,5,9,6,2]
# print(a)
# a.sort(reverse=False)
# print(a)
#
# a = [1,3,5,9,6,2]
# print(a)
# a.sort(reverse=True)
# print(a)

# copy()  复制列表
# a = [1,3,5,9,6,2]
# a.sort(reverse=True)
# b = a.copy()
# print(b)


#三、遍历整个列表
# a  = ['孙悟空','猪八戒','沙和尚']
# for i in a:
#     print(i)
#四、列表嵌套 当一个列表中包含其它子列表时，如果查找指定人名？
# 变量名 =[ ['孙悟空','猪八戒','沙和尚'],['关羽','张飞','赵云'],['李小龙','叶问','霍元甲'] ] #找到李小龙
# print(变量名[2][0])

# 元组  小括号，不可更改
# a = (1,2,3)
# print(type(a))  #tuple 元组
# b = [1,2,3]
# print(type(b))  #list 列表
# c = (1)
# print(type(c))  #int 数值
# d = (1,)
# print(type(d))  #tuple 元组

#元组内数据直接修改会立即报错，不建议你去修改，如果想修改数据，请直接用列表。但是如果必需修改，可以利用切片和重新赋值的方式
# a = ('孙悟空','猪八戒','沙和尚','白龙马','孙悟空')
# #想把最后一个孙悟空删除，把唐僧加在二师兄和沙师弟之间
# b = a[0:2]+("唐僧",)+a[2:4]
# print(b)
# a = b
# print(a)

a = [1,2,3] #列表
b = (1,2,3) #元组
print(tuple(a))
print(list(b))




