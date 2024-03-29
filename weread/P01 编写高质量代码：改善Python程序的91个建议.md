## 编写高质量代码：改善Python程序的91个建议

https://weread.qq.com/web/reader/b4832100597d8eb481b4cd6

这本书主要还是 Python 2 的代码，不过思想是可以参考的。（2021年3月18日01:40:47）

书名：编写高质量代码改善Python程序的91个建议

作者：张颖，赖勇浩

出版社：机械工业出版社

出版时间：2014-06

ISBN：9787111467045

本书由北京华章图文信息有限公司授权上海阅文信息技术有限公司进行制作与发行



## 前言

首先需要注意的是，本书并不是入门级的语法介绍类的书籍，因此在阅读本书之前假定你已经掌握了最基础的Python语法。

本书分为8章，主要从编程惯用法、基础语法、库、设计模式、内部机制、开发工具、性能剖析与优化等方面解读如何编写高质量的Python程序。（2021年3月18日01:46:14）



## 第1章 引论

### 建议1：理解Pythonic概念

TimPeters的《The Zen of Python》（Python之禅）

Python的packaging/unpackaging机制，Pythonic的交换代码只需要一行：

```python
a, b = b, a
```

遍历一个容器，用 for in 更快。

打开文件，用 with 语句。

充分利用 Python 语法，但是不要过分使用奇技淫巧。

比如用 -1 的切片，就不如 reversed 直观。

%s 的使用，中间可以加入字典的 key ，变成 %(name)s 后面跟字典，当然，使用 str.format() 更加推荐，更加 Pythonic 。

（2021年3月18日02:04:02）



### 建议2：编写Pythonic代码

避免只用大小写来区分不同的对象。如a是一个数值类型变量，A是String类型，虽然在编码过程中很容易区分二者的含义，但这样做毫无益处，它不会给其他阅读代码的人带来多少便利。

避免使用容易引起混淆的名称。容易引起混淆的名称的使用情形包括：重复使用已经存在于上下文中的变量名来表示不同的类型；误用了内建名称来表示其他含义的名称而使之在当前命名空间被屏蔽；没有构建新的数据类型的情况下使用类似于element、list、dict等作为变量名；使用o（字母O小写的形式，容易与数值0混淆）、l（字母L小写的形式，容易与数值1混淆）等作为变量名。

不要害怕过长的变量名。为了使程序更容易理解和阅读，有的时候长变量名是必要的。不要为了少写几个字母而过分缩写。下例是一个用来保存用户信息的字典结构，变量名person_info比pi的可读性要强得多。

早年的Pythonista常用dict.has_key()方法来判断字典对象是否包含某个元素，但新版本的Python中提供了in操作符（支持多种容器类型）取代它。

接下来介绍风格检查程序PEP8。其实一开始PEP8是一篇关于Python编码风格的指南，它提出了保持代码一致性的细节要求。它至少包括了对代码布局、注释、命名规范等方面的要求，在代码中遵循这些原则，有利于编写Pythonic的代码。

PEP8不是唯一的编程规范，事实上，有些公司制定的编程规范也非常有参考意义，比如GooglePython Style Guide。同样，PEP8也不是唯一的风格检测程序，类似的应用还有Pychecker、Pylint、Pyflakes等。其中，Pychecker是Google Python Style Guide推荐的工具；Pylint因可以非常方便地通过编辑配置文件实现公司或团队的风格检测而受到许多人的青睐；Pyflakes则因为易于集成到vim中，所以使用的人也非常多。

（2021年3月18日02:13:49）



### 建议3：理解Python与C语言的不同之处

严格的缩进确实能让代码更加规范、整齐，可读性和可维护性都会更高。避免缩进带来的困扰的方法之一就是养成良好的习惯，统一缩进风格，不要混用Tab键和空格。

C语言中单引号（'）与双引号（"）有严格的区别，单引号代表一个字符，它实际对应于编译器所采用的字符集中的一个整数值。但在Python中，单引号与双引号没有明显区别，仅仅在输入字符串内容不同时，在使用上存在微小差异。

三元操作符是if...else的简写方法，语法形式为C ? X: Y，它表示当条件C为True的时候取值X，C为False的时候取值为Y。其简洁的表达形式一直很受欢迎。但在Python 2.5之前并不支持三元操作符。为此，人们想出了不少替代方式，但在特殊情形下存在一些问题，因此很多人对Python语言本身加入该特征也提出了不少建议，最终PEP308被接受，根据提议采用if...else...形式实现条件表达式。C ? X: Y在Python中等价的形式为X if C else Y。

Python中没有像C语言那样的switch...case分支语句，不过这不是什么难事，Python中有很多替代的解决方法。可以使用 if 和多个 elif 来实现，也可以使用跳转表，这个看不懂。

（2021年3月18日02:34:41）



### 建议4：在代码中适当添加注释

只要注释复杂操作和算法，有一定的空白提高可读性。

外部可访问的函数和方法，统统添加文档注释，描述功能、参数、返回值、可能发生的异常。

较为复杂的内部方法也需要进行注释。

推荐在文件头中包含copyright申明、模块描述等，如有必要，可以考虑加入作者信息以及变更记录。

避免注释与代码重复。注释应该是用来解释代码的功能、原因以及想法的，而不是对代码本身的解释。

（2021年3月18日02:40:43）



### 建议5：通过适当添加空行使代码布局更为优雅、合理

在一组代码表达完一个完整的思路之后，应该用空白行进行间隔。如每个函数之间，导入声明、变量赋值等。通俗点讲就是不要在一段代码中说明几件事。推荐在函数定义或者类定义之间空两行，在类定义与第一个方法之间，或者需要进行语义分割的地方空一行。

尽量保持上下文语义的易理解性。如当一个函数需要调用另一个函数的时候，尽量将它们放在一起，最好调用者在上，被调用者在下。

避免过长的代码行，每行最好不要超过80个字符。以每屏能够显示完整代码而不需要拖动滚动条为最佳，超过的部分可以用圆括号、方括号和花括号等进行行连接，并且保持行连接的元素垂直对齐。

不要为了保持水平对齐而使用多余的空格，其实使阅读者尽可能容易地理解代码所要表达的意义更重要。

空格的使用要能够在需要强调的时候警示读者，在疏松关系的实体间起到分隔作用，而在具有紧密关系的时候不要使用空格。

二元运算符（赋值（=），比较（==，<，>，!=，<>，<=，>=，in，not in，is，is not）、布尔运算（and，or，not））的左右两边应该有空格。逗号和分号前不要使用空格。

函数名和左括号之间、序列索引操作时序列名和[ ]之间不需要空格，函数的默认参数两侧不需要空格。

强调前面的操作符的时候使用空格。比如负2减5，减号要有空格，但是负号不要。

（2021年3月18日02:49:14）



### 建议6：编写函数的4个原则

原则1 函数设计要尽量短小，嵌套层次不宜过深。高度不要翻页，嵌套不要超过3层。

原则2 函数申明应该做到合理、简单、易于使用。参数如果太多，难理解，难测试。

原则3　函数参数设计应该考虑向下兼容。如果新增参数可以加默认参数，兼容旧代码。

原则4 一个函数只做一件事，尽量保证函数语句粒度的一致性。

Python中函数设计的好习惯还包括：不要在函数中定义可变对象作为默认值，使用异常替换返回错误，保证通过单元测试等。

（2021年3月20日21:14:44）



### 建议7：将常量集中到一个文件

在Python中应该如何使用常量呢？一般来说有以下两种方式：

通过命名风格来提醒使用者该变量代表的意义为常量，如常量名所有字母大写，用下划线连接各个单词，如MAX_OVERFLOW、TOTAL。然而这种方式并没有实现真正的常量，其对应的值仍然可以改变，这只是一种约定俗成的风格。

通过自定义的类实现常量功能。这要求符合“命名全部为大写”和“值一旦绑定便不可再修改”这两个条件。下面是一种较为常见的解决方法，它通过对常量对应的值进行修改时或者命名不符合规范时抛出异常来满足以上常量的两个条件。

专门搞一个类来放常量，绑定的常量名都是后期动态绑定的，而且要求必须是大写，而且不可以修改。（说实话，语法有点看不懂）

（2021年3月20日21:15:07）



## 第2章 编程惯用法

### 建议8：利用assert语句来发现问题

断言是有代价的，它会对性能产生一定的影响，对于编译型的语言，如C/C++，这也许并不那么重要，因为断言只在调试模式下启用。但Python并没有严格定义调试和发布模式之间的区别，通常禁用断言的方法是在运行脚本的时候加上-O标志，这种方式带来的影响是它并不优化字节码，而是忽略与断言相关的语句。

断言实际是被设计用来捕获用户所定义的约束的，而不是用来捕获程序本身错误的，因此使用断言需要注意以下几点：

1）不要滥用，这是使用断言最基本的原则。若由于断言引发了异常，通常代表程序中存在bug。因此断言应该使用在正常逻辑不可到达的地方或正常情况下总是为真的场合。

2）如果Python本身的异常能够处理就不要再使用断言。如对于类似于数组越界、类型不匹配、除数为0之类的错误，不建议使用断言来进行处理。

3）不要使用断言来检查用户的输入。如对于一个数字类型，如果根据用户的设计该值的范围应该是2～10，较好的做法是使用条件判断，并在不符合条件的时候输出错误提示信息。

4）在函数调用后，当需要确认返回值是否合理时可以使用断言。

5）当条件是业务逻辑继续下去的先决条件时可以使用断言。如list1和其副本list2，业务继续下去的条件是这两个list必须是一样的，但由于某些不可控因素，如使用了浅拷贝而list1中含有可变对象等，就可以使用断言来判断这两者的关系，如果不相等，则继续运行后面的程序意义不大。

（2021年3月20日21:19:54）



### 建议9：数据交换值的时候不推荐使用中间变量

直接使用 x, y = y, x 会更快，有解释，但我不是很理解。

> 一般情况下Python表达式的计算顺序是从左到右，但遇到表达式赋值的时候表达式右边的操作数先于左边的操作数计算，因此表达式expr3，expr4= expr1，expr2的计算顺序是expr1，expr2→expr3，expr4。因此对于表达式x，y=y，x，其在内存中执行的顺序如下：
>
> 1）先计算右边的表达式y，x，因此先在内存中创建元组（y，x），其标示符和值分别为y、x及其对应的值，其中y和x是在初始化时已经存在于内存中的对象。
>
> 2）计算表达式左边的值并进行赋值，元组被依次分配给左边的标示符，通过解压缩（unpacking），元组第一标识符（为y）分配给左边第一个元素（此时为x），元组第二个标识符（为x）分配给第二个元素（此时为y），从而达到x、y值交换的目的。

还有字节码（用 dis 模块）：

> 通过字节码可以看出，区别主要集中在swap1函数的第4行和swap2函数的第4～6行代码，其中swap1的第4行代码对应的字节码中有2个LOAD_FAST指令、2个STORE_FAST指令和1个ROT_TWO指令，而swap2函数对应的第4～6行代码中共生成了3个LOAD_FAST指令和3个STORE_FAST指令。而指令ROT_TWO的主要作用是交换两个栈的最顶层元素，它比执行一个LOAD_FAST+STORE_FAST指令更快。

（2021年3月20日21:26:06）



### 建议10：充分利用Lazy evaluation的特性

就是用好短路运算，减少计算量。

> 1）避免不必要的计算，带来性能上的提升。对于Python中的条件表达式if x and y，在x为false的情况下y表达式的值将不再计算。而对于if x or y，当x的值为true的时候将直接返回，不再计算y的值。因此编程中应该充分利用该特性。
>
> 在编程过程中，如果对于or条件表达式应该将值为真可能性较高的变量写在or的前面，而and则应该推后。

还有就是用好生成器，节省空间。

（2021年3月20日21:31:06）



### 建议11：理解枚举替代实现的缺陷

这部分是 Python 2 的内容，已经没啥意义了。

> Python3.4中根据PEP435的建议终于加入了枚举Enum，其实现主要参考实现flufl.enum，但两者之间还是存在一些差别，如flufl.enum允许枚举继承，而Enum仅在父类没有任何枚举成员的时候才允许继承等，读者可以仔细阅读PEP435了解更多详情。另外，如果要在Python3.4之前的版本中使用枚举Enum，可以安装Enum的向后兼容包enum34，下载地址为https://pypi.Python.org/pypi/enum34。

（2021年3月20日21:37:06）



### 建议12：不推荐使用type来进行类型检查

此处代码排版有问题，不是很想看。

大概是说，int 的子类，如果用 type() 判断，不是 int 类型。

> 由此可见基于内建类型扩展的用户自定义类型，type函数并不能准确返回结果。
>
> 在古典类中，任意类的实例的type()返回结果都是<type 'instance'>。这种情况下使用type()函数来确定两个变量类型是否相同显然结果会与我们所理解的大相径庭。

古典类，没搜到，搜到的是经典类和新式类，大概就是是否继承自 object 的区别，反正感觉意义不大。

> 因此对于内建的基本类型来说，也许使用type()进行类型检查问题不大，但在某些特殊场合type()方法并不可靠。那么究竟应怎样来约束用户的输入类型从而使之与我们期望的类型一致呢？答案是：如果类型有对应的工厂函数，可以使用工厂函数对类型做相应转换，如list(listing)、str(name)等，否则可以使用isinstance()函数来检测。

（2021年3月20日21:46:10）



### 建议13：尽量转换为浮点类型后再做除法

### 建议14：警惕eval()的安全漏洞

### 建议15：使用enumerate()获取序列迭代的索引和值

### 建议16：分清==与is的适用场景

### 建议17：考虑兼容性，尽可能使用Unicode

### 建议18：构建合理的包层次来管理module



## 第3章 基础语法

### 建议19：有节制地使用from...import语句

### 建议20：优先使用absolute import来导入模块

### 建议21：i+=1不等于++i

### 建议22：使用with自动关闭资源

### 建议23：使用else子句简化循环（异常处理）

### 建议24：遵循异常处理的几点基本原则

### 建议25：避免finally中可能发生的陷阱

### 建议26：深入理解None，正确判断对象是否为空

### 建议27：连接字符串应优先使用join而不是+

### 建议28：格式化字符串时尽量使用.format方式而不是%

### 建议29：区别对待可变对象和不可变对象

### 建议30：[]、()和{}：一致的容器初始化形式

### 建议31：记住函数传参既不是传值也不是传引用

### 建议32：警惕默认参数潜在的问题

### 建议33：慎用变长参数

### 建议34：深入理解str()和repr()的区别

### 建议35：分清staticmethod和classmethod的适用场景



## 第4章 库

### 建议36：掌握字符串的基本用法

### 建议37：按需选择sort()或者sorted()

### 建议38：使用copy模块深拷贝对象

### 建议39：使用Counter进行计数统计

### 建议40：深入掌握ConfigParser

### 建议41：使用argparse处理命令行参数

### 建议42：使用pandas处理大型CSV文件

### 建议43：一般情况使用ElementTree解析XML

### 建议44：理解模块pickle优劣

### 建议45：序列化的另一个不错的选择——JSON

### 建议46：使用traceback获取栈信息

### 建议47：使用logging记录日志信息

### 建议48：使用threading模块编写多线程程序

### 建议49：使用Queue使多线程编程更安全



## 第5章 设计模式

### 建议50：利用模块实现单例模式

### 建议51：用mixin模式让程序更加灵活

### 建议52：用发布订阅模式实现松耦合

### 建议53：用状态模式美化代码



## 第6章 内部机制

### 建议54：理解built-1n objects

### 建议55：__init__()不是构造方法

### 建议56：理解名字查找机制

### 建议57：为什么需要self参数

### 建议58：理解MRO与多继承

### 建议59：理解描述符机制

### 建议60：区别__getattr__()和__getattribute__()方法

### 建议61：使用更为安全的property

### 建议62：掌握metaclass

### 建议63：熟悉Python对象协议

### 建议64：利用操作符重载实现中缀语法

### 建议65：熟悉 Python 的迭代器协议

### 建议66：熟悉 Python 的生成器

### 建议67：基于生成器的协程及greenlet

### 建议68：理解GIL的局限性

### 建议69：对象的管理与垃圾回收

### 

## 第7章 使用工具辅助项目开发

### 建议70：从PyPI安装包

### 建议71：使用pip和yolk安装、管理包

### 建议72：做paster创建包

### 建议73：理解单元测试概念

### 建议74：为包编写单元测试

### 建议75：利用测试驱动开发提高代码的可测性

### 建议76：使用Pylint检查代码风格

### 建议77：进行高效的代码审查

### 建议78：将包发布到PyPI



## 第8章 性能剖析与优化

### 建议79：了解代码优化的基本原则

### 建议80：借助性能优化工具

### 建议81：利用cProfile定位性能瓶颈

### 建议82：使用memory_profiler 和 objgraph 剖析内存使用

### 建议83：努力降低算法复杂度

### 建议84：掌握循环优化的基本技巧

### 建议85：使用生成器提高效率

### 建议86：使用不同的数据结构优化性能

### 建议87：充分利用set的优势

### 建议88：使用multiprocessing克服GIL的缺陷

### 建议89：使用线程池提高效率

### 建议90：使用C/C++模块扩展提高性能

### 建议91：使用 Cython 编写扩展模块