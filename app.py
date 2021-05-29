from flask import Flask, redirect, url_for
#-- create flask app instance --#
app = Flask(__name__)
app.secret_key = 'doingDev'

#-- DB --#
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#-- main route --#
@app.route('/')
def home():
	return redirect(url_for('board.articleList'))

#-- blueprint --#
from views import boardView
app.register_blueprint(boardView.bp)

