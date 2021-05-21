from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid
from app import db

class User:

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get("inputName"),
      "phone": request.form.get("inputPhoneNum"),
      "email": request.form.get("inputEmail"),
      "password": request.form.get("inputPassword")
    }

    # Encrypt the password
    user["password"] = pbkdf2_sha256.encrypt(user["password"])

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify(user), 200