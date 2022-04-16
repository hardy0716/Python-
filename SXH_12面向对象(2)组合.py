class 叶问(object):
    def __init__(self,x):
        self.功夫 = x

class 李小龙(object):
    def __init__(self,x):
        self.功夫 = x

class 香港(object):
    def __init__(self,x,y):
        self.叶问 = 叶问(x)
        self.李小龙 = 李小龙(y)
    def 次数(self):
        print(f'在香港，叶问使用功夫{self.叶问.功夫}次，李小龙使用功夫{self.李小龙.功夫}次')
对象 = 香港(1,10)
对象.次数()











