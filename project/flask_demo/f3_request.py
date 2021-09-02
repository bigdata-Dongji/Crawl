from flask import Flask, request, render_template,flash
import os
app=Flask(__name__)
# 两种方式设置secret_key
# app.secret_key=os.urandom(24)
app.config['SECRET_KEY']=os.urandom(24)



@app.route('/login', methods=['GET', 'POST'])  # 设置请求方法
def login():
    if request.method == 'POST': # 捕获请求方法
        print('POST run successful!')
        user=request.form.get('username') # 获取post方法表单，只获取第一个username
        passwd=request.form.get('password')
        u=request.form.get('user')
        user_li=request.form.getlist('user') # getlist()方法获取多个同名的值
        data=request.data  # data属性可以接受json,js,xml等post请求数据
        print(user,passwd)
        print(u)
        print(user_li)
        print(data)
        if passwd=='123':
            flash('登录成功！')
    else:
        print('GET run successful!')
        id=request.args.get('id') # 获取url参数
        print(id)
    return render_template('3-request.html')






if __name__ == '__main__':
    app.run(debug=True) # debug是否调试模式