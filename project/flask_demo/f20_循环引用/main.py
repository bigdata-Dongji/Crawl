# encoding:utf8
from flask import Flask
# 下面2行导入会报错。循环引用，解决办法：推迟一方的导入，让另一方先完成
from order import record
from goods import item

app=Flask(__name__)
# 函数定义后调用装饰器
app.route('/record')(record)
app.route('/item')(item)
@app.route('/',methods=['GET','POST'])
def index():
    # from order import record
    # from goods import item
    return 'hello'


if __name__=='__main__':

    app.run(debug=True,port='5000')