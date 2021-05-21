from flask import Flask
app = Flask(__name__)

from user.models import User

@app.route('/user/signup/', methods=['GET'])
def signup():
  return User().signup()

