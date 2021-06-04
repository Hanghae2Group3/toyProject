from typing import Dict
from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from passlib.hash import pbkdf2_sha256
from functools import wraps
import uuid

from models.form import userLoginForm, userSignupForm
from models.database import dbInfo, dbFunc

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
dbBooks = client.booklists


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
				'password': pbkdf2_sha256.encrypt(form.userPassword.data)
			}
				
			dbFunc().insertUserData(userData)
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
@bpBook.route('/library/')
def library():
  reviews = list(dbBooks.booklists.find({}))
  return render_template('book_library.html', data = reviews)

#-- 라이브러리 : 읽은 책 저장 --#
@bpBook.route('/library/bookread/', methods=['GET', 'POST'])
def insertBookReadToList():
  if request.method == 'POST':
    bookId = request.form.get("favbookId")
    currentUserId = session["user"]["_id"]
    user = dbFunc().findUserById(currentUserId)
    dbInfo().userCol.update_one({"_id": currentUserId}, {"$push": {"bookRead": bookId}})
    return jsonify({'msg' : 'POST 성공'})

  return redirect(url_for('book.library'))



#-- 즐겨찾기(임시라우트) --#
@bpBook.route('/cart/')
@login_required
def cart():
	currentUserId = session["user"]["_id"]
	currentUser = dbFunc().findUserById(currentUserId)
	books = currentUser["bookRead"]

	bookList = []
	for bookId in books:
		bookInfo = dbInfo().bookCol.find_one({"_id": bookId})
		bookList.append(bookInfo)
	
	return render_template('book_cart.html', data = bookList)


