from flask import Flask, render_template, jsonify, request, session, redirect
from functools import wraps

app = Flask(__name__)
app.secret_key = b":D'\x1d\x8f\xfa`f\xdb2;\xd7>E\xcfH"

import uuid
from passlib.hash import pbkdf2_sha256

from pymongo import MongoClient

# Database
client = MongoClient('localhost', 27017)
db = client.team3toy

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*arg, **kwargs):
    if 'logged_in' in session:
      return f(*arg, **kwargs)
    else:
      return redirect('/')

  return wrap



# Routes
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

# Class - User
class User:

  ## start session
  def start_session(self, user):
    del user["password"]
    session["logged_in"] = True
    session["user"] = user
    return jsonify(user), 200

  ## sign-up
  def signup(self):
    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get("inputName"),
      "email": request.form.get("inputEmail"),
      "password": request.form.get("inputPassword"),
      "passwordConfirm": request.form.get("inputConfirmPassword")
    }

    # check name value
    if not user["name"]:
      return jsonify({"error": "이름을 입력하세요."}), 400

    # check email validation /existing email address
    if not user["email"]:
      return jsonify({"error": "이메일을 입력하세요."}), 400
    else :
      if ("@" not in user["email"]) or ("." not in user["email"]):
        return jsonify({"error": "이메일을 정확히 입력해주세요."}), 400

      elif db.users.find_one({"email": user["email"]}):
        return jsonify({"error": "이미 가입된 이메일입니다."}), 400

    # check password validation
    if not user["password"]:
      return jsonify({"error": "비밀번호를 입력하세요."}), 400

    else:
      if not user["passwordConfirm"]:
        return jsonify({"error": "한 번 더 비밀번호를 입력하세요."}), 400

      elif user["password"] != user["passwordConfirm"]:
        return jsonify({"error": "입력하신 비밀번호가 서로 다릅니다."}), 400

    # Encrypt the password
    user["password"] = pbkdf2_sha256.hash(user["password"])
    user["passwordConfirm"] = pbkdf2_sha256.hash(user["passwordConfirm"])

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({"error" : "Signup failed"}), 400

  ## sign-out
  def signout(self):
    session.clear()
    return redirect('/')

  ## log-in
  def login(self):

    # check email value
    if not request.form.get("loginEmail"):
      return jsonify({"error": "이메일을 입력하세요."}), 400
    else :
      if ( "@" not in request.form.get("loginEmail") ) or ( "." not in request.form.get("loginEmail") ):
        return jsonify({"error": "이메일을 정확히 입력하세요."}), 400

    # check password value
    if not request.form.get("loginPassword"):
      return jsonify({"error": "비밀번호를 입력하세요."}), 400

    user = db.users.find_one({
      "email" : request.form.get("loginEmail")
    })

    if user and pbkdf2_sha256.verify(request.form.get("loginPassword"), user["password"]):
      return self.start_session(user)

    return  jsonify({"error" : "로그인 정보가 정확하지 않습니다."}), 401


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)