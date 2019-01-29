# 刚才的内容是函数的基本知识了。
# 其实，还可以在函数的内部定义函数

def hi(name='caoqi'):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "noe you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


if __name__ == "__main__":
    hi()

    # 上面展示了无论何时调用 hi(), greet() 和 welcome() 都将会被调用
    # 然而 greet() 和 welcome() 函数在 hi() 函数之外是不能访问的，比如：
    #greet() # Outputs: NameError
