# print('I\'m bigtom')
#
# a = '孙兴华'
# b = 20
# print(f'我的姓名是{a},我的年龄是{b}岁')
#
#
# b = int(input('请输入年龄：'))
# print(f'我的姓名是{a},我的年龄是{b}岁')

#1.下标
# 姓名 = '跟，着孙兴华学习python'
# print(姓名[3])
# print(姓名[8])
# print(姓名[10])

#2.切片
# 姓名 = '跟，着孙兴华学习python'
# print(姓名[3:6])
# print(姓名[3:6:1])
# print(姓名[3:6:2]) #步长
#
# print(姓名[:])
# print(姓名[::-1])
# print(姓名[::-2])
#
# print(姓名[-4:-1])

#3.字符串的常用操作方法（查找、修改、判断）
# 变量 = "只要地球不爆炸，我相信总有一天，全世界都说中国话！中国会成为世界的风向标！"
# print(变量.find("中国"))
# print(变量.find("中国",23,30))
#
# print(变量.find("美国")) #find找不到时返回 -1
# # print(变量.index("美国")) #index找不到时报错
# print(变量.count("中国"))
# print(变量.count("美国"))
# 变量 = "只要地球不爆炸，我相信总有一天，全世界都说中国话！中国会成为世界的风向标！"
# print(id(变量))
# print(变量.replace('中国','祖国'))
# print(id(变量.replace('中国','祖国')))

# 变量名 = "你好，世界！ ^ 你好，中国！ ^ 我们一起学习中国话！ ^ 中国加油！"
# print(变量名.split('^'))
# print(变量名.split('^',2))
# print(变量名.split(' '))
# print(变量名) #变量名并未改变

# 变量名 = ['中','国','最','强']
# print('_'.join(变量名))
# print('…'.join(变量名))
# print(''.join(变量名))
# print(变量名) #变量名并未改变

变量名 = "你好，世界，你好，中国，祝伟大的祖国繁荣昌盛"
print(变量名.startswith('你好')) #True
print(变量名.endswith('繁荣昌盛')) #True
print(变量名.startswith('你好',6,15)) #True
print(变量名.startswith('您好')) #False





















