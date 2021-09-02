from flask import Flask
from flask import abort, redirect, url_for,render_template,make_response,Response

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    # abort() 函数提前中断一个请求并带有一个错误代码
    abort(401)

@app.route('/login1')
def login1():
    resp=Response('login failed')
    abort(resp)

# errorhandler()装饰器定制错误页面
@app.errorhandler(401)
def page_not_found(error):
    resp = make_response(render_template('11.html'), 404)
    resp.headers['info'] = 'DIY'
    return resp
    # 或直接用下面这一条语句
    # return render_template('11.html'),404

if __name__=='__main__':
    app.run(debug=True)