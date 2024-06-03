##integrating HTML with flask
## HTTP GET and POST
#render_template:will help u to render HTML page
#request:will help to read the posted values
##jinja2:integrating HTML with data source
##GET and POST are HTTP request methods used to send data from client to server.
# #GET are used to recieve data from web server
#PoST requests are to post the data to be processed by web server
'''
{%...%}  statements, for loops
{{}} expressions to print output
{#...#} this is for comment
'''
from flask import Flask,redirect,url_for,render_template,request
##wsgi application is created
app= Flask(__name__)

@app.route('/')##decorator that defines route for root URL of app(homepage).
#when the user visits root URL of flask app in browser, func below this decorator will be executed.
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')##building of url dynamically by variable rules
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"
    exp={'score':score,'result':res}
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return"The failed and marks are="+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks>=50:
        result="success"
    else:
        result="fail"
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])  
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    return redirect(url_for('success',score=total_score))


if __name__=='__main__':
    app.run(debug=True)##any change is reflected auto on refreshing chrome