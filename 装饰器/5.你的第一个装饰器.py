# 前面回顾了函数的基本知识，现在开始学习装饰器的内容
# 上一个例子里，其实已经创建了一个装饰器，现在我们修改下上一个装饰器
# 来编写一个稍微更有用点的程序
"""
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after acecuting a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the funciton which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
# outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()
"""

"""
# 仔细研究上面的代码就会有点理解
# 现在讲代码改成用 @ 的形式
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after acecuting a_func()")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    # Hey you ! Decorate me !
    print("I am the funciton which needs some decoration to remove my foul smell")

a_function_requiring_decoration()

# the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)


# 学习上面的知识后，应该对装饰器有了了解。现在看看存在的一个问题
print(a_function_requiring_decoration.__name__)
# 会发现打印出的名字并不是原来的名字，而被 warpTheFunction 替代了。
"""
# 幸运的是，Python 提供了解决方案，如下所示：
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after acecuting a_func()")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you ! Decorate me !"""
    print("I am the funciton which needs some decoration to remove my foul smell")

print(a_function_requiring_decoration.__name__)


# 现在问题解决了，让我们看看装饰器的蓝本规范
from functools import wraps

def decorator_name(f):
    @wraps(f) # 用于解决原函数名字被抹去的情况
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run

# 注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
# 这可以让我们在装饰器里面访问在装饰之前的函数的属性。