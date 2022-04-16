# #单继承
# class 小头爸爸(object):
#     def __init__(self):
#         self.age = 30
#
#     def 实例方法(self):
#         print(f'小头爸爸的年龄是{self.age}岁')
#
# #继承的概念：如果两个类存在父子级继承的关系，子类即便没有任何的属性和方法，
# # 那么用子类继承了某一个父类，并且此子类创建了一个对象，那么这个对象就拥有
# # 父类当中的所有属性和方法的使用权。
#
# class 大头儿子(小头爸爸):
#     pass
# 对象 = 大头儿子()
# 对象.实例方法()

#多继承
#就是一个类同时继承多个父类
# 注意： 继承多个类时  默认使用第一个类的属性和方法


# class 叶问(object):
#     def __init__(self):
#         self.功夫 = '咏春'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李小龙(object):
#     def __init__(self):
#         self.功夫 = '截拳道'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李中涛(叶问,李小龙):  #先继承括号一位置
#     pass
#
# 对象 = 李中涛()
# 对象.实例方法()



# mro顺序
# class 叶问(object):
#     def __init__(self):
#         self.功夫 = '咏春'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李小龙(叶问):
#     def __init__(self):
#         self.功夫 = '截拳道'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李中涛(李小龙):
#     pass
#
# 对象 = 李中涛()
# 对象.实例方法()
#
# print(李中涛.__mro__)




# 子类与父类具有相同的属性和方法

# class 叶问(object):
#     def __init__(self):
#         self.功夫 = '咏春'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李小龙(object):
#     def __init__(self):
#         self.功夫 = '截拳道'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李中涛(李小龙,叶问):
#     def __init__(self):
#         self.功夫 = '健身'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# 对象 = 李中涛()
# 对象.实例方法()


#子类调用父类同名方法和属性

# class 叶问(object):
#     def __init__(self):
#         self.功夫 = '咏春'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李小龙(object):
#     def __init__(self):
#         self.功夫 = '截拳道'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李中涛(李小龙,叶问):
#     def __init__(self):
#         self.功夫 = '健身'
#     def 实例方法(self):
#         self.__init__()     #将自己的实例方法初始化
#         print(f'使用{self.功夫}')
#
#     def 叶问_实例方法(self):
#         叶问.__init__(self)
#         叶问.实例方法(self)
#
#     def 李小龙_实例方法(self):
#         李小龙.__init__(self)
#         李小龙.实例方法(self)
#
# 对象 = 李中涛()
# 对象.实例方法()
# 对象.叶问_实例方法()
# 对象.李小龙_实例方法()

# 多层继承  #容易混乱 尽量不用

# class 叶问(object):
#     def __init__(self):
#         self.功夫 = '咏春'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李小龙(object):
#     def __init__(self):
#         self.功夫 = '截拳道'
#     def 实例方法(self):
#         print(f'使用{self.功夫}')
#
# class 李中涛(李小龙,叶问):
#     def __init__(self):
#         self.功夫 = '健身'
#         self.武器 = '屠龙刀'  #公有属性
#         self.__剑术 = '九阳神功'  #私有属性 不可继承
#     # 获取
#     def get_剑术(self):
#         return self.__剑术
#     # 修改
#     def set_剑术(self):
#         self.__剑术 = '葵花宝典'
#
#     # def 公有方法(self):
#     #     print('公有方法')   #可以继承
#     #
#     # def __私有方法(self):
#     #     print('私有方法')   #不可以继承
#
#     def 实例方法(self):
#         self.__init__()     #将自己的实例方法初始化
#         print(f'使用{self.功夫}')
#
#     def 叶问_实例方法(self):
#         叶问.__init__(self)
#         叶问.实例方法(self)
#
#     def 李小龙_实例方法(self):
#         李小龙.__init__(self)
#         李小龙.实例方法(self)
# class 大宝(李中涛):
#     pass
#
# 对象 = 大宝()
# 对象.实例方法()
# 对象.叶问_实例方法()
# 对象.李小龙_实例方法()
#
# #print(对象.武器)  #屠龙刀可以使用
# #print(对象.__剑术)  #找不到
#
# # 对象.公有方法()
# # 对象.__私有方法()
#
# 对象1 = 李中涛()
# 对象2 = 大宝()
# # 调用get_剑术函数  获取私有属性剑术值
# print(对象2.get_剑术())
#
# #调用 set_剑术函数 修改私有属性剑术值
# 对象2.set_剑术()
# #查看修改后的剑术值
# print(对象2.get_剑术())

#super
#使用super()可以自动查找父类。调用顺序遵循__mro__类属性的顺序。比较适合单继承使用。

class 叶问(object):
    def __init__(self):
        self.功夫 = '咏春'
    def 实例方法(self):
        print(f'使用{self.功夫}')

class 李小龙(叶问):
    def __init__(self):
        self.功夫 = '截拳道'
    def 实例方法(self):
        print(f'使用{self.功夫}')

        super().__init__()
        super().实例方法()

class 李中涛(李小龙):
    def __init__(self):
        self.功夫 = '健身'
    def 实例方法(self):
        self.__init__()
        print(f'使用{self.功夫}')
    def 叶问_实例方法(self):
        叶问.__init__(self)
        叶问.实例方法(self)
    def 李小龙_实例方法(self):
        李小龙.__init__(self)
        李小龙.实例方法(self)

    def 叶问和李小龙实例方法(self):
        super().__init__()
        super().实例方法()

对象 = 李中涛()
对象.叶问和李小龙实例方法()

#






































































