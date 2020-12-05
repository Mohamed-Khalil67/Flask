# app.py
from flask import Flask,render_template, jsonify, make_response,abort, url_for, request
import json
import os

app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

with open('Data/books.json') as json_file:
	books = json.load(json_file.read())


@app.route('/')
def index():
	""" Search Bar to seach for Books """
	return render_template('Show_Book.jinja2')

@app.route('/api/books',methods=['GET'])
def get_books():
	""" Get All Books of json """
	return jsonify({"books":books})

@app.route('/api/books/<string:title>',methods=['GET'])
def get_book_title(title):
	""" Get title of a book and it's details """
	book = [book for book in books if book["title"] == title ]
	if len(book) ==0:
		abort(404,"Book with title::{} does not exit".format(title))
	return jsonify({"books":book})

@app.route('/api/book',methods=['GET'])
def get_book_details():
	""" Get A book title details """
	title = books["title"]
	book = [book for book in books if book["title"] == title ]
	return render_template('Show_Book.jinja2',result=request.json['title'][0])

@app.errorhandler(404)
def not_found(error):
	""" Si l'URl est mal écrit on aura un error : NotFound"""
	return make_response(jsonify({'error':'Not Found'}),404)

#run at http://0.0.0.0:5000
if __name__ == "__main__":        
    app.run(debug=True,host='0.0.0.0',port=port)                 
