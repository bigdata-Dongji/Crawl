from flask import Flask,render_template,request,abort,session,\
    jsonify,redirect,url_for,flash,Response,make_response,escape


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('18.html')

if __name__=='__main__':
    app.run(debug=True,port='5000')