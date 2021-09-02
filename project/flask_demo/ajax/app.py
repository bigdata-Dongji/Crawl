from flask import Flask, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@127.0.0.1:3306/breach2020'
# 将其设置为True时，每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=False
# 动态追踪  用于设置数据发生变更之后是否发送信号给应用
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO']=True
db=SQLAlchemy(app)
class tb(db.Model):
    __tablename__ = "wealth"   #表名
    rank = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    wealth = db.Column(db.String(255))
    sourse = db.Column(db.String(255))
    region = db.Column(db.String(255))
@app.route('/total_boxoffice_data',methods=['GET','POST'])
def data():

    q = [{'movie_name': '八佰', 'boxoffice': 309200},{'movie_name': '八佰', 'boxoffice': 309200}]

    q = tb.query.order_by(tb.rank).all()
    result = []
    for i in q:
        result.append({'movie_name': i.name, 'boxoffice': i.rank})
    print(jsonify(result))
    return jsonify(result)


@app.route('/total_boxoffice', methods=['GET', 'POST'])
def total_boxoffice():
    return render_template('total_boxoffice.html')

if __name__=='__main__':
    app.run(debug=True,port=8080)