from decimal import Decimal

import pymysql
import pandas as pd
conn=pymysql.connect(host="localhost", port=3306, user="root", passwd="root" , db="notebook")
cursor=conn.cursor()

def cursor_fet (sql):
    cursor.execute(sql)
    data = pd.DataFrame(list(cursor.fetchall()))
    return data

def te_1():
    sql = 'SELECT graphic,COUNT(graphic) FROM information GROUP BY graphic'
    data = cursor_fet(sql)
    name = list(data[0])
    value = list(data[1])
    return name,value

def te_2():
    sql = 'SELECT  t_name,price FROM information ORDER BY price DESC LIMIT 10'
    data = cursor_fet(sql)
    name = list(data[0])
    value = list(data[1])
    return name, value

def te_3():
    sql = "SELECT solid,count(solid) FROM information WHERE solid != '其他' GROUP BY solid "
    data = cursor_fet(sql)
    res = []
    for i in range(len(data)):
        result = {
            'name': list(data[0])[i],
            'value': list(data[1])[i]
        }
        res.append(result)
    return res

def te_4():
    dest = []
    sql1 ="SELECT t_name,Types_of,COUNT(Types_of) FROM information WHERE t_name ='联想（Lenovo）'AND Types_of !='其他' GROUP BY Types_of"
    sql2 ="SELECT t_name,Types_of,COUNT(Types_of) FROM information WHERE t_name ='戴尔（DELL）'AND Types_of !='其他' GROUP BY Types_of"
    sql3 ="SELECT t_name,Types_of,COUNT(Types_of) FROM information WHERE t_name ='华为（HUAWEI）'AND Types_of !='其他' GROUP BY Types_of "
    sql4 ="SELECT t_name,Types_of,COUNT(Types_of) FROM information WHERE t_name ='华硕（ASUS）'AND Types_of !='其他' GROUP BY Types_of "
    data = cursor_fet(sql1)
    data1 = cursor_fet(sql2)
    data2 = cursor_fet(sql3)
    data3 = cursor_fet(sql4)
    res = []
    res2 = []
    res3 = []
    res4 = []
    for i in range(len(data)):
        result = {
            'name': list(data[1])[i],
            'value': list(data[2])[i]
        }
        res.append(result)
    for i in range(len(data1)):
        result = {
            'name': list(data1[1])[i],
            'value': list(data1[2])[i]
        }
        res2.append(result)
    for i in range(len(data2)):
        result = {
            'name': list(data2[1])[i],
            'value': list(data2[2])[i]
        }
        res3.append(result)
    for i in range(len(data3)):
        result = {
            'name': list(data3[1])[i],
            'value': list(data3[2])[i]
        }
        res4.append(result)
    dest.append(res)
    dest.append(res2)
    dest.append(res3)
    dest.append(res4)
    return dest

def te_5():
    pue = []
    sql = 'SELECT graphic,COUNT(graphic) FROM information GROUP BY graphic ORDER BY COUNT(graphic) DESC LIMIT 5'
    sql1 = 'SELECT thickness,COUNT(thickness) FROM information GROUP BY t_name ORDER BY COUNT(thickness) DESC LIMIT 5'
    data = cursor_fet(sql)
    data1 = cursor_fet(sql1)
    pue.append(list(data[1]))
    pue.append(list(data1[1]))
    return  pue

def te_6():
    sql = 'SELECT t_name,SUM(xiaoliang) FROM information GROUP BY t_name ORDER BY SUM(xiaoliang) DESC LIMIT 20'
    data = cursor_fet(sql)
    name = list(data[0])
    value = list(data[1])
    return name, value

def te_7():
    sql = 'SELECT t_name,SUM(xiaoliang),CAST(SUM(hp) AS CHAR) FROM information GROUP BY t_name ORDER BY SUM(xiaoliang) DESC LIMIT 5'
    sql1 = 'SELECT t_name,SUM(xiaoliang),CAST(SUM(zp) AS CHAR) FROM information GROUP BY t_name ORDER BY SUM(xiaoliang) DESC LIMIT 5'
    sql2 = 'SELECT t_name,SUM(xiaoliang),CAST(SUM(cp) AS CHAR) FROM information GROUP BY t_name ORDER BY SUM(xiaoliang) DESC LIMIT 5'
    data = cursor_fet(sql)
    data1 = cursor_fet(sql1)
    data2 = cursor_fet(sql2)
    ptu = []
    res = []
    res1 = []
    res2 = []
    for i in range(len(data)):
        result = {
            'name': list(data[0])[i],
            'value': list(data[2])[i]
        }
        res.append(result)
    for i in range(len(data1)):
        result1 = {
            'name': list(data1[0])[i],
            'value': list(data1[2])[i]
        }
        res1.append(result1)
    for i in range(len(data2)):
        result2 = {
            'name': list(data2[0])[i],
            'value': list(data2[2])[i]
        }
        res2.append(result2)
    ptu .append(res)
    ptu.append(res1)
    ptu.append(res2)
    return ptu

def te_8():
    sql = 'SELECT t_name,SUM(xiaoliang*price) FROM information GROUP BY t_name ORDER BY SUM(xiaoliang*price) DESC LIMIT 10'
    data = cursor_fet(sql)
    name = list(data[0])
    value = list(data[1])
    return name, value

def te_9():
    sql = "SELECT t_name,graphic,COUNT(graphic) FROM information  WHERE t_name = '戴尔（DELL）' GROUP BY graphic"
    sql1 = "SELECT t_name,graphic,COUNT(graphic) FROM information  WHERE t_name = '联想（Lenovo）' GROUP BY graphic"
    data = cursor_fet(sql)
    data1 = cursor_fet(sql1)
    tpp = []
    res = []
    res1 = []
    for i in range(len(data)):
        result = {
            'name': list(data[1])[i],
            'value': list(data[2])[i]
        }
        res.append(result)
    for i in range(len(data1)):
        result1 = {
            'name': list(data1[1])[i],
            'value': list(data1[2])[i]
        }
        res1.append(result1)
    tpp.append(res)
    tpp.append(res1)
    return tpp




