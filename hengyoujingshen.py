# -*- coding: utf-8 -*-
#这个是针对“很有精神”名场面的特供版
#主要区别:word字符串使用readlines传参，而非单一字符串
import pypinyin,pymysql,random

#严格模式，真时会匹配音调相同的字，假时则不考虑音调（貌似没用）
strict = False

#生成次数，最小值为1，建议为1
user_want = 1

#笔画多不一定是生僻字，所以你可以限制查询的笔画最小值
#目前能让程序识别生僻字的方法只有引入字频库
#但大多数情况下，限制数为0也能找到生僻字，限制数太大反而找不到，如"啊"
strokes_length = 5

#作为偏处女的我不希望看到生成的结果含之前的字符
#真时程序会尽可能输出不同于之前字符串的字符
different = True

#变量初始化，勿动
user_strokes = strokes_length

if str(user_want).isdigit():
    if user_want <= 0:
        user_want = 1
    else: 
        pass
else:
    user_want = 1

db = pymysql.connect("localhost","root","114514","xinhua" )

#请在这里导入UTF-8编码的台词文件
#最好去掉回车符等干扰项
file = open("hengyoujingshen.txt","r",encoding='utf-8')

#主程序
for count in range(0,user_want):
    for line in file.readlines():
        output = ''
        word = str(line)
        for string in word:
            try:
                if strict:
                    value = str(pypinyin.pinyin(string)[0][0])
                    key = 'pinyin'
                else:
                    value = str(pypinyin.pinyin(string,heteronym=True,style=pypinyin.NORMAL)[0][0])
                    key = 'notone'
                if different:
                    while True:
                        search_command = str(("select * from main where %s = '%s' and strokes >= %s")%(key,value,strokes_length))
                        cursor = db.cursor()
                        data_exist = cursor.execute(search_command)
                        result = cursor.fetchall()
                        no = random.randint(0,len(result) - 1)            
                        db.commit()
                        if str(result[no][1]) == string:
                            if strokes_length == 0:
                                output += result[no][1]
                                break
                            else:
                                strokes_length -= 1
                                continue
                        else:
                            output += result[no][1]
                            break
                    user_strokes = strokes_length
                else:
                    search_command = str(("select * from main where %s = '%s' and strokes >= %s")%(key,value,strokes_length))
                    cursor = db.cursor()
                    data_exist = cursor.execute(search_command)
                    result = cursor.fetchall()
                    no = random.randint(0,len(result) - 1)            
                    db.commit()
                    output += result[no][1]
            except ValueError:
                output += string
        output = str(output).replace("\n", "").replace("\r", "")
        print(output)

file.close()
