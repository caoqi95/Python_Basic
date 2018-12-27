"""
2018-12-08
练习列表和元祖
"""

# 列表方法
## 1. append
a = [1,2,3]
a.append(4)
print(a)

## 2. clear 就地清空列表
lst = [1,2,3]
lst.clear()
print(lst)

## 3. copy 复制列表
a = [1,2,3]
b = a # 这种常规做法会将 b 关联到列表
b[1] = 4
print(a) # 此时 a 为 [1,4,3]

a = [1,2,3]
b = a.copy()
b[1] = 4 # 此时只是修改了 b 列表的元素
print(a) # a 没被修改

## 4. count 计算指定的元素在列表中的出现的次数
lst = ['to', 'be', 'or','not','to','be']
print(lst.count('to'))

## 5. exend 同时将多个值扩展到列表中
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

## 6. index 在列表中查找指定值第一次出现的索引
x = [2,3,4,5,1,67,8,9,1]
print(x.index(1))

## 7. insert 用于将一个对象插入列表
n = [1,2,3,4,5]
n.insert(2, 2)
print(n)

## 8. pop 从列表中删除一个元素（末尾为最后一个元素），并返回这一元素
x = [1,2,3]
x.pop()
print(x)

## 9. remove 用于删除第一个为指定值的元素
x = ['i', 'love', 'you']
x.remove('love')
print(x)

## 10. reverse 按反方向顺序排列列表中的元素
a = [1,2,3]
a.reverse()
print(a)

## 11. sort 用于对列表就地排序
a = [2,3,7,5,9,1,0]
a.sort()
print(a)