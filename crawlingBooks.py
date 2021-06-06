# DB에 데이터 집어넣었음 (나중에 수정)

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.booklists

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=2&orderClick=DAB&mallGb=KOR&linkClass=A', headers=headers) # 월간 첫 페이지
soup = BeautifulSoup(data.text, 'html.parser')

books = soup.select('#main_contents > ul > li')
# 코딩 시작
if books is not None:
    for book in books:
        book_details = book.select_one('div.detail')
        title_book = book_details.select_one(
            'div.title > a').text  # 책 제목
        img_book = book.select_one('div.cover > a > img')['src'] # 이미지 링크 가져왔음
        subtitle_book = book_details.select_one(
            'div.subtitle').text.strip()  # 서브타이틀은 없는 경우에 넣어주지 않기
        # if len(subtitle_book) == 0:
        #     continue
        # author_publisher_date = book_details.select_one('div.author').text # 깔끔하게 분리가 안된다.
        reviews = book_details.select_one('div.review > img')['src'] # 리뷰 별점 이미지
        price = book_details.select_one('div.price > strong.book_price').text # 가격
        doc = {
            'title' : title_book,
            'subtitle' : subtitle_book,
            'img_link' : img_book,
            'review_img' : reviews,
            'price' : price,
            'favorite' : 0,
        }
        db.booklists.insert_one(doc)
