from pymongo import MongoClient
from bson.objectid import ObjectId

class dbInfo:
	client = MongoClient('mongodb://localhost', 27017)

	userDb = client['team3toy']
	userCol = userDb['user']

	bookDb = client['booklists']
	bookCol = bookDb['booklists']

#client = MongoClient('mongodb://localhost', 27017)
#client = MongoClient('mongodb://youngkwak:1006@15.164.169.53', 27017)

class dbFunc:
	# user : 이메일로 유저 찾기
	def findUserByEmail(self, email):
		user = dbInfo().userCol.find_one({'email' : email})
		return user

	#	user : 아이디값으로 유저 찾기
	def findUserById(self, id):
		user = dbInfo().userCol.find_one({'_id' : id})
		return user

	# user : 사용자 정보 db 저장
	def insertUserData(self, userData):
		dbInfo().userCol.insert_one(userData)

	# book : 읽은 책 저장 
	def updateBookRead(refUserId, bookId):
		dbInfo().userCol.update({'_id': refUserId}, {'$push': {'bookRead': bookId}})

	# book : 읽은 책 삭제
	def deleteBookRead(refUserId, bookId):
		dbInfo().userCol.delete_one({'_id': refUserId}, {'$unset:': {'bookRead': bookId}})

	# book : 읽을 책 저장
	def updateBookToRead(refUserId, bookId):
		dbInfo().userCol.update({'_id': refUserId}, {'$push': {'bookToRead': bookId}})
	
	# book : 읽을 책 삭제
	def deleteBookToRead(refUserId, bookId):
		dbInfo().userCol.delete_one({'_id': refUserId}, {'$unset:': {'bookToRead': bookId}})


# class handleObjectId:
# 	# 리스트 전체 ObjectId str값으로 변환
# 	def objectIdDecoder(self, list):
# 		results = []
# 		for document in list:
# 			document['_id'] = str(document['_id'])
# 			results.append(document)
# 			return results

# 	# ObjectId str값 
# 	def getSpecificId(id):
# 		result = handleObjectId().objectIdDecoder(list(dbInfo().bookCol.find({"_id": ObjectId(id)})))
# 		return str(result)





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





