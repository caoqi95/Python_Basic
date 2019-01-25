# 练习使用 reduce() 内置函数
# 当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数, 避免使用了 for 循环
# reduce(function, sequence)

from functools import reduce


def all_product(nums):

    res = reduce(lambda x, y: x * y, nums)

    return res


if __name__ == "__main__":

    nums = [1, 2, 3, 4]
    res = all_product(nums)
    print(res)


