## JavaScript学习笔记

ECMAScript 5.1 教程  https://wangdoc.com/javascript/

《ECMAScript 6入门》https://es6.ruanyifeng.com/

《ECMAScript 6入门》 https://wangdoc.com/es6/





## 导论 - JavaScript 教程 - 网道

https://wangdoc.com/javascript/basic/introduction.html

> 主要内容有四部分：
>
> - 基本语法
> - 标准库
> - 浏览器API
> - DOM

这部分内容主要基于 ECMAScript 5.1 版本。

> 为啥要学 JavaScript ？
>
> - 能操控浏览器
> - 使用领域广泛
>   - 浏览器平台化
>   - Node服务端
>   - 能操作数据库
>   - 移动平台开发
>   - 应用程序内嵌 JavaScript
>   - 跨平台桌面应用
> - 容易学
>   - 学习环境无处不在
>   - 语法简单
>   - 和主流语言相似
> - 强大的性能
>   - 语法灵活，表达力强（尤其适用异步编程）
>   - 支持编译运行
>     - 浏览器中，JavaScript 编译后运行，运行效率接近二进制程序
>     - WebAssembly 格式是二进制代码，运行速度快
>   - 事件驱动和非阻塞式设计
>     - 服务端适合高并发环境，普通硬件就可以承受很大的访问量
> - 开放性
>   - 标准的主要实现都是开放的，高质量的，不存在版权和专利问题
>   - 语言标准的制定委员会透明开放，公布会议记录
>   - 不同公司的 JavaScript 运行环境兼容性好
> - 社区支持和就业机会
>   - 社区极大，文献和代码丰富
>   - 找工作和招聘员工都不难

（2021年3月20日02:15:36）



## JavaScript 语言的历史 - JavaScript 教程 - 网道 

https://wangdoc.com/javascript/basic/history.html

浏览器需要一种可以嵌入网页的脚本语言，用来控制浏览器行为。比如验证表单，减轻服务器压力。

和 Java 的关系，不一样，但是存在练习，基本语法和对象体系模仿 Java 。

> 1995年5月，Brendan Eich 只用了10天，就设计完成了这种语言的第一版。它是一个大杂烩，语法有多个来源。
>
> - 基本语法：借鉴 C 语言和 Java 语言。
> - 数据结构：借鉴 Java 语言，包括将值分成原始值和对象两大类。
> - 函数的用法：借鉴 Scheme 语言和 Awk 语言，将函数当作第一等公民，并引入闭包。
> - 原型继承模型：借鉴 Self 语言（Smalltalk 的一种变种）。
> - 正则表达式：借鉴 Perl 语言。
> - 字符串和数组处理：借鉴 Python 语言。

周边大事：

> 1997年，DHTML（Dynamic HTML，动态 HTML）发布，允许动态改变网页内容。这标志着 DOM 模式（Document Object Model，文档对象模型）正式应用。
>
> 2005年，Ajax 方法（Asynchronous JavaScript and XML）正式诞生，Jesse James Garrett 发明了这个词汇。它开始流行的标志是，2月份发布的 Google Maps 项目大量采用该方法。它几乎成了新一代网站的标准做法，促成了 Web 2.0时代的来临。
>
> 2006年，jQuery 函数库诞生，作者为John Resig。jQuery 为操作网页 DOM 结构提供了非常强大易用的接口，成为了使用最广泛的函数库，并且让 JavaScript 语言的应用难度大大降低，推动了这种语言的流行。
>
> 2008年，V8 编译器诞生。这是 Google 公司为 Chrome 浏览器而开发的，它的特点是让 JavaScript 的运行变得非常快。它提高了 JavaScript 的性能，推动了语法的改进和标准化，改变外界对 JavaScript 的不佳印象。同时，V8 是开源的，任何人想要一种快速的嵌入式脚本语言，都可以采用 V8，这拓展了 JavaScript 的应用领域。
>
> 2009年，Node.js 项目诞生，创始人为 Ryan Dahl，它标志着 JavaScript 可以用于服务器端编程，从此网站的前端和后端可以使用同一种语言开发。并且，Node.js 可以承受很大的并发流量，使得开发某些互联网大规模的实时应用变得容易。
>
> 还有很多，比如各个浏览器内核引擎的来源、 React Native 等。

（2021年3月20日02:30:10）



## JavaScript 的基本语法 - JavaScript 教程 - 网道

https://wangdoc.com/javascript/basic/grammar.html

基本都会了，也就随便看看，复习一下。（2021年3月20日02:47:27）

### 语句

语句和表达式的区别，前者主要为了进行某种操作，一般情况下不需要返回值；后者则是为了得到返回值，一定会返回一个值。

分号的使用。

### 变量

变量是对“值”的具名引用。变量就是为“值”起名，然后引用这个名字，就等同于引用这个值。

JavaScript 的变量名区分大小写。

如果只是声明变量而没有赋值，则该变量的值是undefined。undefined是一个特殊的值，表示“无定义”。

不写var的做法，不利于表达意图，而且容易不知不觉地创建全局变量，所以建议总是使用var命令声明变量。

JavaScript 引擎的工作方式是，先解析代码，获取所有被声明的变量，然后再一行一行地运行。这造成的结果，就是所有的变量的声明语句，都会被提升到代码的头部，这就叫做变量提升（hoisting）。

### 标识符

标识符（identifier）指的是用来识别各种值的合法名称。最常见的标识符就是变量名，以及后面要提到的函数名。

JavaScript 语言的标识符对大小写敏感。

中文是合法的标识符，可以用作变量名。

### 注释

> JavaScript 提供两种注释的写法：一种是单行注释，用`//`起头；另一种是多行注释，放在`/*`和`*/`之间。
>
> 由于历史上 JavaScript 可以兼容 HTML 代码的注释，所以`<!--`和`-->`也被视为合法的单行注释。
>
> 需要注意的是，`-->`只有在行首，才会被当成单行注释，否则会当作正常的运算。

```javascript
x = 1; <!-- x = 2;
--> x = 3;

function countdown(n) {
  while (n --> 0) console.log(n);
}
countdown(3)
```

### 区块

在 JavaScript 语言中，单独使用区块并不常见，区块往往用来构成其他更复杂的语法结构，比如for、if、while、function等。

### 条件语句

if结构先判断一个表达式的布尔值，然后根据布尔值的真伪，执行不同的语句。所谓布尔值，指的是 JavaScript 的两个特殊值，true表示真，false表示伪。

需要注意的是，“布尔值”往往由一个条件表达式产生的，必须放在圆括号中，表示对表达式求值。

注意，if后面的表达式之中，不要混淆赋值表达式（=）、严格相等运算符（===）和相等运算符（==）。

多个if...else连在一起使用的时候，可以转为使用更方便的switch结构。需要注意的是，每个case代码块内部的break语句不能少，否则会接下去执行下一个case代码块，而不是跳出switch结构。

```javascript
switch (fruit) {
  case "banana":
    // ...
    break;
  case "apple":
    // ...
    break;
  default:
    // ...
}
```

switch语句后面的表达式，与case语句后面的表示式比较运行结果时，采用的是严格相等运算符（===），而不是相等运算符（==），这意味着比较时不会发生类型转换。

```javascript
(条件) ? 表达式1 : 表达式2
var msg = '数字' + n + '是' + (n % 2 === 0 ? '偶数' : '奇数');

var myVar;
console.log(
  myVar ?
  'myVar has a value' :
  'myVar does not have a value'
)
```

### 循环语句

while语句的循环条件是一个表达式，必须放在圆括号中。代码块部分，如果只有一条语句，可以省略大括号，否则就必须加上大括号。

for语句是循环命令的另一种形式，可以指定循环的起点、终点和终止条件。

do...while循环与while循环类似，唯一的区别就是先运行一次循环体，然后判断循环条件。while语句后面的分号注意不要省略。

break语句和continue语句都具有跳转作用，可以让代码不按既有的顺序执行。

break语句用于跳出代码块或循环。continue语句用于立即终止本轮循环，返回循环结构的头部，开始下一轮循环。

JavaScript 语言允许，语句的前面有标签（label），相当于定位符，用于跳转到程序的任意位置。标签可以是任意的标识符，但不能是保留字，语句部分可以是任意语句。标签通常与break语句和continue语句配合使用，跳出特定的循环。

```javascript
top:
  for (var i = 0; i < 3; i++){
    for (var j = 0; j < 3; j++){
      if (i === 1 && j === 1) break top;
      console.log('i=' + i + ', j=' + j);
    }
  }

foo: {
  console.log(1);
  break foo;
  console.log('本行不会输出');
}
console.log(2);

top:
  for (var i = 0; i < 3; i++){
    for (var j = 0; j < 3; j++){
      if (i === 1 && j === 1) continue top;
      console.log('i=' + i + ', j=' + j);
    }
  }
```

上面代码中，continue命令后面有一个标签名，满足条件时，会跳过当前循环，直接进入下一轮外层循环。如果continue语句后面不使用标签，则只能进入下一轮的内层循环。

（2021年3月20日02:53:00）

