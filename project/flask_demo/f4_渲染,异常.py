from flask import Flask, render_template, jsonify

app=Flask(__name__)
@app.route('/')
def hello():
    data=[2,'name']
    data='{"movie_name": "八佰", "boxoffice": 309200.0}'
    d=jsonify(data)
    print(d)
    # return render_template('4-demo.html',data=data)
    return jsonify(data)


# 参数为 捕获的状态码
@app.errorhandler(404)
def error(e):
    return '网页被外星人搬走了***'

if __name__ == '__main__':
    app.run(debug=1)