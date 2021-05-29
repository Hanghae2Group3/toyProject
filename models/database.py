from flask import Flask
from app import client

# 게시판 DB

class boardDbInfo():
	db = client.team3toy
	boardDbCol = db.board