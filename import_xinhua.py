import json,time,pymysql,pypinyin
file = open("word.json","r",encoding='utf-8')
content = file.read()
a = json.loads(content)
file.close()
db = pymysql.connect("localhost","root","123456","xinhua" )

for i in range(0,len(a)):
    try:
        no = int(i + 1)
        word = str(a[i]["word"])
        strokes = int(a[i]["strokes"])
        pinyin = str(a[i]["pinyin"])
        tmp = ''
        for z in pinyin:
            if z == 'ɡ':
                tmp += 'g'
            elif z == '0':
                pass
            elif z == '1':
                pass
            elif z == '发':
                break
            elif z == '亇':
                break
            else:
                tmp += z
        pinyin = tmp

        notone = ''
        for z in pinyin:
            if z in ['á', 'ā', 'à', 'ǎ']:
                notone += 'a'
            elif z in ['é', 'è', 'ě', 'ē']:
                notone += 'e'
            elif z in ['í', 'ì', 'ǐ', 'ī']:
                notone += 'i'
            elif z in ['ó', 'ò', 'ǒ', 'ō']:
                notone += 'o'
            elif z in ['ú', 'ù', 'ǔ', 'ū']:
                notone += 'u'
            elif z in ['ǘ', 'ǜ', 'ǚ', 'ü']:
                notone += 'v'
            elif z in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                notone += z
            else:
                print(pinyin)
                input_z = input(str("输入一个字母"))
                notone += input_z

        into_command = str(("insert into main values(%s,'%s',%s,'%s','%s',1)")%(no,word,strokes,pinyin,notone ))
        print(into_command)
        cursor = db.cursor()
        cursor.execute(into_command)
        db.commit()
    except Exception:
        db.rollback()
