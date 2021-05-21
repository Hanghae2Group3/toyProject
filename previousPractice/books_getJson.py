import os
import sys
import urllib.request
import json

# input-data from the search box (str)
searchKeyword = ""
encText = urllib.parse.quote(searchKeyword)
# json
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # + "&display=value" display value(int)

# naver api client information
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", "YOUR_CLIENT_ID")
request.add_header("X-Naver-Client-Secret", "YOUR_CLIENT_SECRET")

response = urllib.request.urlopen(request)

# --- for checking error code ---
# rescode = response.getcode()
# if(rescode == 200):
#     response_body = response.read()
#     responseJson = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)

rawJson = response.read().decode('utf-8')

# load json data
json_data = json.loads(rawJson)

# result
searchResult = json_data.get('items')

for result in searchResult :
    print(result['title'])
    print(result['link'])
    print(result['image'])
    print(result['author'])
    print(result['price'])
    print(result['discount'])
    print(result['publisher'])
    print(result['pubdate'])
    print(result['isbn'])
    print(result['description'])
    print('\n')
