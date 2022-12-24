from flask import Flask
from flask import jsonify
from flask import request
from articles import postNewsAPI
import json
import time
import pymongo

app = Flask(__name__)

keywords = ['iphone', 'android', 'cars', 'intel', 'microsoft', 'sony', 'java', 'python']
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
users = mydb['users']

@app.route('/')
def hello_world():  # put application's code here
    return '<h1> hello </h1>'

@app.route('/iphone')
def iphone():  # put application's code here
    return postNewsAPI('iphone')


@app.route('/create')
def create():  # put application's code here
    return '<h1> Error...You must type a userid, city and 8 favorite keywords </h1>'


#127.0.0.1:5000/create/akis?k1=iphone&k2=android&k3=cars&k4=intel&k5=microsoft&k6=sony&k7=java&k8=python&city=athens
@app.route('/create/<userid>')
def post(userid):  # put application's code here
    try:
        user_test = users.find_one({'userid': userid}).get('userid')
        if (str(user_test) == str(userid)):
            return '<h1> Error... this user is already created </hi>'
    except AttributeError:
        keywords = []
        keywords.append(str(request.args.get('k1')))
        keywords.append(str(request.args.get('k2')))
        keywords.append(str(request.args.get('k3')))
        keywords.append(str(request.args.get('k4')))
        keywords.append(str(request.args.get('k5')))
        keywords.append(str(request.args.get('k6')))
        keywords.append(str(request.args.get('k7')))
        keywords.append(str(request.args.get('k8')))

        users.insert_one({
            "userid": str(userid),
            'city': str(request.args.get('city')),
            'time': str(time.time()),
            'keywords': keywords
        })

        print(userid +" insert to collection "+ users.name)
        output = {
            "userid": userid,
            'city': str(request.args.get('city')),
            'time': str(time.time()),
            'keywords': keywords
        }

        # Serializing json
        json_object = json.dumps(output)
        # Writing to sample.json
        with open("user.json", "w") as outfile:
            outfile.write(json_object)
        #keywords.clear()
        return output


@app.route('/read')
def read():  # put application's code here
    return '<h1> Error...You must type the userid to continue </h1>'

@app.route('/read/<userid>', methods = ['GET'])
def get(userid):  # put application's code here
    try:
        user = users.find_one({'userid': userid}).get('userid')
        if (str(user) == str(userid)):
            keys = users.find_one({'userid': userid}, {'keywords': 1}).get('keywords')
            for k in keys:
                col = mydb[k]
                print(col.name)
            return jsonify({'keywords': str(keys)})
    except:
        return '<h1> Error... this user is not exist! </hi>'



if __name__ == '__main__':
    app.run()
