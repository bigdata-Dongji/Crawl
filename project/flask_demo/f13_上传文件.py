from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape

import os

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

# 上传文件第1种方法
@app.route('/upload1',methods=['POST'])
def upload1():
    file = request.files.get('img')
    if file is None:
        return '未上传图片'
    else:
        f=open('static/test.png','wb')
        f.write(file.read())
        f.close()

# 上传文件第2种方法
@app.route('/upload2',methods=['POST'])
def upload2():
    file = request.files.get('img')
    if file is None:
        return '未上传图片'
    else:
        file.save('static/test2.png') # 保存文件
        return '上传成功'
if __name__ == '__main__':

    app.run(debug=True,port='5000')