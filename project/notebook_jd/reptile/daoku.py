import re
import pymysql

# 打开数据库连接
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root" , db="notebook")
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
#通过open（）方法以只读的方式打开文件，编码格式为UTF-8
file = open("京东笔记本电脑信息.txt", 'r', encoding='UTF-8')
#通过readlines（）方法读取文件的每一行赋值给lines
lines = file.readlines()
#如果lines为真，执行循环的内容
#对txt文件进行预处理操作
if lines:
    for line in lines:      #lines是一个列表，列表中的每隔元素就是txt文件中的一行数据 b
        line.replace('\n', '')
        r = '[\n’!"#$%&\'()[\\]]'
        data = re.sub(r, '', line)
        datas = data.split(', ')
        if len(datas) !=13:
            pass
        else:
            a = datas[0]
            b = int(datas[1])
            c = datas[2]
            d = float(datas[3])
            e = datas[4]
            f = datas[5]
            g = datas[6]
            h = datas[7]
            j = datas[8]
            k = datas[9]
            l = datas[10]
            m = datas[11]
            n = datas[12]
            print(a, b, c , d , e , f , g , h , j , k , l , m , n )
            sql = "insert into information values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  #数据库数据插入语句
            param = (a, b, c , d , e , f , g , h , j , k , l , m , n )                    #param参数是要输入的数据
            cursor.execute(sql, param)              #cursor.execute(sql,param)方法执行插入语句
#关闭连接
conn.commit()
file.close()
cursor.close()
conn.close()