from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape


app=Flask(__name__)


# 自定义状态码
@app.route('/')
def status():
    # 1、使用元组，返回自定义响应信息
    # 返回的3个参数：响应体，状态码，响应头
    # return '状态码更改成功！',666,(["name","tom"],['age',18])
    # return ('状态码更改成功！',666,(["name","tom"],['age',18]))
    # return '状态码更改成功！', 888, {'language':'python'}

    # 2、使用make_response构造响应信息
    resp=make_response('hello') # 响应体
    resp.status='999 diy' # 状态码
    resp.headers['gender']='male' # 响应头
    return resp

if __name__=='__main__':
    app.run(debug=True,port='5000')