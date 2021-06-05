from flask import Flask, redirect, render_template, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'doingDev'

#-- index --#
@app.route('/')
def index():
	return render_template('index.html')

#-- view.py --#
from models import view
app.register_blueprint(view.bpUser)
app.register_blueprint(view.bpBook)

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
