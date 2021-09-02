'''
正则匹配路由:根据自己的规则去限定参数在进行访问
应用场:景:限制用户访问
具体实现步骤为:

导入转换器基类:在Flask中，所有的路由的匹配规则都是使用转换器对象进行记录
自定义转换器:自定义类继承于转换器基类
汤加转换器到默认的转换器字典中
使用自定义转换器实现自定义匹配规则
'''
from werkzeug.routing import BaseConverter
from flask import Flask

# 自定义转换器
class RegexConverter(BaseConverter):

    def __init__ (self,url_map,*args):
        # super重写父类
        super(RegexConverter, self).__init__(url_map)
        # 将第一个接受的参数当做匹配规则进行保存
        self.regex=args[0]


app=Flask(__name__)
# 将自定义转换器添加到转换器字典中，并指定使用时的名字：re
app.url_map.converters['re']=RegexConverter

@app.route('/user/<re("[0-9]{3}"):user_id>')
def index(user_id):
    return user_id


if __name__ == '__main__':
    app.run(debug=1)