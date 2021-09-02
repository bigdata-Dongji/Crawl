from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import aliased
import os

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/student'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=False
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']=False
app.config['SQLALCHEMY_ECHO']=True
db=SQLAlchemy(app)

class course(db.Model):
    __tablename__='course'
    cid=db.Column(db.String(10),primary_key=True)
    cname=db.Column(db.String(10))
    tid=db.Column(db.String(10))

class student(db.Model):
    __tablename__='student'
    sid=db.Column(db.String(10),primary_key=True)
    sname=db.Column(db.String(10))
    sage=db.Column(db.DateTime)
    ssex=db.Column(db.String(10))

class sc(db.Model):
    __tablename__='sc'
    sid = db.Column(db.String(10),primary_key=True)
    cid = db.Column(db.String(10))
    score = db.Column(db.DECIMAL(18,1))

class teacher(db.Model):
    __tablename__='teacher'
    tid = db.Column(db.String(10),primary_key=True)
    tname = db.Column(db.String(10))



@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'

if __name__=='__main__':
    # app.run(debug=True,port='5000')
    s=aliased(sc) # 将sc表取别名为s
    #  1 查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数  1
    # result=sc.query.join(student,sc.sid==student.sid).join(s,sc.sid==s.sid).filter(sc.cid=='01',s.cid=='02',sc.score>s.score).all()
    # result=db.session.query(sc).join(student,sc.sid==student.sid).join(s,sc.sid==s.sid).filter(sc.cid=='01',s.cid=='02',sc.score>s.score).all()

    # result=db.session.query(sc).all()
    # # result=sc.query.all()
    # 1.1 查询同时存在" 01 "课程和" 02 "课程的情况  2
    result2=db.session.query(sc).join(s,sc.sid==s.sid).filter(sc.cid=='01',s.cid=='02')
    # 1.2 查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为 null )  3
    result3=db.session.query(sc).filter(sc.cid=='01').join(s,sc.sid==s.sid).filter(s.cid=='02').all()
    print(result3)
    for i in result3:
        print(i.sid)


    # sqlAlchemy使用sql语句执行
    cursor=db.session.execute("select * from (select * from sc where cid='01') a left join sc b on a.sid=b.sid and b.cid='02' ;")
    result_sql=cursor.fetchall()
    print(result_sql)

