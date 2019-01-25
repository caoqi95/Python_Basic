# 练习使用 set 集，set 是一个非常好用的数据结构。
# 它与 list 相似，区别在于 set 不能包含重复的值


if __name__ == "__main__":

    # 检查列表中是都包含重复的元素

    # 第一种方法：使用 for 循环
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    """
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)

    print(duplicates)
    """
    # 第二种方法：使用 set 集合
    duplicates = set([x for x in some_list if some_list.count(x) > 1])
    print(duplicates)

    # 交集
    valid = set([1, 2, 3, 4, 6, 8])
    input_set = set([2, 4, 6])
    print("交集：", input_set.intersection(valid))

    # 差集
    print("差集：", input_set.difference(valid))