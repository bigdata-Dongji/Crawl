
'''
migrate Ǩ�ƣ��������ݿ��ά��
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

# ����flask�ű������߶���
manager=Manager(app)
# �������ݿ�Ǩ�ƹ��߶���
Migrate(app,db)
# ��manager������������ݿ�Ĳ�������
manager.add_command('db',MigrateCommand)


@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'

if __name__=='__main__':
    # app.run(debug=True,port='5000')
    manager.run()

    # 1�ն������ʼ�����python f19_migrate.py db init
    # 2Ȼ���ն���������Ǩ���ļ����python f19_migrate.py db migrate    ��Ҫ��ע��Ϣ�ɼ��ϲ���-m '��ע����'
    # 3����ն����������汾�ļ����python f19_migrate.py db upgrade

    # �ն˲鿴��ʷǨ�ư汾��¼���python f19_migrate.py db history
    # �ն˽��������ˣ�Ǩ�ư汾���python f19_migrate.py db downgrade '�汾��'
