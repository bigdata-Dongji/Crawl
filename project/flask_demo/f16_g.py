from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape,g
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    # g对象是应用上下文，用来不同函数传递参数，g对象每次进入这个函数会被清空,传递多个参数会比较方便
    g.name='tom'
    sayHello()
    return 'hello'

def sayHello():
    name=g.name
    print(name)

if __name__=='__main__':
    app.run(debug=True,port='5000')
