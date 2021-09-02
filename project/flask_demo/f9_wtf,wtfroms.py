from flask import Flask, request, flash, render_template
from flask_wtf import FlaskForm
import os
# 导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField
# 导入表单验证器
from wtforms.validators import DataRequired,EqualTo



app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
# 关闭csrf校验
# app.config['WTF_CSRF_ENABLED']=False

# 自定义表单类  继承FlaskFrom
class RegisterForm(FlaskForm):
    # 文本字段
    username=StringField('用户名',validators=[DataRequired('请输入用户名')],render_kw={'placeholder':'请输入用户名'})
    # 密码字段
    password=PasswordField('密码',validators=[DataRequired('请输入密码')])
    password2=PasswordField('密码',validators=[DataRequired('请输入确认密码'),EqualTo('password','两次密码不一致')])
    # 提交字段
    submit=SubmitField('注册')



@app.route('/register',methods=['POST','GET'])
def index():
    register_form=RegisterForm()
    # 验证表单
    if register_form.validate_on_submit():
        username=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('password2')

        print(username,password,password2)
        return 'OK'

    else:
        if request.method=='POST':
            flash('用户名或密码错误')

    return render_template('9.html',form=register_form)

if __name__=='__main__':
    app.run(debug=True)