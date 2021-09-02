# encoding:utf8
from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape
from flask_script import Manager  # 启动命令的管理类

app=Flask(__name__)
# 创建Manager管理类的对象
manager=Manager(app)

@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'

if __name__=='__main__':
    app.run()