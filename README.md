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

### hengyoujingshen.py

这个主程序通过readlines进行逐行传参，demo为《啊，海军》名场面

## 数据库

使用MySQL5.7.11，数据库为xinhua，表为main

注意！表使用utf8mb4编码，而非utf8，使用其它编码方式可能会造成在导入生僻字时编码异常

main表结构如下：

  · no
    序号，类型为int，长度7，非NULL，主键

  · no
    序号，类型为int，长度7，非NULL，主键


## 开发
