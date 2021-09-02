# encoding:utf8
from flask import Flask

# __name__表示当前的模块名字
app=Flask(__name__,
          static_url_path='/python',# 访问静态资源的url前缀，默认是static
          static_folder='static', # 静态文件的目录，默认是static
          template_folder='templates',# 模板文件的目录，默认是templates
          )

# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile('static/config.cfg')
# 2.使用对象导入配置
class Config(object):
    DEBUG=True
# app.config.from_object(Config)
# 3.直接使用config的字典对象
app.config['DEBUG']=True

@app.route('/',methods=['GET','POST'])
def index():
    return 'hello'

if __name__=='__main__':
    app.run()