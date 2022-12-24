from flask import Flask
from flask import jsonify
from flask import request
import time
import pymongo

app = Flask(__name__)

#keywords = ['iphone', 'android', 'cars', 'intel', 'microsoft', 'sony', 'java', 'python']

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
col = mydb['users']

@app.route('/')
def hello_world():  # put application's code here
    return '<h1> hello </h1>'


@app.route('/create')
def create():  # put application's code here
    return '<h1> Error...You must type a username, email, city and 8 favorite keywords </h1>'


@app.route('/create/<username>')
def post(username):  # put application's code here
    keywords = []

    keywords.append(str(request.args.get('k1')))
    keywords.append(str(request.args.get('k2')))
    keywords.append(str(request.args.get('k3')))
    keywords.append(str(request.args.get('k4')))
    keywords.append(str(request.args.get('k5')))
    keywords.append(str(request.args.get('k6')))
    keywords.append(str(request.args.get('k7')))
    keywords.append(str(request.args.get('k8')))

    col.insert_one({
        "username": username,
        "email": str(request.args.get('email')),
        'city': str(request.args.get('city')),
        'time': str(time.time()),
        'keywords': keywords
    })

    print(username +" insert to collection "+ col.name)
    output = jsonify(
            username=username,
            email=request.args.get('email'),
            city=request.args.get('city'),
            time=time.time(),
            keywords=keywords,
            status='user created'
        )
    #keywords.clear()
    return output

if __name__ == '__main__':
    app.run()
