from flask import Flask, url_for,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)
# test_request_context() 方法告诉 Flask 表现得像是在处理一个请求

# 重定向
@app.route('/redi')
def redi():
    return redirect(url_for('login'))
# 重定向2
@app.route('/redi2')
def redi2():
    return redirect(url_for('profile',username='marshall'))
# 重定向到百度
@app.route('/redi3')
def redi3():
    return redirect('https://www.baidu.com/')

with app.test_request_context():
     print(url_for('index'))
     print(url_for('login'))
     print(url_for('login', next='/'))
     print(url_for('profile', username='John Doe'))
'''
print出以下结果
/
/login
/login?next=%2F   # 对字符串进行了转义，未知变量部分被当做查询参数
/user/John%20Doe
'''
if __name__ == '__main__':
    app.run(debug=1)