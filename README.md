# String2ShengPiZi

之前在b站看到CSGO茄子发的[视频](https://www.bilibili.com/video/BV1zp4y1S7vr)：“真不错，住在山里真不错啊”，然后弹幕全是生僻字

虽然不知道他们怎么搞的，但是我这里用MySQL解决问题了

## 主程序

主程序分为zhenbucuo.py和hengyoujingshen.py,只在传参上有区别

均依靠数据库，否则不能运行

具体用法在主程序有注释

如果仍然不能理解可以通过B站私信/GitHub(如果可以)/邮箱通知我，我们会进行友♂好沟♂通并在下一次更新README

### zhenbucuo.py

这个主程序用户每次只能输入一段字符串，demo为“真不错，住在山里真不错啊”

### henyoujingshen.py

这个主程序通过readlines进行逐行传参，demo为《啊，海军》名场面

如果需要查看demo效果，请一同下载henyoujingshen.py

## 数据库

使用MySQL5.7.11，数据库为xinhua，表为main

数据库文件为main.csv

注意！表使用utf8mb4编码，而非utf8，使用其它编码方式可能会造成在导入生僻字时编码异常

main表结构如下：

  • no： 序号，类型为int，长度7，非NULL，主键

  • word： 汉字，类型为char，长度2，非NULL

  • strokes： 笔画，类型为int，长度3，非NULL

  • pinyin： 带注音的拼音，类型为text，非NULL

  • notone： 不带注音的拼音，类型为text，非NULL

  • from_xinhua： 标识符，类型为int，长度为1，非NULL，默认为0，目前0表示来自Unihan，1表示来自新华字典


## 开发

import_unihan.py通过简单读取文本向数据库写入数据

import_xinhua.py通过解析JSON向数据库写入数据

Unihan相关文件来自互联网，新华字典文件(word,json)来自[pwxcoo/chinese-xinhua](https://github.com/pwxcoo/chinese-xinhua)

## 存在的问题

首先，汉字存在多音字，出现多音字情况只会取第一种情况

另外，数据库存在一点问题，尤其是Unihan的，会出现个别字异常或对不上读音/笔画的情况

总之存在一些bug就对了:)
