from flask import Flask
from articles import postNewsAPI

app = Flask(__name__)

keywords = ['iphone', 'android', 'cars']

@app.route('/')
def hello_world():  # put application's code here
    return '<h1> hello </h1>'


@app.route('/iphone')
def get_iphone():  # put application's code here
    return postNewsAPI('iphone')



if __name__ == '__main__':
    app.run()
