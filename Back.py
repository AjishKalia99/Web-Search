from flask import Flask,render_template,request,redirect,url_for
import requests,json
app=Flask(__name__)

def Api(data,page):
    parameters={'q':data,'cx':'010770557411319608341:uu-ygn-9kdo','key':'AIzaSyDgo0K5lsB5LbThqJRpladleZ1lZ8tAVnY','start':page}
    response=requests.get("https://www.googleapis.com/customsearch/v1",params=parameters)
    res=response.json()
    return res

i=1
data=None

@app.route('/')
def index():
    Dat=None
    global i
    i=1
    return(render_template('index.html',data=Dat,i=i))

@app.route('/results')
def results():
    global data
    data = request.args.get('search')
    Dat=Api(data,i)
    return(render_template('results.html',data=Dat,i=i))

@app.route('/Next/')
def Next_Page():
    global i
    i=i+10
    Dat=Api(data,i)
    return(render_template('results.html',data=Dat,i=i))

@app.route('/Prev/')
def Prev_Page():
    global i
    i=i-10
    Dat=Api(data,i)
    return(render_template('results.html',data=Dat,i=i))


@app.route('/Home')
def index1():
    global data
    global i
    i=1
    data = request.args.get('search')
    Dat=Api(data,i)
    return(render_template('results.html', data=Dat,i=i))


@app.errorhandler(Exception)
def All_Err(e):
    return(render_template('Some_Wrong.html'))

if __name__=='__main__':
    app.run(debug=True)
