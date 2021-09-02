from notbook_tu.flask_qd import app
from flask import render_template
from notbook_tu.sql_dest import *

@app.route('/1')
def ksa_1():
    return render_template('te_1.html',name = te_1()[0],value =te_1()[1])

@app.route('/3')
def ksa_3():
    return render_template('te_3.html',name = te_3())

@app.route('/4')
def ksa_4():
    return render_template('te_4.html',name1 =te_4()[0],name2 =te_4()[1],name3 =te_4()[2],name4 =te_4()[3])

@app.route('/5')
def ksa_5():
    max_n=max(te_5()[0])*1.05
    return render_template('te_5.html',name1=te_5()[0],max_n=max_n)

@app.route('/6')
def ksa_6():
    max_n = max(te_5()[1]) * 1.05
    return render_template('te_6.html',name1=te_5()[1],max_n=max_n)

@app.route('/7')
def ksa_7():
    return render_template('te_7.html',name = te_6()[0],value = te_6()[1])

@app.route('/8')
def ksa_8():
    return render_template('te_8.html',name = te_7()[0])

@app.route('/9')
def ksa_9():
    return render_template('te_9.html',name = te_7()[1])

@app.route('/10')
def ksa_10():
    return render_template('te_10.html',name = te_7()[2])

@app.route('/11')
def ksa_11():
    return render_template('te_11.html',name = te_8()[0],value =te_8()[1])

@app.route('/12')
def ksa_12():
    return render_template('te_12.html',name = te_9()[0] , name1 = te_9()[1] )




