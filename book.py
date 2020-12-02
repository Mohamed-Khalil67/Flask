# app.py
from flask import Flask, render_template
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
import json

app = Flask(__name__)
books = json.load(open("Data/books.json"))

@app.route('/')
def index():
	return 'API Tutorials with Flask.eg /api/v1/books to see books'

@app.route('/api/v1/books',methods=['GET'])
def get_books():
	return jsonify({"books":books})

@app.route('/api/v1/books/<string:title>',methods=['GET'])
def get_book_title(title):
	book = [book for book in books if book["title"] == title ]
	if len(book) ==0:
		print(404,"Book with title::{} does not exit".format(title))
	return jsonify({"books":book})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}),404)

if __name__ == "__main__":        
    app.run(debug=True,host='0.0.0.0',port=5000)                 
