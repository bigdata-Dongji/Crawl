# encoding:utf8
from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route('/login',methods=['POST'])
def index():
    username=request.form.get('username')
    password=request.form.get('password')
    
    # 参数判断
    if not all([username,password]):
        resp={
            "code":1,
            "message":"invalid params"
        }
        return jsonify(resp)
    elif username=='admin' and password == 'python':
        resp={
            'code':0,
            'message':'login success'
        }
        return jsonify(resp)
    else:
        resp={
            'code':2,
            'message':'wrong username or password'
        }
        return jsonify(resp)

if __name__=='__main__':
    app.run(debug=True,port='5000')