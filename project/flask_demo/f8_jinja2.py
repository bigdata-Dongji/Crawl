from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    data={'name':'xiaoMing','age':18}
    lists=[1,2,3,4]
    tom_score=90
    return render_template('8-jinja2.html',data=data,lists=lists,tom_score=tom_score)


# 自定义jinja2过滤器
def say_hello(name):
    return 'hello '+name
app.add_template_filter(say_hello,'greet')  # 注意传入函数不能有括号

if __name__=='__main__':
    app.run(debug=True)