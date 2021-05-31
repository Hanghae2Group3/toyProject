from flask import Flask
from app import client

# 게시판 DB

class boardDbInfo():
	db = client.team3toy
	boardDbCol = db.board

	# def callList(self):
	# 	articleList = boardDbCol.find({}).sort('createTime', -1)
  #   return articleList


# from pymongo import MongoClient
# from datetime import datetime
# import uuid

# client = MongoClient('localhost', 27017)
# db = client.team3toy

# for i in range(50):
# 	articleData = {
# 		'_id': uuid.uuid4().hex,
# 		'name': '테스트유저:[%03d]' % i,
# 		'subject': '테스트 데이터:[%03d]' % i,
# 		'content': '내용무',
# 		'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 	}
# 	db.board.insert_one(articleData)