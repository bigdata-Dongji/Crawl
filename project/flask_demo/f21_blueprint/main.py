# encoding:utf8
from flask import Flask
from blue import app_blue
app=Flask(__name__)

# 注册蓝图
# app.register_blueprint(app_blue)
# 注册蓝图并添加前缀
app.register_blueprint(app_blue,url_prefix='/blue')

@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'

if __name__=='__main__':
    print(app.url_map)
    app.run(debug=True,port='5000')