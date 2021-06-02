from typing import Optional
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, validators 
from wtforms.fields.core import BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email



#-- 회원가입 폼 --#
class userSignupForm(FlaskForm):
	userName = StringField('이름', validators=[DataRequired('이름을 입력하세요.')])
	userEmail = EmailField('이메일', validators=[DataRequired('이메일을 입력하세요.'), Email('이메일 주소가 바르지 않습니다.')])
	userPassword = PasswordField(
		'비밀번호', validators=[DataRequired('비밀번호를 입력하세요.')])
	userPasswordConfirm = PasswordField('비밀번호 확인', 
		validators=[DataRequired('비밀번호를 한 번 더 입력하세요.'), EqualTo('userPassword', '비밀번호가 일치하지 않습니다.')])
	privacyPolicy = BooleanField('개인정보 처리 방침', [validators.required('필수 동의 항목에 동의해 주세요.')])
	termsOfService = BooleanField('서비스 이용 약관', [validators.required('서비스 이용 약관에 동의해 주세요.')])
	allowPromotions = BooleanField('프로모션 수신', [validators.optional()])

#-- 로그인 폼 --#
class userLoginForm(FlaskForm):
	userEmail = EmailField('이메일', validators=[DataRequired('등록한 이메일 주소를 입력하세요.'), Email('이메일 주소가 바르지 않습니다.')])
	userPassword = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력하세요.')])