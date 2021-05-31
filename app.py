from flask import Flask, redirect, url_for, render_template
#-- create flask app instance --#
app = Flask(__name__)
app.secret_key = 'doingDev'

#-- DB --#
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#-- main route --#
@app.route('/')
def home():
	return render_template('index.html')

#-- blueprint --#
from views import boardView, userView
app.register_blueprint(boardView.bp)
app.register_blueprint(userView.bp)