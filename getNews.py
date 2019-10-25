# ---------- Firebase Config Begins ---------- #

import pyrebase

firebase_config = {
    "apiKey": "AIzaSyDN9wi_VIbE1lBeg15WFF24j3tyC_F5Agk",
    "authDomain": "medialabhackathon.firebaseapp.com",
    "databaseURL": "https://medialabhackathon.firebaseio.com",
    "projectId": "medialabhackathon",
    "storageBucket": "medialabhackathon.appspot.com",
    "messagingSenderId": "1056171249747",
    "appId": "1:1056171249747:web:eafd3a29b79e996e97f6a6",
    "measurementId": "G-ZJ8YTQ3Z4M"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# ---------- Firebase Config Ends ---------- #


def getFeed():
	response = []
	news = db.child('all_news').get().val()

	MAX_COUNT = 10
	count = 0

	for newsid, newsvalue in news.items():
		newsdata = {
			"html_text": newsvalue["html_text"],
			"highlights": newsvalue["highlights"],
			"image_url": newsvalue["image_url"],
			"timetoread": newsvalue["timetoread"],
			"release_date": newsvalue["release_date"],
			"title": newsvalue["title"],
			"subtitle": newsvalue["subtitle"]
		}
		response.append(newsdata)

		count += 1
		if count == MAX_COUNT:
			break

	return response

getFeed()


# --------- Flask Code Begins --------- #

#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/getFeed')
def solve():
	response = getFeed()
	return jsonify({
		'result': response,
		'status': 'ok',
		'code': 200
	})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 7744)

# --------- Flask Code Ends --------- #