from flask import Flask
from articles import postNewsAPI

app = Flask(__name__)

keywords = ['iphone', 'android', 'cars', 'intel', 'microsoft', 'sony', 'java', 'python']

@app.route('/')
def hello_world():  # put application's code here
    return '<h1> hello </h1>'


@app.route('/iphone')
def get_iphone():  # put application's code here
    # return consumer(keywords[0])
    return postNewsAPI(keywords[0])



if __name__ == '__main__':
    app.run()
