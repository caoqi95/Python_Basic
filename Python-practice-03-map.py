# 练习使用 map() 内置函数
# map(function_to_apply, list_of_inputs)


def square(items):

    print(list(map(lambda x: x**2, items)))


if __name__ == "__main__":

    items = [1, 2, 3, 4, 5]
    square(items)