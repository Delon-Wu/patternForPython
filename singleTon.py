# -*- coding = utf-8 -*-
# @Time: 2021/10/7 0007 16:46
# @Author: Delon
# @File: singleTon.py
# @software: PyCharm

# 单例设计模式
class SingleTon(object):
    spam = 1

    def __new__(cls):
        print(cls)
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTon, cls).__new__(cls)
        return cls.instance


s = SingleTon()
s1 = SingleTon()
print(s, s1)
