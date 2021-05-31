from flask import Flask, Blueprint, render_template, redirect, url_for, request

bp = Blueprint('userAuth', __name__, url_prefix='/user')

@bp.route('/dashboard/')
def dashboard():
	return render_template('user_dashboard.html')

@bp.route('/signup/')
def signup():
	return render_template('user_signup.html')

@bp.route('/login/')
def login():
	return render_template('user_login.html')