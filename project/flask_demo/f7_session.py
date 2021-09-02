'''
flask 默认是将session存储到内存中，如果想将session持久化到数据库，需要依赖flask-session
'''
from flask import Flask,session
import os
from datetime import timedelta
app=Flask(__name__)

# 使用一组随机数对session进行加密
app.config['SECRET_KEY'] = os.urandom(24)

# 设置 Session 过期时间为 2 天  (如果不设置，默认浏览器退出即自动结束)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# 用户请求设置session
@app.route('/set_session')
def set_session():
    session['username'] = 'marshall'
    # 设置持久化
    session.permanent = True  # flask默认生存为31天,django是14天

    return '设置Session成功!'

# 用户请求清除session
@app.route('/del_session')
def del_session():
    try:
        # 3种删除session方法
        # session.pop("username")
        # session.clear()  # 清除所有session
        del session['username']
    except Exception:
         return "Session不存在!"
    return '清除Session成功！'

# 用户请求查询session
@app.route('/get_session')
def get_session():

    username = session.get('username')
    print(username)
    return "获取到的Session值为："+str(username)

if __name__=='__main__':
    app.run(debug=True)