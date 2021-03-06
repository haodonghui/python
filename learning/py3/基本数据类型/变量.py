"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，
    变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，
    我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
"""

a = 100  # 整型变量
b = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(a)
print(type(a))
print(b)
print(type(b))
print(name)
print(type(name))

'''
100
<class 'int'>
1000.0
<class 'float'>
runoob
<class 'str'>
'''
