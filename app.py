from flask import Flask
from articles import postNewsAPI

app = Flask(__name__)

keywords = ['bitcoin', 'tesla']

@app.route('/')
def hello_world():  # put application's code here
    return '<h1> hello </h1>'


@app.route('/all_articles')
def get_all_articles():  # put application's code here
    return postNewsAPI(keywords[0])



if __name__ == '__main__':
    app.run()
