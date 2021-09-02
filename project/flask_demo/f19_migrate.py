
'''
migrate 迁移，方便数据库的维护
'''

from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/flask2020'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=False
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']=False
app.config['SQLALCHEMY_ECHO']=True
db=SQLAlchemy(app)

# 创建flask脚本管理工具对象
manager=Manager(app)
# 创建数据库迁移工具对象
Migrate(app,db)
# 向manager对象中添加数据库的操作命令
manager.add_command('db',MigrateCommand)


@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'

if __name__=='__main__':
    # app.run(debug=True,port='5000')
    manager.run()

    # 1终端输入初始化命令：python f19_migrate.py db init
    # 2然后终端输入生成迁移文件命令：python f19_migrate.py db migrate    需要备注信息可加上参数-m '备注内容'
    # 3最后终端输入升级版本文件命令：python f19_migrate.py db upgrade

    # 终端查看历史迁移版本记录命令：python f19_migrate.py db history
    # 终端降级（回退）迁移版本命令：python f19_migrate.py db downgrade '版本号'
