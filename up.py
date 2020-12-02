from flask import Flask

app = Flask(__name__)


#route for home page
@app.route("/")
def index():
    return "Hello World!"

#run at http://0.0.0.0:5000
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)