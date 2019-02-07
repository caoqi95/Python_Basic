# 学习 Python 容器模块

## 01-defaultdict

import collections

s = [('cao', 1), ('qi', 1), ('95', 2)]
d = collections.defaultdict(list)

for k, v in s:
    d[k].append(v)

print(d)

# defaultdict 可以用于字典的键嵌套赋值，如果一个键不存在的话，一般字典会报错，但是 defaultdict 不会

### 报错情况
some_dict = {}
#some_dict['colour']['favorite'] = 'yellow'

# 会报 KeyError：‘colour’

### 不报错的解决方法
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colour']['favorite'] = 'yellow'
## 打印结果
import json

print(json.dumps(some_dict))




## 02-counter
# Counter 是一个计数器，可以帮助我们针对某项数据进行计数
# 下面的例子是计算每个人喜欢多少种颜色

from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)

print(favs)

# 还可以用来统计一个文件：
""""
with open('filename', 'rb') as f:
    line_count = Counter(f)
    
print(line_count)
"""




## 03-deque
# deque 提供了一个双端队列，可以从头/尾两端添加或者删除元素

from collections import deque

# 创建一个 deque 对象
d = deque()

# 用法和 list 类似：
d.append('1')
d.append('2')
d.append('3')

print(len(d))
print(d[0])
print(d[-1])

# 从两端取数据
d = deque(range(5))
print(d)
print(len(d))
d.popleft() # 弹出 0
print(d)
d.pop()
print(d) # 弹出 4

# 也可以用 deque 来限制列表的大小，当超出限制时
# 数据会从队列另一端被挤出去(pop)

d = deque(maxlen=30)
for i in range(30):
    d.append(i)

print(len(d))
print(d)

d.append(31) # 超出范围限制
print(d)
print(len(d))




## 04-namedtuple
# 我们都知道元祖中的数据是不能修改的，而需要使用整数作为索引
# 才能获取元祖中的数据，如下所示：
man = ('Ali', 30)
print(man[0])

# 那 namedtuples 是什么？它把元祖变成一个针对简单任务的容器
# 不必再使用整数索引来访问一个 namedtuples 的数据，可以像字典一样访问
# 但是 namedtuple 是 不可变的

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)
print(perry.name)
print(perry.age)
print(perry.type)

"""
现在你可以看到，我们可以用名字来访问namedtuple中的数据。我们再继续分析它。一个命名元组(namedtuple)有两个必需的参数。它们是元组名称和字段名称。
在上面的例子中，我们的元组名称是Animal，字段名称是'name'，'age'和'type'。
namedtuple让你的元组变得自文档了。你只要看一眼就很容易理解代码是做什么的。
你也不必使用整数索引来访问一个命名元组，这让你的代码更易于维护。
而且，namedtuple的每个实例没有对象字典，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快。
然而，要记住它是一个元组，属性值在namedtuple中是不可变的，所以下面的代码不能工作：
perry.age = 42
"""
# namedtuple 也支持整数索引来取值
print(perry[0])

# namedtuple 还能转换成字典：
print(perry._asdict())





## 05-enum.Enum (Python 3.4+)
# enum 是枚举对象

from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2   # (译者注：幼小的狗狗)

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == tom.type) # True
print(charlie.type)

# 更详细的内容可以查看文档：
# https://docs.python.org/zh-cn/3/library/collections.html

## 06-enumerate 枚举
# 枚举会经常用到，下面是一个例子：
some_dict = {'cao':1, 'qi':2, '95':3}
for counter, value in enumerate(some_dict):
    print(counter, value)

# enumerate 还可以接收可选参数：
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# 可选参数可以允许我们定制从哪个数字开始枚举