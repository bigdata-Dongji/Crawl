# encoding:utf8
from flask import Flask,Blueprint

# 创建1个蓝图对象，蓝图就是一个小模块的抽象的概念
# 必须加入2个参数，第1个是蓝图的名字，第2个__name__是所在模块
app_blue=Blueprint('app_blue',__name__)


@app_blue.route('/blueprint_page')
def blueprint_page():
    return 'blueprint page'

