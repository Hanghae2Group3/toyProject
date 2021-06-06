from typing import Dict, Reversible
from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from passlib.hash import pbkdf2_sha256
from functools import wraps
import uuid
from datetime import *

from wtforms.widgets.html5 import DateTimeLocalInput

from models.form import userLoginForm, userSignupForm
from models.database import dbInfo, dbFunc

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
dbBooks = client.booklists
favCols = client.team3toy.favorites

#-- 데코레이터 : 로그인 세션 확인 --#
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('user.login'))
	
	return wrap

###--- 사용자 뷰 ---###
bpUser = Blueprint('user', __name__, url_prefix='/user')

#-- 즐겨찾기(메인) (로그인 필요) --#
@bpUser.route('/dashboard/')
@login_required
def dashboard():
	return render_template('user_dashboard.html')

#-- 사용자 등록 --#
@bpUser.route('/signup/', methods = ['GET', 'POST'])
def signup():

	form = userSignupForm()

	if request.method == 'POST' and form.validate_on_submit():
		user = dbFunc().findUserByEmail(form.userEmail.data)
		if not user:
			userData = { 
				'_id' : uuid.uuid4().hex,
				'name' : form.userName.data,
				'email' : form.userEmail.data,
				'password': pbkdf2_sha256.encrypt(form.userPassword.data),
				'count' : {'read': 0 , "unread":0, "total":0},
			}
				
			dbFunc().insertUserData(userData)
			favCols.insert({'_id': userData['_id'], 'favorites':[]})
			

			return redirect(url_for('user.login'))

		else:
			flash('이미 등록된 이메일입니다.')	

	return render_template('user_signup.html', form = form)

#-- 로그인 --#
@bpUser.route('/login/', methods=['GET', 'POST'])
def login():
	form = userLoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		error = None
		user = dbFunc().findUserByEmail(form.userEmail.data)
        
		if not user:
			error = '존재하지 않는 사용자입니다.'

		elif not (pbkdf2_sha256.verify(form.userPassword.data, user["password"])):
			error = '비밀번호가 일치하지 않습니다.'

		if error is None:
			del user['password']
			session['logged_in'] = True
			session['user'] = user
		
			return redirect(url_for('user.dashboard'))

		flash(error)

	return render_template('user_login.html', form = form)

#-- 로그아웃 --#
@bpUser.route('/logout/')
def logout():
	session.clear()
	return redirect('/')


###--- 책 뷰 ---###
bpBook = Blueprint('book', __name__, url_prefix='/book')

#-- 라이브러리 --#
@bpBook.route('/library/', methods=['GET'])
def library():
  data = list(dbInfo().bookCol.find({}))
  return render_template('book_library.html', data = data)

#-- 라이브러리 : 읽은 책 저장 --#
@bpBook.route('/library/bookread/', methods=['GET', 'POST'])
def insertBookReadToList():
	if request.method == 'POST':
		bookId = request.form.get("favbookId")
		
		favList = favCols.find_one({'_id': session["user"]["_id"]})['favorites']
		
		#이미 책 담았는지 확인
		flag = None
		for favbook in favList:
			if favbook['bookRead'] == bookId :
				flag = 1
				return jsonify({'msg' : '이미 저장된 책입니다.'})
				
		# checkExist = favCols[currentUserId]["favorites"].find({bookId: {'$exists': True}})
		# if checkExist == True:
		# 	favCols.update_many({}, {'$unset' : {"favorites": {'bookRead': bookId}}})

		else:
			favCols.update_one(
				{'_id': session["user"]["_id"]},
				{'$addToSet': {"favorites" : {'bookRead' : bookId, 'isRead': 0, 'createTime': datetime.now()}}},True)
		# dbInfo().userCol.find({"_id": currentUserId}, {'$inc': {"count": {'total': 1}}}, upsert=False)
		# dbInfo().userCol.find({"_id": currentUserId}, {'$inc': {"count": {'unread': 1}}}, upsert=False)

	return redirect(url_for('book.library'))



#-- 즐겨찾기(임시라우트) --#
@bpBook.route('/favorites/')
@login_required
def favorites():
	currentUserId = session["user"]["_id"]
	currentUserFavs = favCols.find_one({'_id': currentUserId})
	books = currentUserFavs['favorites']
	# sortedBookListByTime = sorted(books, key=(lambda x: x['createTime']), reverse=True)
	bookList = []
	if len(books) != 0:
		for bookId in reversed(books):	
			bookInfo = dbInfo().bookCol.find_one({'_id': bookId['bookRead']})
			bookList.append(bookInfo)
		return render_template('book_favorites.html', data = bookList)
		
	return render_template('book_favorites_empty.html')
	


#-- 즐겨찾기 삭제 --#
@bpBook.route('/favorites/delete/', methods=['POST'])
def deleteFavs():
	if request.method == 'POST':
		bookId = request.form.get("favBookId")

		favCols.update_one(
			{'_id': session["user"]["_id"]},
			{'$pull': {'favorites' : {'bookRead': bookId}}}, bypass_document_validation = True) #
		# dbInfo().userCol.find({"_id": currentUserId}, {'$inc': {"count": {'total': 1}}}, upsert=False)
		# dbInfo().userCol.find({"_id": currentUserId}, {'$inc': {"count": {'unread': 1}}}, upsert=False)
		
		return jsonify({'msg': '삭제 성공'})

	return jsonify({'msg': '삭제 실패'})
