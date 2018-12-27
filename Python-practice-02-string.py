"""
2018-12-27
练习字符串
"""

# 01 字符串的基本操作
# 字符串除了元素赋值和切片赋值外，其他索引，切片，长度，最大值，最小值都适用于字符串
website = "http:/www.python.org"
#website[-3] = "com" # 此处会报错，所以注释掉


# 02 设置字符串的格式：精简版
# 百分号的左边是字符串的格式，右边是格式的值；指定值得时候，可以使用元祖，也可以使用字典
# %s 称为转换说明符，s 表示输出为字符串。%.3f 表示输出为 3 位浮点数
format = "Hello, %s. %s enought for ya?"
values = ('world', 'Hot')
print(format % values)

print("{}, {}, {}".format('first', 'second', 'third'))

# 命名字段的工作原理
from math import pi
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))


# 03 字符串的方法

### 1）center 方法通过在两边添加填充字符（默认为空格) 来让字符串居中
s = "The Middel building is an office building"
print(s)
print(s.center(60))

### 2）find 方法在字符串中查找子字符串，如果找到就返回第一个字符的索引
s = "The Middel building is an office building".find("The")
print(s)

### 3）join 方法是一个非常重要的方法，与 split 方法相反，用于合并序列元素，所合并的元素必须为字符串
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

### 4）lower 方法返回字符串的小写版本
s = "CHINA"
print(s)
print(s.lower())

### 5) replace 方法将指定字串都替换成另一个字符串，并返回替换后的结果
s = "Hello, world".replace("world", "Python")
print(s)

### 6) split 方法用于将字符串拆分为序列，与 join 方法相反。
s = '1+2+3+4+5'
print(s.split('+'))

### 7) strip 方法用于将字符串开头或者结尾的空白删除（不包括中间的空白）
s = "                      Hi            "
print(s)
print(s.strip())

### 8) translate 方法和 replace 一样替换字符串的特定部分，但不同的是只能进行单字符替换
# 该方法的优势在于能够同时替换多个字符，因此效率比 replace 高
# 然而使用 translate 之前需要建立转换表
table = str.maketrans('cs', 'kz')
print("trans table: %s" % table)
s = 'This is an incredible test'
print(s)
print(s.translate(table))
