# -*- coding: utf-8 -*-  

file = open("Unihan_IRGSources.txt","r",encoding='utf-8')

import pypinyin,pymysql

db = pymysql.connect("localhost","root","114514","xinhua" )

global temp
global output

no = 16142

for line in file.readlines():
    no += 1
    raw = line.split("	")
    unicode_raw = raw[0]
    if unicode_raw[0] == "U":
        if str(raw[1]) == 'kTotalStrokes':
            temp = ''
            output = ''
            strokes = int(raw[2])
            for i in unicode_raw:
                if i in ["A","B","C","D","E","F"]:
                    i = i.lower()
                elif i == "+":
                    continue
                elif i == "U":
                    continue
                else:
                    pass
                temp += i
                if len(temp) == 4:
                    break
                else:
                    pass
            exec((r"output = str('\u%s')")%(temp))
            notone = pypinyin.pinyin(output,style=pypinyin.NORMAL)[0][0]
            if str(notone[0]).islower():
                try:
                    pinyin = pypinyin.pinyin(output)[0][0]
                    into_command = str(("insert into main values(%s,'%s',%s,'%s','%s',0)")%(no,output,strokes,pinyin,notone ))
                    cursor = db.cursor()
                    cursor.execute(into_command)
                    db.commit()
                    print(into_command)
                except ValueError:
                    continue
                except:
                    db.rollback()
            else:
                pass
            
        
