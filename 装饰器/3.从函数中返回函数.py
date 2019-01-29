# 有时候并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来

def hi(name='caoqi'):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == 'caoqi':
        return greet
    else:
        return welcome


if __name__ == "__main__":
    a = hi()
    #print(a) # Outputs: <function hi.<locals>.greet at 0x00000284FD782598>

    # 上面展示了 a 指向 hi() 函数中的 greet() 函数
    # 现在看看下面这个：
    # print(a()) # Outputs: now you are in the greet() function

    # 为什么会出现这样的结果？因为当一对小括号在后面的时候，函数就会被执行；
    # 而如果没有小括号在后面的话，那这个函数就可以被到处传递，并且可以赋值给别的变量而不去执行它
    # 使用 hi()() 也与上面一样的结果
    print(hi()()) # Outputs: now you are in the greet() function