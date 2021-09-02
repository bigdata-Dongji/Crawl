'''
运行前除了安装flask模块，还需安装mysqlclient模块
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
app.secret_key=os.urandom(24)
# 设置数据库连接  语法：'数据库+驱动://用户名:密码@ip:端口/数据库名' 或 '数据库://用户名:密码@ip:端口/数据库名'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@127.0.0.1:3306/breach2020'
# 将其设置为True时，每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# 动态追踪  用于设置数据发生变更之后是否发送信号给应用
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO']=True
db=SQLAlchemy(app)
# 创建数据表
class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    rname=db.Column(db.String(50))
    # 非空设置是nullable=True

@app.route('/create')
def create():
    # 创建表
    db.create_all()
    print('create cuccess')
    return 'cuccess'
@app.route('/add')
def add():
    r=Role(rname='xiaoli')
    db.session.add(r)
    db.session.commit()
    return 'add cuccess'
@app.route('/update')
def update():
    r=Role.query.filter(Role.rname=='xiaoli').first()
    r.rname='jack'
    db.session.commit()
    return 'update success'
@app.route('/delete')
def delete():
    r=Role.query.filter(Role.rname=='jack').first()
    db.session.delete(r)
    db.session.commit()
    return 'del succuss'
@app.route('/show')
def show():
    rs=db.session.query(Role).filter(Role.rname=='jack').all()
    print(rs[0].rname)
    return rs[0].rname

if __name__ == '__main__':
    app.run(debug=True)