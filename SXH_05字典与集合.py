a = {'华为':520,'小米':520,'苹果':14,'三星':24}
# #增加和修改  字典序列名[键] = 值  存在则修改；不存在则新增
# a['华为'] = 521
# print(a)
# a['荣耀'] = 500
# print(a)
#
# #删数据
# #删除字典内数据语法：del字典序列名[键]
# del a['三星'] #只需要写键，它会把键和值一起删除
# print(a)
#
# #清空字典：clear( )     字典序列名.clear( )
# a.clear()
# print(a)
# #删除整个字典的语法：del 字典序列
# del a
# print(a)

#查字典
#查数据：注意只能用键查值，不能用值查键，因为键是唯一的，值可能是重复的
print(a['小米'])
# print(a['诺基亚']) #没有则报错

#（1）get( )  语法： 字典序列名.get(键，随便写)
#如果键存在，返回值。如果键不存在，返回默认值，默认值是你随便写的内容，如果省略了这个参数，返回None
# print(a.get('华为','不存在'))
# print(a.get('荣耀','不存在'))
# print(a.get('荣耀'))
#
# #(2）values( )  语法： 字典序列名.values( )         # 返回字典中所有的值
# print(a.values())
#
# #（3）items( )  语法：字典序列名.items( )            #可迭代对象（里面的数据是元组）,迭代就是重复反馈过程
# print(a.items())

###字典的循环遍历
# for i in a.keys():
#     print(i)
#
# for i in a.values():
#     print(i)
#
# for i in a.items():
#     print(i)
#
# for i,j in a.items():
#     print(f'{i}={j}')
#     print(type(i))
#     print(type(j))

# 集合
#创建集合：可以用{ } 或 set( )创建集合，但是创建空集合必需用set( )，因为{ }创建的是空字典
# b = {}
# print(type(b))
# c = {1,2}
# print(type(c))
# d = set()
# print(type(d))

#集合的特点： (1)自动去除重复数据  (2)顺序是随机的，所以不支持下标
# b = {1,2,2,3,4,5}
# print(b)  #结果为1，2，3，4，5
# c = {1,23,22,5,7,4}
# print(c)

#增加数据：
#集合名.add(数据)	# 因为集合自动去重复，所以增加重复内容时不进行任何操作
# b.add(4)
# print(b)
# b.add(6)
# print(b)

#追加数据序列：
#集合名.update(数据序列)        # 数据序列：列表，字符串，元组

# a = {1,2,3,4}
# a.update([5,6,7]) #列表
# print(a)
# a.update((8,9,10)) #元组
# print(a)
# a.update('abc')
# print(a)
# a.update('abc','de','孙兴华')
# print(a)

#删除数据：
#集合名.remove(数据)	   #  如果数据不存在，报错
#集合名.discard(数据)     # 如果数据不存在，不报错
# a = {1,2,3,4}
# # a.remove(5)
# a.discard(5)
# print(a)
#
# a.remove(1)
# print(a)
# a.discard(4)
# print(a)

#集合名.pop( )         # 随机删除集合中某个数据，并返回这个数据
# a = {1,2,3,4,5,6}
# a.pop()
# print(a)
# a.pop()
# print(a)

#查找数据
# in:  判断数据是否在集合序列中
# not in: 判断数据不在集合序列中
# print( 数据 in 集合名 )                          # 返回 True 或 False
# print( 数据 not in 集合名 )	 # 返回 True 或 False
a = {1,2,3,4,5,6}
print(1 in a)
print(8 in a)
print(8 not in a)

#第1课 我们学习3种类型转换    int( )   float( )   str( )
# 第3课，我们又学习2种类型转换
# list(序列名)     # 将序列转为列表
# tuple(序列名)  # 将序列转为元组
# 今天我们再学一个
# set(序列名)       # 将某个序列转换成集合
# 注意：集合自动去重复，但不支持下标，没有顺序
a = [1,2,3,4]
b = (5,6,7)
print(set(a))
print(set(b))









