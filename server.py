from flask import Flask, render_template,request,redirect,session
app=Flask(__name__)
app.secret_key='insiyahakim'
@app.route('/')
def page():
    session['count'] += 1
    return render_template("index.html",session=session['count'])
@app.route('/index',methods=['POST'])
def index():
    session['count']+=1
    render_template("index.html",session=session['count'])
    return redirect('/')


@app.route('/index2',methods=['POST'])
def index2():
    session['count']=0
    return redirect('/')

app.run(debug=True)