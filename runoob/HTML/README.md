## 菜鸟教程学习HTML
https://www.runoob.com/html/html-tutorial.html

参考资料 https://developer.mozilla.org/zh-CN/docs/Web/HTML



## 1.中文编码问题

```html
<meta charset="utf-8">
```

charset 属性规定在外部脚本文件中使用的字符编码。

如果外部文件中的字符编码与主文件中的编码方式不同，就要用到 charset 属性。

```
<head> 元素包含了文档的元（meta）数据，如 <meta charset="utf-8"> 定义网页编码格式为 utf-8。
```



## 2.什么是HTML？

HTML指的是超文本标记语言，Hyper Text Markup Language，不是编程语言而是标记语言。HTML使用标记标签来描述网页，一个HTML文档，也就是一个web页面，包含了HTML标签和文本内容。



## 3.最简单的HTML

基本上是每个网页的框架。

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>标题（显示在浏览器的标签栏）</title>
</head>

<body>
    <h1>我的第一个标题</h1>
    <p>我的第一个段落。</p>
</body>

</html>
```



## 4.HTML版本

不重要，基本上知道最早的HTML是1991年，HTML5是2012年就够了。



## 5.<!DOCTYPE> 声明

不区分大小写，以下均可。

```html
<!DOCTYPE html> 

<!DOCTYPE HTML> 

<!doctype html> 

<!Doctype Html>
```



## 6.适用的 VS Code 插件

想要右键使用浏览器打开，安装一个插件叫做 Open in browser

Emmet插件加快写代码速度，参考https://blog.csdn.net/qq_33744228/article/details/80910377

比如有Emmet只要写一个感叹号然后Tab，就会有：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```



## 7.常用标签

标题：h1到h6

```html
<h1>这是一个标题</h1>
<h2>这是一个标题</h2>
<h3>这是一个标题</h3>
```

段落：p和斜杠p。不要忘记结束标签，虽然大多数浏览器也能正确显示。未来的HTML版本不允许省略结束标签。

```html
<p>这是一个段落。</p>
<p>这是另外一个段落。</p>
浏览器会自动地在段落的前后添加空行。（</p> 是块级元素）
```

链接：

```html
<a href="https://www.baidu.com">这是一个链接</a>
```

图像：

```html
<img loading="lazy" src="/images/logo.png" width="258" height="39" />
<img loading="lazy" src="/images/logo.png" />
<img loading="lazy" src="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png" />

<img src="./images/logo.png" />
<img src="/images/logo.png" />
上面表示同级目录，下面表示所在磁盘根目录
```

HTML标签对大小写不敏感，但是推荐使用小写，未来（XHTML）会强制使用小写。



## 8.空元素

没有内容的 HTML 元素被称为空元素。空元素是在开始标签中关闭的。

```html
<br> 就是没有关闭标签的空元素（<br> 标签定义换行）。

在 XHTML、XML 以及未来版本的 HTML 中，所有元素都必须被关闭。

在开始标签中添加斜杠，比如 <br />，是关闭空元素的正确方法，HTML、XHTML 和 XML 都接受这种方式。

即使 <br> 在所有浏览器中都是有效的，但使用 <br /> 其实是更长远的保障。
```



## 9.HTML属性

以超链接标签为例，href是属性，写在开始标签中，通常以键值对形式出现（比如：name="value"），后面的中文是标签的元素。

```html
<a href="http://www.baidu.com">这是一个链接</a>
```

属性值应该始终被包括在引号内。

双引号是最常用的，不过使用单引号也没有问题。

在某些个别的情况下，比如属性值本身就含有双引号，那么您必须使用单引号（例如：name='John "ShotGun" Nelson'）。

属性和属性值对大小写不敏感。

不过，万维网联盟在其 HTML 4 推荐标准中推荐小写的属性/属性值。

而新版本的 (X)HTML 要求使用小写属性。

查看完整的HTML属性列表 https://www.runoob.com/tags/html-reference.html

常见的属性，class、id、style、title等。



## 10.HTML标题

浏览器会自动地在标题的前后添加空行。

请确保将 HTML 标题 标签只用于标题。不要仅仅是为了生成粗体或大号的文本而使用标题。

搜索引擎使用标题为您的网页的结构和内容编制索引。

因为用户可以通过标题来快速浏览您的网页，所以用标题来呈现文档结构是很重要的。

应该将 h1 用作主标题（最重要的），其后是 h2（次重要的），再其次是 h3，以此类推。



## 11.水平线

hr 元素可用于分隔内容。

```html
<hr> 标签在 HTML 页面中创建水平线。
```



## 12.注释

可以理解为左右的箭头，前面有个英文感叹号。

<--理解为左箭头，然后插一个感叹号。

-->可以理解为→。

这么想方便记忆。

```html
<!--这是一个注释，注释在浏览器中不会显示-->
```



## 12.折行

br标签产生一个新行。相当于Word文档编辑时候的回车。其实大家知不知道回车键为什么叫回车？有什么历史？

```html
HTML5中，<br><br/><br />三者的区别？
https://www.zhihu.com/question/21632236/answer/18824702

<br>是HTML写法。
<br/>是XHTML1.1的写法，也是XML写法。
<br />是XHTML为兼容HTML的写法，也是XML写法。
因为HTML5兼容XHTML写法，所以三种都可以使用，没有区别。
如果要省一到二个字节的文件大小，使用第一种。
如果要方便地转成XML而且也要省一个字节的文件大小，使用第二种。
如要要方便地转成XML而且要兼容老的浏览器，使用第三种。
因为HTML是SGML的子集，SGML允许标签没有结束标签，而换行符元素正好不需要内嵌元素，也就不需要结束标签。所以在HTML中，应该写成<br>。
因为XHTML是XML的子集，在XML中，标签必须要有结束标签。所以在XHTML中只写<br>是不符合语法的，必须写成<br></br>或简写成<br/>。
而在XHTML的发展过程中，要做到兼容旧的HTML浏览器。而旧的HTML浏览器不理解（错误理解）这两种写法，对于第一种写法，某些浏览器估计会理解成两个<br>标签（我没有资料证明这一点），对于第二种写法，某些浏览器会理解成一个叫"br/"的标签。所以在兼容HTML的XHTML中我们通常把它写成<br />，这样在HTML解析中会理解成有一个叫"/"的属性的"br"标签，在XML解析中仍然会理解成<br></br>的简写，达到了两全其美的效果。
```



## 13.文本格式化

加粗、斜体、上标、下标、em标签、strong强调、big和small、pre标签。

加粗是bold，用b标签

斜体是italic，用i标签  用strong标签强调好像是一样的效果

```html
<strong>和 <b> 的区别
https://www.cnblogs.com/webARM/p/4781948.html

    
<b> 粗体文本，<strong> 用于强调文本

首先，从语义上来说<b>是UI层面上的‘加粗’，而<strong>是语气上的强调。所以语义控的同学，要区别使用这两种标签。

其次，具体看看官方的解释，W3C上对于<b>标签有这样的一段提示：根据 HTML5 规范，在没有其他合适标签更合适时，才应该把 <b> 标签作为最后的选项。HTML5 规范声明：应该使用 <h1> - <h6> 来表示标题，使用 <em> 标签来表示强调的文本，应该使用 <strong> 标签来表示重要文本，应该使用 <mark> 标签来表示标注的/突出显示的文本。

您也能够使用 CSS "font-weight" 属性来设置粗体文本。

W3C上是这样来解释<strong>的：

<strong> 标签和 <em> 标签一样，用于强调文本，但它强调的程度更强一些。

由此可以看出，<b>是W3C预设的加粗式样，如果不想要专门写一个类(font-weight:bold;)，用<b>还是个不错的选择，如果想做语义上的强调<strong>和<em>更加的合适。
    
但是语义上一般的强调优先使用<em>，更重一些的语气应使用<strong>。应注意的是在大多数书的浏览器中将<strong>和<b>采用了相同的式样来解释但是这种式样不能保证所有浏览器的统一。因为<strong>是语气上的强调，至于浏览器是否将‘强调’和‘加粗’划等号，还是因浏览器而异。

如果很关心式样，还是建议用css来实现。
```

另一篇文章

```html
<b>和<strong>的真正区别在哪？ 
https://www.douban.com/group/topic/80619913/

如果你使用<b>标签的理由是为了强调，那么你只需要用strong标签把它替换即可，在表现上，b标签和strong标签都是对文字进行加粗，看不出区别，但在标签语义上来说，strong标签是具有强调作用，在seo方面更为良好。 

如果你不是为了强调，只为了表现加粗效果，那就用css来控制样式。如果是标题的加粗效果，就用h标签来代替，这些对SEO更有亲和力。
```



## 14.pre元素

```html
HTML <pre> 元素表示预定义格式文本。在该元素中的文本通常按照原文件中的编排，以等宽字体的形式展现出来，文本中的空白符（比如空格和换行符）都会显示出来。(紧跟在 <pre> 开始标签后的换行符也会被省略)

<pre> 标签的一个常见应用就是用来表示计算机的源代码。

可以导致段落断开的标签（例如标题、<p> 和 <address> 标签）绝不能包含在 <pre> 所定义的块里。尽管有些浏览器会把段落结束标签解释为简单地换行，但是这种行为在所有浏览器上并不都是一样的。

pre 元素中允许的文本可以包括物理样式和基于内容的样式变化，还有链接、图像和水平分隔线。当把其他标签（比如 <a> 标签）放到 <pre> 块中时，就像放在 HTML/XHTML 文档的其他部分中一样即可。
```



## 15.code标签

```html
<code> 标签用于表示计算机源代码或者其他机器可以阅读的文本内容。

软件代码的编写者已经习惯了编写源代码时文本表示的特殊样式。<code> 标签就是为他们设计的。
    
包含在该标签内的文本将用等宽、类似电传打字机样式的字体（Courier）显示出来，对于大多数程序员来说，这应该是十分熟悉的。

只应该在表示计算机程序源代码或者其他机器可以阅读的文本内容上使用 <code> 标签。虽然 <code> 标签通常只是把文本变成等宽字体，但它暗示着这段文本是源程序代码。将来的浏览器有可能会加入其他显示效果。例如，程序员的浏览器可能会寻找 <code> 片段，并执行某些额外的文本格式化处理，如循环和条件判断语句的特殊缩进等。

提示：如果只是希望使用等宽字体的效果，请使用 <tt> 标签。或者，如果想要在严格限制为等宽字体格式的文本中显示编程代码，请使用 <pre> 标签。
```



## 16.addr标签和acronym标签

```html
HTML5 中不支持 <acronym> 标签。请使用 <abbr> 标签代替。
```



## 17.文字方向

```html
<p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
```



## 18.块引用

```html
<q> 与 <blockquote> 的区别

<q> 标签在本质上与 <blockquote> 是一样的。不同之处在于它们的显示和应用。<q> 标签用于简短的行内引用。如果需要从周围内容分离出来比较长的部分（通常显示为缩进的块），请使用 <blockquote> 标签。
```



## 19.超链接

target属性可以设置在新窗口打开超链接

```html
<a href="https://www.baidu.com/" target="_blank">访问菜鸟教程!</a>
```

使用id可以定义一个锚点，然后用href的井号跳转过去，比如回到页面顶部。可以不是本页面。定位到一个长网页的某个部分。

```html
在HTML文档中插入ID:

<a id="tips">有用的提示部分</a>
在HTML文档中创建一个链接到"有用的提示部分(id="tips"）"：

<a href="#tips">访问有用的提示部分</a>
或者，从另一个页面创建一个链接到"有用的提示部分(id="tips"）"：

<a href="https://www.runoob.com/html/html-links.html#tips">
可以从别的页面访问有用的提示部分</a>

请始终将正斜杠添加到子文件夹。假如这样书写链接：href="https://www.runoob.com/html"，就会向服务器产生两次 HTTP 请求。这是因为服务器会添加正斜杠到这个地址，然后创建一个新的请求，就像这样：href="https://www.runoob.com/html/"。
```

点击图片跳转超链接的实现：

```html
<a href="//www.baidu.com/"><img src="这里是图片地址smiley.gif"></a>
<a href="//www.baidu.com/">原本是文字的，改成图片img标签就行</a>
```



## 20.head元素

base标签注意一下

link标签是一定要熟悉的，导入css文件的

```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

style标签可以直接添加样式

```html
<head>
    <style type="text/css">
        body {
            background-color: yellow
        }
        p {
            color: blue
        }
    </style>
</head>
```

meta标签是不显示的，主要给搜索引擎看



## 21.使用CSS

内联样式

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>内联样式</title>
</head>

<body style="background-color:black;">
    <h2 style="background-color:red;">这是一个标题</h2>
    <p style="background-color:green;">这是一个段落。</p>
</body>

</html>
```

内部样式表

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>使用CSS</title>
    <style type="text/css">
        h1 {
            color: red;
        }
        p {
            color: blue;
        }
    </style>
</head>

<body>
    <h1>这是一个标题</h1>
    <p>这是一个段落。</p>
</body>

</html>
```

外部引用

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>外部的CSS</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

<body>
    <h1>我使用了外部样式文件来格式化文本 </h1>
    <p>我也是!</p>
</body>

</html>
```

```html
CSS 可以通过以下方式添加到HTML中:

内联样式 - 在HTML元素中使用"style" 属性
内部样式表 - 在HTML文档头部 <head> 区域使用<style> 元素 来包含CSS
外部引用 - 使用外部 CSS 文件
```

最好的方式是通过外部引用CSS文件。



## 22.插入图像

参考代码

```html
<p>一个来自文件夹中的图像:</p>
<img src="/images/chrome.gif" alt="Google Chrome" width="33" height="32">
<p>一个来自菜鸟教程的图像:</p>
<img src="//www.runoob.com/images/logo.png" alt="runoob.com" width="336" height="69">

在 HTML 中，图像由<img> 标签定义。
<img> 是空标签，意思是说，它只包含属性，并且没有闭合标签。

alt 属性用来为图像定义一串预备的可替换的文本。

替换文本属性的值是用户定义的。

<img src="boat.gif" alt="Big Boat">
在浏览器无法载入图像时，替换文本属性告诉读者她们失去的信息。此时，浏览器将显示这个替代性的文本而不是图像。为页面上的图像都加上替换文本属性是个好习惯，这样有助于更好的显示信息，并且对于那些使用纯文本浏览器的人来说是非常有用的。


图像映射，一个图片的多个区域可以点击，跳转到不同的链接
<p>点击太阳或其他行星，注意变化：</p>
<img src="planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">
<map name="planetmap">
  <area shape="rect" coords="0,0,82,126" alt="Sun" href="sun.htm">
  <area shape="circle" coords="90,58,3" alt="Mercury" href="mercur.htm">
  <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
</map>
```



## 23.表格

```html
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>

<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

tr 表示表格的行

td 表示表格数据

th 表示表格的头

跨行跨列等等。。。



## 24.列表

```html
无序列表使用 <ul> 标签

<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>
    

有序列表也是一列项目，列表项目使用数字进行标记。 
有序列表始于 <ol> 标签。每个列表项始于 <li> 标签。

列表项使用数字来标记。

<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>
```

自定义列表略，列表编号使用圆圈、圆点、方形、数字、大小写字母、罗马数字等略。



## 25.区块

就是div和span的使用

都是没有明确含义的，只是为了方便处理。



## 26.表单

文本域、密码字段、单选按钮、复选框、提交按钮

```html
<form>
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>

<form>
Password: <input type="password" name="pwd">
</form>

<form>
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>

<form>
<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
<input type="checkbox" name="vehicle" value="Car">I have a car 
</form>

<form name="input" action="html_form_action.php" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
```



2020年12月4日17:48:57

笔记先做到这里

代码到单选按钮