# app.py
from flask import Flask,render_template, jsonify, make_response,abort, url_for, request
import json
import os

app = Flask(__name__)
port = int(os.environ.get("PORT",5000))
books = json.load(open("Data/books.json"))

@app.route('/',methods=['POST','GET'])
def index():
	if request.method == 'POST':
		return 'Hello'
	else:
		return render_template('index.html')

@app.route('/api/books',methods=['GET'])
def get_books():
	return jsonify({"books":books})

@app.route('/api/books/<string:title>',methods=['GET'])
def get_book_title(title):
	book = [book for book in books if book["title"] == title ]
	if len(book) ==0:
		abort(404,"Book with title::{} does not exit".format(title))
	return jsonify({"books":book})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}),404)

#run at http://0.0.0.0:5000
if __name__ == "__main__":        
    app.run(debug=True,host='0.0.0.0',port=port)                 
