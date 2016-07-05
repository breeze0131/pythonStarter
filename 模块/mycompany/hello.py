#!/usr/bin/env python3


' a test module '
__author__ = 'mm'
import sys

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
def test():
    args = sys.argv
    print(len(args))


if (__name__ == '__main__'):
    test()


# 作用域 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
