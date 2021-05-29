from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

# 게시판 글 쓰기 폼
class createArticleForm(FlaskForm):
	subject = StringField('제목', validators=[DataRequired('제목을 입력하세요.')])
	name = StringField('이름', validators=[DataRequired('이름을 입력하세요.')])
	content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])