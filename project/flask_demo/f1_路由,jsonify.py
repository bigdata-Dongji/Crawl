# 导入Flask类
from flask import Flask,jsonify
# 创建1个Flask类实例
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据，还有float浮点类型可以使用
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/ 之后的路径名
    return 'Subpath {}'.format(subpath)

# 唯一URL,带重定向行为，即使访问/projects不带斜线不会报错
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/rjson')
def rjson():
    json_dict={
        'name':'Marshall',
        'age':30
    }
    # jsonify帮助转为json数据，并设置响应头Content-Type为application/json
    # return jsonify(json_dict)
    return jsonify(topic='use jsonify',program='python')

if __name__ == '__main__':
    app.run(debug=True) # debug是否调试模式