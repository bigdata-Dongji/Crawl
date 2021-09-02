from flask import Flask,make_response,Response,request
app=Flask(__name__)

@app.route('/')
def index():
    ...

@app.route('/cookie')
def cookie():
    resp=make_response('写入cookie成功啦')
    # resp=Response('写入cookie成功啦')  # 第2种创建response对象
    resp.set_cookie('username','marshall')
    # max_age设置有效期/秒
    resp.set_cookie('age','3',max_age=3000)
    return resp

@app.route('/del_cookie')
def del_cookie():
    resp=Response('删除cookie成功啦')
    resp.delete_cookie('username')
    return resp

# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    username=request.cookies.get('username')
    if username:
        return "获取到的Cookie值为:" + username
    else:
        return u"没有获取到Cookie"

if __name__=='__main__':
    app.run(debug=True)