###web application framework written in python
##based on jinja2 template and WSGI (pocco projects)
##WSGI-->web server gateway interface(standard/protocol):used to communicate between web server and application
##requests-->web server-->protocol(WSGI)-->web application
##jinja2-->popular template engine/web templating system. 
# it combines web template along with certain data source to render dynamic pages
##redirect-->make sure redirecting to required page
##url_for-->to create url dynamically



from flask import Flask,redirect,url_for
##wsgi application is created.
app= Flask(__name__)

@app.route('/')##decorator that defines route for root URL of app(homepage).
#when the user visits root URL of flask app in browser, func below this decorator will be executed.
def welcome():
    return'Welcome!!.How are you. hello. yellow'

@app.route('/members')
def members():
    return'Welcome!'

@app.route('/success/<int:score>')##building of url dynamically by variable rules
def success(score):
    return"<html><body><h1>The result is passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return"The failed and marks are="+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))
   
if __name__=='__main__':
    app.run(debug=True)##any change is reflected auto on refreshing chrome

