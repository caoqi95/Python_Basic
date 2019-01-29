"""
学习内容来自：https://eastlakeside.gitbooks.io/interpy-zh/content/decorators/everything_is_object.html
"""

def hi(name="caoqi"):
    return "hi," + name

if __name__ == "__main__":
    #print(hi())

    # 其实可以将一个函数复制给一个变量，比如
    greet = hi
    # 这里没有使用小括号，因为我们并不是在调用 hi 函数
    # 而是在将它放在 greet 变量里面。可以尝试运行这个：
    print(greet())

    # 如果删掉 hi 函数，看看会发生什么
    del hi

    print(hi()) # Outputs: NameError


    print(greet()) # Outputs: "hi, caoqi"