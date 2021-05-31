from flask import Flask, Blueprint, render_template, redirect, url_for, request
from functools import wraps
from datetime import datetime 
import uuid

from models.database import boardDbInfo
from models.form import createArticleForm

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/')
def boardHome():
	return redirect(url_for('board.articleList'))

# 게시판 글 목록
@bp.route('/list/')
def articleList():
  # ariticleList = boardDbInfo().callList()
	articleList = boardDbInfo().boardDbCol.find({}).sort('createTime', -1)
	# page = request.args.get('page', type=int, default=1)
	# articleList = articleList.paginate(page, per_page=10)
	return render_template('article_list.html', articleList=articleList)

# 게시판 글 상세
@bp.route('/detail/<path:articleId>/')
def articleDetail(articleId):
	article = boardDbInfo().boardDbCol.find_one({'_id': articleId })
	return render_template('article_detail.html', article = article)

# 글 쓰기 페이지
@bp.route('/post/', methods=['GET', 'POST'])
def articleForm():
	form = createArticleForm()
	if request.method == 'POST' and form.validate_on_submit():
		articleData = {
			'_id' : uuid.uuid4().hex,
			'name' : request.form.get('name'),
			'subject': request.form.get('subject'),
			'content': request.form.get('content'),
			'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		}
		boardDbInfo().boardDbCol.insert_one(articleData)
		return redirect(url_for('board.articleList'))
	
	return render_template('article_form.html', form=form)

# 글 삭제
@bp.route('/delete/<path:articleId>/')
def deleteArticle(articleId):
	article = boardDbInfo().boardDbCol.find_one({'_id': articleId })
	boardDbInfo().boardDbCol.delete_one(article)
	return redirect(url_for('board.articleList'))

# #글 수정
# @bp.route('/edit/<path:articleId>/', methods=['GET', 'POST'])
# def editArticle(articleId):
# 	article = boardDbInfo().boardDbCol.find_one({'_id': articleId })

# 	# if request.method == 'POST':
# 	# 	form = createArticleForm()
# 	# 	if form.validate_on_submit():
# 	# 		form.populate_obj(article)
# 	# 		boardDbInfo().boardDbCol.update_one({'_id': articleId })
# 	# 		return redirect(url_for('board.detail', articleId = articleId))
# 	# else:
# 	form = createArticleForm(obj=article)
	
# 	return render_template('article_form.html', form=form)
	

