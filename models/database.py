from pymongo import MongoClient

class dbInfo:
	client = MongoClient('mongodb://localhost', 27017)
	db = client['team3toy']
	userDB = db['user']
#client = MongoClient('mongodb://localhost', 27017)
#client = MongoClient('mongodb://-', 27017)

class dbFunc:
	# 이메일 찾기
	def findUserEmail(self, email):
		userEmail = dbInfo().userDB.find_one({'email' : email})
		return userEmail

	# 사용자 정보 db 저장
	def insertUserData(self, userData):
		dbInfo().userDB.insert_one(userData)

	# 읽은 책 저장 
	def updateBookRead(refUserId, bookId):
		dbInfo().userDB.update({'_id': refUserId}, {'$push': {'bookRead': bookId}})

	# 읽은 책 삭제
	def deleteBookRead(refUserId, bookId):
		dbInfo().userDB.delete_one({'_id': refUserId}, {'$unset:': {'bookRead': bookId}})

	# 읽을 책 저장
	def updateBookToRead(refUserId, bookId):
		dbInfo().userDB.update({'_id': refUserId}, {'$push': {'bookToRead': bookId}})
	
	# 읽을 책 삭제
	def deleteBookToRead(refUserId, bookId):
		dbInfo().userDB.delete_one({'_id': refUserId}, {'$unset:': {'bookToRead': bookId}})

# # API 역할을 하는 부분
# @app.route('/api/list', methods=['GET'])
# def show_stars():
#     movie_stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
#     return jsonify({'star_list': movie_stars})


# @app.route('/api/like', methods=['POST'])
# def like_star():
#     name_receive = request.form['name_give']
#     target_star = db.mystar.find_one({'name': name_receive})
#     current_like = target_star['like']

#     new_like = current_like + 1

#     db.mystar.update_one({'name': name_receive},{'$set':{'like': new_like}})

#     return jsonify({'msg': '좋아요!'})


# @app.route('/api/delete', methods=['POST'])
# def delete_star():
#     name_receive = request.form['name_give']
#     db.mystar.delete_one({'name': name_receive})
#     return jsonify({'msg': '삭제 완료!'})





