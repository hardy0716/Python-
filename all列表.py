######
#   _all_  all列表
# 如果一个模块文件中有_all_变量，当使用from xxx import *导入时只能导入这个列表中的元素


__all__ = ['猴']

def 猴():
    print('齐天大圣-孙悟空')
def 猪():
    print('天蓬元帅-猪八戒')