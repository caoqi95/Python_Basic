# 练习使用 filter() 内置函数
# filter(function, iterable)


def filter_nums(nums):

    res = list(filter(lambda x: x >= 0, nums))

    return res


if __name__ == "__main__":

    nums = list(range(-5, 5))
    print("before filter:", nums)
    res = filter_nums(nums)
    print("after filter:", res)