---
title: 【阿修】Python学习笔记 - 廖雪峰教程
tags: [Ax,Python]
date: 2021-3-23 02:51:37
---

我是阿修，B站账号【阿修的修行】。

这是我的Python学习笔记，来和我一起刷廖雪峰Python教程吧。

这是比较难的部分，包括map、reduce、filter、sorted、返回函数和闭包、匿名函数、装饰器、偏函数、模块、面向对象编程等。

（2021年3月23日02:51:32）

## Python学习笔记和代码

https://www.liaoxuefeng.com/wiki/1016959663602400

基本是跟我的主页那篇文章一致的。

https://lucky-ax.gitee.io/ax-learning-python-liaoxuefeng/

https://lucky2018.github.io/ax-learning-python-liaoxuefeng/

<!--more-->

## map函数

接收的参数：函数、可迭代对象

将函数依次作用于序列的每个元素

返回：迭代器，注意，是迭代器

```python
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(r))
print(list(r))

# <class 'map'>
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

优点：更直观

```python
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
# 不使用map 不够直观
```

下面可以理解为map的实现，实际上就是把上面封装成函数my_map()

```python
def f(x):
    return x * x

def my_map(func,iter_obj):
    L = []
    for n in iter_obj:
        L.append(func(n))
    return L

r = my_map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(r))
print(list(r))

# <class 'list'>
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

下面一行表示什么功能，怎么用了这么多个函数，解释一下

```python
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
```

## map习题

利用`map()`函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：`['adam', 'LISA', 'barT']`，输出：`['Adam', 'Lisa', 'Bart']`：

```python
def normalize(name):
    return name[0].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
```

首位变大写，之后变小写就行了

看看有没有其他解法

```python
def normalize(s):
    sl = list(s)  # 首字母大写
    fs = sl[0].upper()  # 其余部分小写
    rl = sl[1:]
    for i in rl:
        i = i.lower()
        fs = fs+i
    return fs


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
```

其实没有必要逐个字符用lower方法，因为可以处理字符串。其次rl变量也没必要，因为只用了一次。

```python
def normalize(name):
    if name[0].islower():
        a = name[0].upper()
        return a + name[1:].lower()
    else:
        return name[0]+name[1:].lower()
```

没有必要判断，变量a也没啥必要定义。

## reduce函数

接收的参数，也是一个函数一个序列

先对序列开头的元素使用函数，拿到结果，再对结果和之后的元素使用函数，重复此步骤

需要导入

python 社区推荐写可读性好的代码，有更好的选择时不建议用reduce

所以 python 2 中内置的reduce 函数 移到了 functools模块中

效果等效于

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

用于加法，等于使用sum

```python
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))
# 25
print(sum([1, 3, 5, 7, 9]))
# 25
```

列表组合成整数

```python
from functools import reduce
def fn(x, y):
    return x * 10 + y

ret = reduce(fn, [1, 3, 5, 7, 9])
print(ret)
print(type(ret))
# 13579
# <class 'int'>
```

基于上面，字符串转换为整数，等于使用int强制转换

```python
from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

ret = reduce(fn, map(char2num,'13579'))
print(ret)
print(type(ret))
# 13579
# <class 'int'>
```

整理后

```python
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
```

使用lambda函数

```python
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
```

## reduce习题

Python提供的`sum()`函数可以接受一个list并求和，请编写一个`prod()`函数，可以接受一个list并利用`reduce()`求积：

```python
from functools import reduce

def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, [1, 3, 5, 7, 9])

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
```

当然，fn写在外面应该也是可以的，不过一般做题的时候只让提交一个函数，故写在函数内部，更符合题意。

直接改例子中的加法为乘法就行。

## 习题 map+reduce

利用`map`和`reduce`编写一个`str2float`函数，把字符串`'123.456'`转换成浮点数`123.456`：

```python
from functools import reduce

def str2float(s):
    return float(s)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
```

这样当然是不行的，题目的意思就是让你自己实现float函数

为什么测试代码中不是相等而是相减小于0.00001

只要根据上面的，字符串转换成整数，加上小数部分的处理就行

```python
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    s1,s2 = s.split('.')
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    f1 = reduce(fn, map(char2num, s1))
    f2 = reduce(fn, map(char2num, s2))/(10**len(s2))
    return f1 + f2

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
```

这个跟我的思路是类似的，不过是乘10的负数次方，以及使用了int函数强制转换和lambda表达式

```python
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    lister = s.split('.')
    # 字符串分割
    list1 = reduce(lambda x, y: x * 10 + y, map(int, lister[0]))
    # 为省事直接用int了
    list2 = reduce(lambda x, y: x * 10 + y, map(int, lister[1]))
    return list1 + list2 * (10 ** -len(lister[1]))
    # 有len(lister[1])位小数位，乘以10的负数次方

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
```

生成数字匹配字典的方式不错，小数点位置应该是从右边开始的，就是为了算小数位有多少

同时为了防止不是小数，用了try...except，很不错，但是其实做题不需要考虑这么周全

```python
from functools import reduce


def str2float(s):
    try:
        # str-->num
        def str2num(n):
            digits = {str(v): v for v in list(range(10))}  # 生成数字匹配字典
            n = digits[n]
            return n
        # str换算num值 上面两行可以合并

        def tran(x, y):
            return x*10+y
        
        L = list(s)
        if '.' in L:
            dot = len(L)-(L.index('.')+1)  # 小数点的位置
            '''
            print('dot=',dot,end=' ')
            print('len(L)=',len(L),end=' ')
            print('L.index(\'.\')=',L.index('.'))
            '''
            L.remove('.')
            print(L)
            num = reduce(tran, map(str2num, L))*(0.1**dot)

        else:
            print(L)
            num = reduce(tran, map(str2num, L))
        return num
    except ValueError:
        print('Enter the right Float-Str')


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

```

我修改了一下

```python
from functools import reduce

def str2float(s):
    def str2num(n):
        digits = {str(v): v for v in list(range(10))}
        return digits[n]

    def tran(x, y):
        return x*10+y

    L = list(s)
    if '.' in L:
        dot = len(L)-(L.index('.')+1)  # 小数点右边有几位
        print('小数位 dot=',dot)
        print('总长度 len(L)=',len(L))
        print('L.index(\'.\')=',L.index('.'))        
        L.remove('.')
        print(L)
        num = reduce(tran, map(str2num, L))*(0.1**dot)
    else:
        print(L)
        num = reduce(tran, map(str2num, L))
    return num


print(str2float('123.444444444456'))

```

思路没变，就是先看看小数点后面有几位，然后整个序列变为一个整数后添上小数点，还考虑了没有小数点的情况。假如不考虑异常情况(不是数字)，不考虑没有小数点的情况：

```python
from functools import reduce

def str2float(s):
    def str2num(n):
        digits = {str(v): v for v in list(range(10))}
        return digits[n]

    def tran(x, y):
        return x*10+y

    L = list(s)
    dot = len(L)-(L.index('.')+1)  # 小数点右边有几位     
    L.remove('.') # 这是一个原地操作
    num = reduce(tran, map(str2num, L))*(0.1**dot)

    return num


print(str2float('123.0'))
print(str2float('123.'))

```

另外一个答案

```python
# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):    
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    num = 0.0
    inde = s.index('.')
    zheng = s[:inde]
    small = s[inde+1:]
    i = len(zheng)-1
    for x in zheng:
        num += (digits[x] * (10 ** i))
        i -= 1
    i = -1
    for x in small:
        num += (digits[x] * (10**i))
        i -= 1
    return num

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
```

完全没用使用map和reduce，不符合练习的本意，import也没必要留了。

就是给出了一种常规方法，能实现功能，但题目的要求是练习相关知识点。

变量命名怪异，inde不常见，使用拼音zheng表示整数，small表示小数。略奇怪。

```python
# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    dec_list = s.split('.')
    dec_list[0] = reduce(lambda x, y: x * 10 + y, map(lambda x: dict[x], dec_list[0]))
    dec_list[1] = reduce(lambda x, y: x * 0.1 + y , list(map(lambda x: dict[x], dec_list[1]))[::-1])
    return dec_list[0] + dec_list[1] * 0.1
```

使用了较多知识点，匿名函数使行数略减。

```python
def str2float(s):
	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': None}
	divisor = pow(10, (len(s) - s.find('.') - 1))
	def fn(x, y):
		if y == None:
			return x
		else:
			return x * 10 + y
	def digital(c):
		return DIGITS[c]
	return reduce(fn, map(digital, s)) / divisor
print(str2float('123.456'))
```

表达略有不同而已，还判断了y，不过没啥必要。

```python
def str2float(s) :
    from functools import reduce         #调用reduce函数
    DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def char2num(s) :               #定义把数字字符元素转为数字元素的函数
            return DIGITS[s]
    i = s.find('.')            #找到'.'所在的索引位
    L1=reduce(lambda x,y:x*10+y,map(char2num,s[:i]))  #取'.'之前的元素计算
    L2=reduce(lambda x,y:x/10+y,map(char2num,s[:i:-1]))/10  #取'.'之后的元素计算
    return L1 + L2
```

我自己是想看到使用除法的，其实乘0.1或者10的负数次幂都一样。

此外，不建议import写在那个位置。

那里，不可以。

算了不玩梗了，只是个人建议，通常写在开头。

## filter函数

参数：还是一样，函数和序列。

作用：函数用于判断是否满足某种条件，返回True还是False，而 filter 只保留前者。

返回的是迭代器。用于print需要转换为其他类型。

```python
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 结果: [1, 5, 9, 15]
```

取模运算，返回的是True或者False，看看类型，转为列表

```python
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# 结果: ['A', 'B', 'C']
```

以上部分相当于

```python
def not_empty(s):
    if s:# 不为空不为None 则满足条件
        return s.strip()
    else:# 空或者None
        return s

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
```

if 的判断逻辑，后面的表达式不为空不为零不为None，则成立

```python
for s in [' A ', '', ' B ', None, 'C', '  ']:
    if s:
        print("s ***{}*** True".format(s))
    else:
        print("s ***{}*** False".format(s))
```

字符串strip方法

> Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
>
> **注意：**该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
>
> https://www.runoob.com/python3/python3-string-strip.html

and 运算的逻辑，x and y 相当于 if x is false, then x, else y

```python
# 判断变量是否为0， 是0则为False，非0判断为True
# and中含0，返回0
# 均为非0时，返回后一个值
2 and 0   # 返回0
2 and 1   # 返回1
1 and 2   # 返回2
# x and y 的值只可能是x或y. x为真就是y, x为假就是x
```

> https://blog.csdn.net/weixin_40041218/article/details/80868521
>
> Python 中 （&，|）和（and，or）之间的区别
>
> https://www.zhihu.com/question/20152384
>
> Python 里 and、or 的计算规则是怎样的？
>
> https://docs.python.org/zh-cn/3.8/library/stdtypes.html
>
> Python官方文档  x and y    if x is false, then x, else y



## 补充：短路逻辑

为什么输入为None的时候，s.strip() 会抛出异常，但是s and s.strip()不会。

and 运算的逻辑，x and y 相当于 if x is false, then x, else y。没有到y

and 的逻辑，只要前面不成立就直接返回False，后面表达式可以不合法。

即and语句左边不成立直接返回False，不再判断右边表达式。

```python
# 正常判断
age = 19
print(age > 18)
# 非法比较
age = '19'
print(age > 18)
# 单项判断
if age > 18:
    print("已经成年")
# 两个条件同时满足
if age > 18 and age < 22:
    print("你应该是大学生吧")
# 写错了 应该为or
if age < 0 and age > 100:
    print("写错了 不可能的")
# 只要满足一个条件
if age < 0 or age > 100:
    print("何方妖孽（请输入0~100的数）")
# 右边非法但是没关系
age = 19
if age < 0 and age < '100':
    print("age是19 不会输出这行的 age是负数 同样不会输出这行")
# 这样才会抛出异常
age = -19
if age < 0 and age < '100':
    print("age是19 不会输出这行的 age是负数 同样不会输出这行")
```





## 用filter求素数

第一步 奇数序列

```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
```

可以试着用用这个生成器函数

```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

c = _odd_iter()
for i in range(10):
    print(next(c))
```

注意正确的用法，不要写成：（每次都是新的生成器）

```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

for i in range(10):
    print(next(_odd_iter()))
```

第二步 筛选器 不能被n整除的才输出True

```python
def _not_divisible(n):
    return lambda x: x % n > 0
```

第三步 素数生成器

```python
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
```

注意中间 it 的类型是变了的

```python
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    print(type(it))
    while True:
        n = next(it)  # 返回序列的第一个数
        print(type(it))
        yield n
        it = filter(_not_divisible(n), it)
```

第四步 打印

```python
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

完整代码

```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n, end='  ')
    else:
        break

```

## filter习题

回数是指从左向右读和从右向左读都是一样的数，例如`12321`，`909`。请利用`filter()`筛选出回数：

```python
# -*- coding: utf-8 -*-

def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
```

变为字符串后，如果逆序仍然相等就返回True

解释一下[::-1]

切片复习 负数逆序 类似range

切片和索引中的-1 我们不一样

有没有-2 自己去试试咯

注意

```python
print('12345678'[::-1])#逆序输出
print('12345678'[-1:-100:-1])#越界了怕不怕，从右到左
print('12345678'[0:-1:-1])#开头到最后一个但是不包含最后一个，步长-1可以吗
print('12345678'[0:-1:1])#这就是从左到右但是不含最右，默认步长就是1
print('12345678'[::-2])#逆序切片而且步长是2
print('12345678'[::2])#顺序全都要，但是步长是2，拿一个杀一个
```

自己运行一下想想其中的道理吧

```python
from functools import reduce

def is_palindrome(n):
    return str(n)==reduce(lambda x,y:x+y,[str(n)[-1-unit] for unit in range(len(str(n)))])
```

略微复杂，要从右边开始看。

```python
def is_palindrome(nums):
    nums = int2list(nums)
    if len(nums) == 1:
        return True
    if len(nums) == 2 and nums[0] == nums[1]:
        return True
    # 三位以上 将list reverse 之后再做对比
    copy_nums = nums[:]
    copy_nums.reverse()
    return copy_nums == nums
```

没必要分别处理

评论区有个值得看看的问题，我就不讲了



## sorted函数

就是用来排序的，只不过可以自己定义排序的方式。

```python
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
```

相当于先取绝对值再计算

key接收的是函数，尝试使用自定义的函数

```python
def aaa(a):
    return a + a + a

print(sorted([36, 5, -12, 9, -21], key=aaa))
```

貌似没啥变化？

因为没有显示中间过程，显示的是排序后的结果，排序的对象是原来的序列，aaa只是排序的方式。

这种方式并不改变顺序

```python
def aa(a):
    return a*a

def aaa(a):
    return a**3

def fua(a):
    return -a

print("默认",sorted([36, 5, -12, 9, -21]))
print("立方",sorted([36, 5, -12, 9, -21], key=aaa))
print("平方",sorted([36, 5, -12, 9, -21], key=aa))
print("绝对值",sorted([36, 5, -12, 9, -21], key=abs))
print("取负",sorted([36, 5, -12, 9, -21], key=fua))
```

看这个你就懂了

此外，千万不要像我这样命名函数

用英语单词，不懂就查，还能学英语。这里举的是反例

平方 立方 取负数  不懂就问 问谁 搜索引擎

接下来是字符串的排序

```python
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
```

默认ASCII 大写和小写区分的

可以统一转换成全部大写或者全部小写

此外，字符串的排序是从头开始对比，相同则比较后一个字母



## sorted习题

假设我们用一组tuple表示学生名字和成绩：

```
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
```

请用`sorted()`对上述列表分别按名字排序：

```python
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

```

t[0]是指('Bob', 75），还是指'Bob'？

假如我写L而不是t呢？会不会混淆？

再按成绩从高到低排序：

```python
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
print(L2)
```

没必要非要用lambda表达式，也不符合题目要求

```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L, key = lambda x : x[0].lower())
L2 = sorted(L, key = lambda x : x[1], reverse = True)
print(L1)
print(L2)
```



## 返回函数和闭包

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

可变参数的求和函数，可以接收多个参数，忘记的复习前面函数的参数。

```python
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1,2,3))
print(calc_sum(1,2,3,4))
print(calc_sum(1,2,3,4,5))
print(calc_sum(1,2,3,4,5,6))
print(calc_sum(1,2,3,4,5,6,6,6,6))
```

如果不需要立刻求和，就返回求和函数，求和函数定义在内部。

相当于我让金秘书在我泡妞的时候帮我买花（函数），但我不确定什么时候会遇到妞（需要调用函数），但我又想现在先把钱交给金秘书（传递参数）。

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3)
print(f)
print(hex(id(f)))
print(type(f))
```

那么如何调用呢？调用函数加括号，调用函数的函数就加俩。

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum(1,2,3)())
print(type(lazy_sum(1,2,3)()))

f = lazy_sum(6,6,6)
result = f()
print(result)
```

加个括号就是了

调用 lazy_sum 的时候参数已经给了，但是结果还没算

需要再调用 lazy_sum 返回的结果（ f 函数）

> 在这个例子中，我们在函数`lazy_sum`中又定义了函数`sum`，并且，内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

注意，当我们调用 lazy_sum() 时，每次调用都会返回一个新的函数，即使传入相同的参数

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)
```

sum是内部函数，引用了外部的args，属于lazy_sum的局部变量。

注意，返回的函数没有被立即执行，直至被调用。

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
```

for循环里面 i 为 1,2,3 分别创建了一个新的函数，返回了3个。

返回的函数引用了变量 i ，但是并非立即执行，后面 i 变了，才调用执行 i*i。

```python
'''调用 count() 返回的是三个函数
这三个函数的返回值都是 i*i
但是执行计算的时候 i 已经不是原来的 i 了
i 意思是 我
我已经不是原来的我了'''
```

这个故事告诉我们，要保持初心。

啊呸，返回函数不要引用循环变量，不要引用会变化的变量。

不要追一个注定会变心的女人。

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
```

> 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变。

区别是append的时候，传入的东西是否还在乎被改变。前者相当于金秘书买花前，把她钱包掏空了。后者相当于金秘书接到命令，马上把钱给了花店老板，让老板接到电话马上把花送过来，就是参数已经再传给另一个函数了。

使用匿名函数。参考[闭包 - Python 之旅 - 极客学院Wiki]( https://wiki.jikexueyuan.com/project/explore-python/Functional/closure.html)

```python
def count():
    def f(j):
        g = lambda : j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
```



## 返回函数和闭包习题

利用闭包返回一个计数器函数，每次调用它返回递增整数：

```python
def createCounter():
    def counter():
        return 1
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# createCounter函数怎么改，才能在第一次调用的时候返回1，第二次调用的时候返回2，如此类推
```

首先是使用一个列表对象，列表的内存地址不变，内容是可修改的。

```python
def createCounter():
    c = [0]
    def counter():
        c[0] += 1            
        return c[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```

> 利用可变对象的这个特性有可能会引起变量作用域混乱的。
>
> Python闭包与nonlocal - 简书 https://www.jianshu.com/p/703ad1289a00

当然，还有办法，变成nonlocal就可以修改了，哪怕是整型变量。使用**nonlocal**的好处是，在为函数添加状态时不用额外地添加全局变量，因此可以大量地调用此函数并同时记录着多个函数状态，每个函数都是独立、独特的。也就是说，把变量当成一个全局变量来用。在本题中，如果不使用nonlocal，且c为int型变量，那么内层函数只能读取不能修改。

```python
def createCounter():
    c = 0
    def counter():
        c += 1            
        return c
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```

且看它报什么错：

```python
UnboundLocalError: local variable 'c' referenced before assignment
```

它是把c当成是一个内部函数的变量了，所以提示局部变量还没有定义就引用了。这里的理解是，内部函数的c相当于一个跟外部c没关系的变量，只是恰巧名字相同而已。就好比班主任教了好几个班，他知道他班里有一个“小明”，但是如果随便在一个班里面叫小明回答问题，那就有一定几率触发“查无此人”。

nonlocal就相当于班主任提前声明，“这是小明，也是我教的，不过不是咱们班，今天来咱们班上课”，那就可以在上课的时候叫小明回答问题了。

> 在Python 2.x中，闭包只能读外部函数的变量，而不能改写它。为了解决这个问题，Python 3.x引入了nonlocal关键字，在闭包内用nonlocal声明变量，就可以让解释器在外层函数中查找变量名。
>
> 注意：关键字nonlocal:是python3.X中出现的,所以在python2.x中无法直接使用。
>
> 一文读懂关键字nonlocal和global的用法与区别-Python学习网 https://www.py.cn/faq/python/11219.html

可以说，nonlocal是专门用在这种情况下的，专门为闭包开发，所以只要加在内层函数里面就好了。

> Python3中加入了新的关键字**nonlocal**,当在一个嵌套的函数中对变量申明为**nonlocal**时，就明确表示这个变量是外部函数中定义的变量。也许会有这么一个问题：按照python的LEGB原则，在函数本地作用域找不到变量的情况下，解释器会自动在外层函数寻找，**nonlocal**关键字岂不是显得多余？
>
> 是的，当一个函数在本地作用域找不到变量申明时会向外层函数寻找，这在函数闭包中很常见。
>
> 但是在本地作用域中使用的变量后，还想对此变量进行更改赋值就会报错。
>
> 加上关键字nonlocal申明就可解决这个问题。
>
> 当然，这也可以通过申明全局变量来实现增加函数状态的功能。当这样会出现以下问题：
>
> - 每次调用函数时，都得在全局作用域申明变量。别人调用函数时还得查看函数内部代码。
> - 当函数在多个地方被调用并且同时记录着很多状态时，会造成非常地混乱。
>
> 使用nonlocal的好处是，在为函数添加状态时不用额外地添加全局变量，因此可以大量地调用此函数并同时记录着多个函数状态，每个函数都是独立、独特的。针对此项功能其实还个一个方法，就是使用类，通过定义 **\_\_call\_\_** 可实现在一个实例上直接像函数一样调用。
>
> 为什么要使用nonlocal - 科幻vs现实 - 博客园 https://www.cnblogs.com/zhouyang123200/p/6538160.html

你也可以使用global，将变量声明为全局变量。不过那就要改测试代码了。

```python
def createCounter():
    global c
    c = 0
    def counter():
        global  c
        c += 1            
        return c
    return counter

# 测试:
c = 0
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```

区别是什么呢？

小明不属于我们班，但他属于我们班主任带的班。

global 声明的变量就不一样了，他甚至不属于我们学校，他是旦总安排的非洲交换生，是插班生，别的学校的交换生。

所以无论在内部函数还是外部函数，都要声明一下他是global的，global是“全球的”这个意思。在函数中，则是“全局的”，这个变量不属于函数，是函数外部的东西。如果不声明global，那就是函数内部自己使用的，哪怕名字一样，也不是同一个东西。

> 主要区别有以下两点：
>
> 1. 两者的功能不同。global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量，而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。
>
> 2. 两者使用的范围不同。global关键字可以用在任何地方，包括最上层函数中和嵌套函数中，即使之前未定义该变量，global修饰后也可以直接使用，而nonlocal关键字只能用于嵌套函数中，并且外层函数中定义了相应的局部变量，否则会发生错误。
>
> 一文读懂关键字nonlocal和global的用法与区别-Python学习网 https://www.py.cn/faq/python/11219.html

在评论区看到有使用循环的，都是闹着玩的。循环只进行了一次，就遇到了return或者break，那你干嘛要写while True。

> Python 闭包代码理解？ - 知乎 https://www.zhihu.com/question/31792789/answer/303653743
>
> 提一下这个的第一个答案，讲得不错

上面的1、4、9，如果调用的时候直接执行，结果就不一样了。

> Python 中通俗一点来说，如果在一个函数内部，嵌套了函数，这个内部函数对（非全局作用域）外部作用域的变量进行引用，那么这个内部函数称为闭包。闭包每次运行是能记住引用的外部作用域的变量的值。
>
> 黄哥漫谈Python 闭包。 - 知乎 https://zhuanlan.zhihu.com/p/21680710?refer=pythonpx

闭包有什么用呢？

记住了引用的外部变量的值，就是一个可以利用的点。

> - 闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
> - 闭包在运行时可以有多个实例，即使传入的参数相同。
> - 利用闭包，我们还可以模拟类的实例。
>
> 这里构造一个类，用于求一个点到另一个点的距离：
>
> ```python
> from math import sqrt
> 
> class Point(object):
>     def __init__(self, x, y):
>         self.x, self.y = x, y
> 
>     def get_distance(self, u, v):
>         distance = sqrt((self.x - u) ** 2 + (self.y - v) ** 2)
>         return distance
> 
> >>> pt = Point(7, 2)        # 创建一个点
> >>> pt.get_distance(10, 6)  # 求到另一个点的距离
> 5.0
> ```
>
> 用闭包来实现：
>
> ```python
> def point(x, y):
>     def get_distance(u, v):
>         return sqrt((x - u) ** 2 + (y - v) ** 2)
> 
>     return get_distance
> 
> >>> pt = point(7, 2)
> >>> pt(10, 6)
> 5.0
> ```
>
> 可以看到，结果是一样的，但使用闭包实现比使用类更加简洁。
>
> 闭包 - Python 之旅 - 极客学院Wiki https://wiki.jikexueyuan.com/project/explore-python/Functional/closure.html



[一步一步教你认识Python闭包 - FooFish-Python之禅](https://foofish.net/python-closure.html) 

[Python-闭包详解 - John_ABC - 博客园](https://www.cnblogs.com/JohnABC/p/4076855.html) 

[理解Python闭包概念 - alpha_panda - 博客园](https://www.cnblogs.com/yssjun/p/9887239.html) 

[深入浅出python闭包 - 知乎]( https://zhuanlan.zhihu.com/p/22229197) 这里举例说了闭包的作用、评论区也值得一看

[python中闭包详解 - HAPPYEVERYD - 博客园](https://www.cnblogs.com/s-1314-521/p/9763376.html) 

[Python闭包与nonlocal - 简书](https://www.jianshu.com/p/703ad1289a00)  题目多种解法，甚至有生成器加循环的

[为什么要使用nonlocal - 科幻vs现实 - 博客园](https://www.cnblogs.com/zhouyang123200/p/6538160.html) 

[Python学习：关键字global和nonlocal的用法说明](https://blog.csdn.net/qq_42780289/article/details/89244761) 



```python
# 内层再加def的思路。能否解决这个问题，好像不行，当然我也不敢说绝对
```

总结，首先应该明白变量的作用域这个概念。然后就是对闭包的机制有足够的了解。最后是熟悉Python的内部机制。

这个是三重境界。



## 匿名函数

有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

```python
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
```

等效的

```python
def f(x):
    return x * x

lambda x: x * x
```

限制：只能有一个表达式

好处：没有名字，不用担心函数命名冲突

可以赋值给变量，利用变量来调用函数，这又是何必呢

```python
f = lambda x: x * x
print(f(5))
```

可以把匿名函数作为返回值返回，注意这里其实是函数里面定义函数，意思是把上一节的闭包进行一定程度的简化，故lambda的冒号前无参数，如果忘记的，自己去看闭包那节。

```python
def build(x, y):
    return lambda: x * x + y * y
```

## 匿名函数习题

请用匿名函数改造下面的代码：

```python
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
```

so easy

```python
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
```

不写 == 1 也是可以的

```python
L = list(filter(lambda n: n % 2, range(1, 20)))
print(L)
```

相当于

```python
def is_odd(n):
    return n % 2

L = list(filter(is_odd, range(1, 20)))

print(L)
```

类似于

```python
def is_odd(n):
    if n % 2:
        return True
    else:
        return False

L = list(filter(is_odd, range(1, 20)))

print(L)
```

filter 和 if 都认这个逻辑，非零就是True

```python
def is_odd(n):
    if n % 2:
        return 1
    else:
        return 0

L = list(filter(is_odd, range(1, 20)))
print(L)
```

## 装饰器

函数可以赋值给一个变量，通过变量调用。以及怎样打印出函数的名字

```python
def now():
    print('2020年4月26日')

f = now
f()
now()

print(now.__name__)
print(f.__name__)
```

最后一行说明 f 其实就是 now 的一个别名而已。

```python
def log(func):
    def wrapper(*args, **kw):
        print('正在调用函数 %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2020年8月9日')

now()
# print(now.__name__)
```

wrapper 的w不发音，怎么读，应该很清楚了。没错，就是rapper。

看着函数套函数的样子，有没有感到一点熟悉。

没错，这就是闭包。闭包的应用，就有装饰器。内层函数显示了正在调用的函数的名字，顺便把参数原样传进去了。

相当于系统调用函数的时候，先调用了上面有个艾特符号的函数。也就是log函数，而且把函数名字now及其参数传进去了。

这时候，你以为是在调用now，其实是调用log，只不过log里面包含了now。

如果不使用@语法，就可以这么写：

```python
def log(func):
    def wrapper(*args, **kw):
        print('正在调用函数 %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def now():
    print('2020年8月9日')

function_without_at = log(now)
function_without_at()
# 这就是不使用@语法的装饰器 实际上就是闭包的应用
```

需要定义一个变量，还要把函数名传入装饰器，然后在这个变量后面加括号调用它。

@语法只是简化了这个过程，这就是Python的语法糖。

可以理解为：

```
now = log(now)
now()#新的now函数
```

如果装饰器本身需要参数，比如自定义log的文本，类似于 “正在启动函数：xxx” 这样的，那就需要再写一层函数：（例子中是execute）

```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')#这里有参数，ex怎么读，cute怎么读，大家心里有数
def now():
    print('2015-3-25')

now()
```

3层嵌套的效果：

```python
now = log('execute')(now)
now()
```

但是这样的话，如果最后打印now的名字的时候会有问题，因为根据倒数第三行的代码，new相当于最内层函数wrapper。打印的是wrapper的名字。	

```python
def log(text):
    def decorator(func):
        # print(func) # 不是指这里会出问题
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('正在执行')#这里有参数
def now():
    pass

# 以下三种情况等价

now()
print(now.__name__)

now = log('execute')(now)
now()
print(now.__name__)

new = log('execute')(now)
new()
print(new.__name__)
```

也就是说，装饰器内部打印名字不会有问题，外部的话，打印名字，问题大了。

所以需要一些特殊处理。

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

```python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

这样是为了严谨，安全。



## 装饰器习题

题目是做一个计时的装饰器：

```Python
# -*- coding: utf-8 -*-
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*arg,**kw):
        start_time = time.time()
        fn_tmp = fn(*arg,**kw)
        end_time = time.time()
        print('函数 %s 耗时 %s 秒' % (fn.__name__,end_time - start_time))
        return fn_tmp
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
```

其实测试代码有点问题，并不能检测装饰器是否工作，只要上面的wrapper那句包含return tmp这句就不会测试失败。

注意这个time.time()是有精度损失的，大概1毫秒。

```python
# -*- coding: utf-8 -*-
import time,random

def metric(fn):
    def wrapper(random_float):
        star_time = time.time()
        fn_tmp = fn(random_float)
        end_time = time.time()
        print("时间误差 %.5f " % (end_time - star_time - random_float))
        return fn_tmp
    return wrapper


@metric
def test(random_float):
    time.sleep(random_float)


for i in range(20):
    test(random.random())

# 测试时间误差，装饰器计时器统计结果和实际休眠时间相减
# 实际休眠时间是一个0到1之间的随机数

# 时间误差 0.00167 
# 时间误差 0.00057 
# 时间误差 0.00039 
# 时间误差 0.00148 
# 时间误差 0.00165 
# 时间误差 0.00184 
# 时间误差 0.00161 
# 时间误差 0.00128 
# 时间误差 0.00019 
# 时间误差 0.00128 
# 时间误差 0.00028 
# 时间误差 0.00082 
# 时间误差 0.00024 
# 时间误差 0.00059 
# 时间误差 0.00040 
# 时间误差 0.00052 
# 时间误差 0.00097 
# 时间误差 0.00135 
# 时间误差 0.00119 
# 时间误差 0.00093 
```

另一种统计方式，都控制在一毫秒以内，注意结果中的科学计数法，e-05表示前面的数字乘10的负5次方。这两种统计方式不一定准确，只是要告诉大家，大概有一毫秒的误差，仅此而已。

```python
import time

l = []
for i in range(20):
    t1 = time.time()
    time.sleep(0.01)
    t2 = time.time()
    l.append(t2-t1-0.01)

print(l)

# [0.000943174362182617, 0.0009739303588867185, 4.099845886230448e-05, 8.582115173339823e-05, 0.0009043121337890623, 0.0009703540802001951, 0.00014232635498046854, 3.742218017578104e-05, 0.0009858512878417967, 0.0001444721221923826, 4.672050476074198e-05, 1.0242462158202917e-05, 0.0009770298004150389, 0.0004496479034423826, 0.0009748840332031248, 0.0005993747711181639, 0.0009231472015380857, 0.00020336151123046854, 0.0006413364410400389, 2.192497253417948e-05]

# https://www.codenong.com/1938048/
# https://segmentfault.com/a/1190000012618603
```

log后面有无参数均可用的装饰器：

```python
import functools,time

def log(text=None):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)
        return wrapper

@log
def now():
    print("当前时间 ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

@log("启动")
def now2():
    print("当前时间 ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

now()
now2()

# 获取当前时间并按格式显示
# https://blog.csdn.net/qq_36478920/article/details/89468455
# https://www.runoob.com/python3/python3-date-time.html
```

你听我狡辩，不，你听我解释一下：

```python
import functools,time

def log(text=None):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)
        return wrapper

def now():
    print("当前时间 ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def now2():
    print("当前时间 ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


new = log(now)
new()
new2 = log('execute')(now)
new2()
log(now)()#和new是等价的
log('execute')(now)()#和new2是等价的


# 去掉语法糖@ 就很好懂了
# 主要是让函数log判断log之后的第一个参数的类型
# 到底是函数还是字符串
```

这种情况的if和else实际上是分别处理有参数和没有参数的情况。if和else中的逻辑大概可以合并一些，但是我暂时没有更好的写法了，就先这样吧。我一开始的解法，是log后面有括号但是参数数量不一定的，这就是没有看题目，做了下面这样的一个不正确的结果。不符合题目要求，题目要的是，连括号都没有：

```python
# 一种错误的解法 没有正确理解题意
def log(*text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (''.join(text), func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')# @log() 可以 但是 @log 不可以
def now():
    print('2020年8月11日')

now()
```

> 参考资料：
>
> 如何理解Python装饰器？ - 知乎 https://www.zhihu.com/question/26930016
>
> 理解Python装饰器(Decorator) - 简书 https://www.jianshu.com/p/ee82b941772a
>
> 一篇文章搞懂装饰器所有用法 - CoderEllison - 博客园 https://www.cnblogs.com/ellisonzhang/p/11196390.html

## 偏函数

先看例子，假如要把二进制字符转换为十进制数字：

```python
def int2(x, base=2):
    return int(x, base)
```

等价于

```python
import functools
int2 = functools.partial(int, base=2)
```

就是给int函数一个默认的参数，方便调用，而且可以覆盖。

偏函数还能够定住部分参数，比如计算最大值，默认都有10这个数：

```python
max2 = functools.partial(max, 10)
```

实际上会把10作为`*args`的一部分自动加到左边，也就是：

```python
max2(5, 6, 7)
```

相当于：

```
args = (10, 5, 6, 7)
max(*args)
```

结果为10。

```
import functools

max2 = functools.partial(max, 10)

def max3(*args,c=10):
    return max(*args,c)

print(max2(5, 6, 7))
print(max3(5, 6, 7))
```

假如是三个参数，想要固定第二个参数，那固定的参数之后的就要用等号赋值调用了。

比如三个数相加，某些时候第二个数是确定的，那么第三个参数就要用类似 c = 10 这样的方式调用。这部分其实是函数参数的知识，忘记的，自己去复习吧，函数的可变参数，关键字参数，默认参数，以及它们之间的优先级。

对于参数=固定的，固定参数往后的参数需要加上对应的变量名。

```python
def fun(a, b, c):    
    return a + b + c
    
f = functools.partial(fun, b = 2)

#则运算f的时候需要
f(1,c=3)
6
f(1)
#错误，未输入c
f(1,3)
f(1,2,3)
f(1,,3)
#错误，已经有一个固定的b值
#partial没有改变f中参数的位置
```

“当你固定的参数不是最后一个时”，修改“固定参数之后”的参数才需要加参数名。

例如：你固定的是a，那么你修改abc都需要加参数名；若你固定的是b，那么修改a就不用加参数名，修改b和c都需要参数名，以此类推……



参数的优先级，关键字参数要在可变参数后面。



## 模块

每个py文件就是一个模块

模块可以组合成一个包

每一个包必须包含一个 init 文件，被导入的时候自动导入并运行，init就是初始化的意思。

自己制作一个包试试，就叫做 lv 好了。



## 使用模块

导入



## 安装模块

pip安装



## Anaconda

自带了很多包，像LV啊，GUCCI啊，天津狗不理啊，这些，都没有。



## 面向对象编程

你的电脑就是你的对象，然后，编程的时候，你的脸要对着它，这就是面向对象编程。



## @property装饰器

1.可以检查参数，使用setter方法

```python
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

使用方式：

```python
s = Student()
s.set_score(60) # ok!
print(s.get_score())
# 60
s.set_score(9999)
#Traceback (most recent call last):
#  ...
#ValueError: score must between 0 ~ 100!
```

2.可以检查参数，而且使用简单

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

Python内置的@property装饰器就是负责把一个方法变成属性。

Python内置的@property装饰器就是负责把一个方法变成属性。

Python内置的@property装饰器就是负责把一个方法变成属性。

（重要的事情说3遍，一会再解释）（建议打在公屏上）

```python
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
# 60
s.score = 9999
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
```

所谓使用简单，其实是给score赋值只要用等号。

3.对比一下几种方式

回忆一下，最初我们是怎么使用的：

```python
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```

简化一下：

```python
class Student(object):
    pass

# 名字和属性都是后期动态绑定的
lisa = Student()
lisa.name = "Lisa"
lisa.score = 99
print(lisa.name)
print(lisa.score)
```

然后再看看上面有参数检查的两种方式（使用@property和不使用@property）的对比，只看赋值和查询部分（也就是get获取和set设置）：

```python
s = Student()
s.set_score(60) # ok!
print(s.get_score())
-----------------------------------------
# 设置和获取都是通过 函数
-----------------------------------------
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
-----------------------------------------
# 设置和获取都是通过 s.score
# 是不是很像动态绑定的写法，但是又有了参数检查
# 有效避免了s.score = 9999 或者 s.score = "amazing"
-----------------------------------------
```

4.@property具体作用

Python内置的@property装饰器就是负责把一个方法变成属性。

Python内置的@property装饰器就是负责把一个方法变成属性。

Python内置的@property装饰器就是负责把一个方法变成属性。

（还记得这段要求你们打在公屏上的内容吗？现在听我狡辩，啊，不，听我解释）

（我不听我不听我不听.gif）

百度搜@property，看知乎那个解释，排名在廖雪峰教程前面的。比较好懂。

[python @property的介绍与使用 - 知乎](https://zhuanlan.zhihu.com/p/64487092)

```python
class Suibian(object):

  @property
  def haha(self): ##含有@property
      return "hhhhhhhh红红火火恍恍惚惚"

  def hehe(self): ##不含@property
      return "呵呵"

sb = Suibian()
print(sb.haha) 
# 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
print(sb.hehe())  
#没有加@property , 必须使用正常的调用方法的形式，即在后面加()
```

加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。加了括号反而是错的，因为这就相当于已经获得返回值，再加了个括号，就会提示你，这个值不是一个可以被调用的函数。

> 学习资料
>
> 一个很不错的例子 逐渐演变的
>
> http://www.srcmini.com/2630.html
>
> property在python2和python3中的区别 - SegmentFault 思否 
>
> https://segmentfault.com/a/1190000019662994
>
> 官网搜@property
>
> https://docs.python.org/zh-cn/3.8/library/functions.html?highlight=property#property



## 多重继承

继承顺序

https://blog.csdn.net/qq_36346262/article/details/79299225

https://blog.csdn.net/weixin_40636692/article/details/79940501

https://www.jianshu.com/p/70af48457b6d

https://www.pythonf.cn/read/161149

mixin

https://blog.csdn.net/appleyuchi/article/details/105733270

https://blog.csdn.net/qq_25473157/article/details/87110464

https://www.jianshu.com/p/dae61c60f323

https://zhuanlan.zhihu.com/p/179265105

http://www.bjhee.com/python-mixin.html

网站那个例子，TCP 的运行不了，应该是 ForkingMixIn 的问题，猜测是因为 Windows 没有 fork 功能。

```python
from socketserver import TCPServer,ThreadingMixIn

class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


# https://blog.csdn.net/wowotouweizi/article/details/44085171
# from socketserver import TCPServer
# https://blog.csdn.net/caicaiatnbu/article/details/84873257
# https://www.v2ex.com/t/437625
```

