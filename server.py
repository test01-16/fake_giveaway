# https://flask.palletsprojects.com/en/1.1.x/
from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect("https://www.tesla.com/",code=302)

@app.route('/eth')
def eth_world():
    return render_template("eth.html")

@app.route('/btc')
def btc_world():
    return render_template("btc.html")

@app.route('/ping')
def home_world():
    return {"status":200}

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
#   app.run(host='localhost', port=8080)
  app.run(host='0.0.0.0', port=8000)
  
