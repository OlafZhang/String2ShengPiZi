# -*- coding: utf-8 -*-  
import pypinyin,pymysql,random

#严格模式，真时会匹配音调相同的字，假时则不考虑音调（貌似没用）
strict = False

#生成次数，最小值为1
user_want = 100

#笔画多不一定是生僻字，所以你可以限制查询的笔画最小值
#目前能让程序识别生僻字的方法只有引入字频库
#但大多数情况下，限制数为0也能找到生僻字，限制数太大反而找不到，如"啊"
strokes_length = 0

#作为偏处女的我不希望看到生成的结果含之前的字符
#真时程序会尽可能输出不同于之前字符串的字符
different = True

#在这里输入你想要转换的文本
#字符递归处理
#注意，如果遇到一些情况(pypinyin不能将一个字符识别为汉字例如标点符号)，会直接输出原字符
word = str("真不错,住在山里真不错啊")

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

#主程序
for count in range(0,user_want):
    output = ''
        
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
    print(output)
