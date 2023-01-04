from flask import Flask
from flask import jsonify
from flask import request
import time
import pymongo

app = Flask(__name__)

# my keywords for database
#keywords = ['iphone', 'android', 'cars', 'intel', 'microsoft', 'sony', 'java', 'python']
keywords = ['pop', 'greece', 'cars', 'gaming', 'microsoft', 'sony', 'xbox', 'marketing']

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
users = mydb['users']

@app.route('/')
def menu():  # put application's code here
    return "<h1>Welcome to the System!</h1>" \
           "<p>Menu:</p>" \
           "<p>-create</p>" \
           "<p>-read</p>" \
           "<p>-update</p>" \
           "<p>-delete</p>"


@app.route('/create', methods = ['POST'])
def create():  # put application's code here
    return '<h1> You must type a userid, city and 8 favorite keywords </h1>'



@app.route('/create/<userid>', methods = ['POST'])
def create_one(userid):  # put application's code here
    try:
        user_test = users.find_one({'userid': userid}).get('userid')
        if str(user_test) == str(userid):
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

        print("User "+ userid +" insert to collection "+ users.name)

        output = {
            "userid": userid,
            'city': str(request.args.get('city')),
            'time': str(time.time()),
            'keywords': keywords,
            'status': 'User created'
        }

        return output


@app.route('/read', methods = ['GET'])
def read():  # put application's code here
    return '<h1> You must type the userid to continue </h1>'

@app.route('/read/<userid>', methods = ['GET'])
def read_one(userid):  # put application's code here

    try:
        # check if userid exists
        user_test = users.find_one({'userid': userid}).get('userid')
        if str(user_test) == str(userid):
            source_names_db = mydb["sources_domain_name"]
            # list with all extracts from all domains names
            extracts_list = {}
            # all domain names
            source_names = []
            cursor = source_names_db.find({})
            for document in cursor:
                for key in document.keys():
                    value = document.get(key)
                    source_names.append(key)
                    if value is not None:
                        # extracts is exist and store
                        extracts_list[key] = str(value)


            output = {}
            # find user keywords
            keys = users.find_one({'userid': userid}, {'keywords': 1}).get('keywords')
            for k in keys:
                # every collection
                col = mydb[k]
                # initilize articles for each keyword
                articles = {}
                # initilize extracts for each keyword
                extracts = {}
                for s in source_names:
                    documents = []
                    cursor = col.find({})
                    for document in cursor:
                        # search for all articles in this keyword collection
                        for i in range(len(document.get('articles'))):
                            # if find this source name, store documents
                            if s == document.get('articles')[i]['source']['name']:
                                documents.append(document.get('articles')[i])
                                articles[s] = documents
                                # if source names has extract from list and it's not stored yet, store now
                                if (s in extracts_list.keys()) and (s not in extracts.keys()):
                                    extracts[s] = extracts_list.get(s)
                # output with articles and extracts from this collection/keyword
                output[k] = {'articles': articles, 'extracts': extracts}

            return output

    except AttributeError:
        return '<h1> userid Dont exist ! </h1>'




@app.route('/update', methods = ['PUT'])
def update():  # put application's code here
    return '<h1> You must type the userid and new keywords to continue </h1>'


#http://127.0.0.1:5000/update/akis?k1=iphone&k2=android&k3=cars&k4=intel&k5=microsoft&k6=sony&k7=java&k8=python&city=athens
@app.route('/update/<userid>', methods = ['PUT'])
def update_one(userid):  # put application's code here
    try:
        user_test = users.find_one({'userid': userid}).get('userid')
        if str(user_test) == str(userid):
            keywords = []
            keywords.append(str(request.args.get('k1')))
            keywords.append(str(request.args.get('k2')))
            keywords.append(str(request.args.get('k3')))
            keywords.append(str(request.args.get('k4')))
            keywords.append(str(request.args.get('k5')))
            keywords.append(str(request.args.get('k6')))
            keywords.append(str(request.args.get('k7')))
            keywords.append(str(request.args.get('k8')))
            users.update_one({'userid': userid}, {"$set": {'keywords': keywords}})
            print('User '+ userid+ 'updates his keywords')

            return jsonify({'status': 'update completed',
                            'keywords': keywords,
                            'userid': userid})
        else:
            return '<h1> Error... this user is not exist! </hi>'
    except:
        return '<h1> Error... this user is not exist! </hi>'




@app.route('/delete', methods = ['DELETE'])
def delete():  # put application's code here
    return '<h1> You must type the userid to continue </h1>'

@app.route('/delete/<userid>', methods = ['DELETE'])
def delete_user(userid):  # put application's code here
    try:
        user_test = users.find_one({'userid': userid}).get('userid')
        if (str(user_test) == str(userid)):
            users.delete_one({'userid': userid})
            print('User ' + userid + ' has deleted from collection '+ users.name)
            return jsonify({'status': 'User Deleted'})
        else:
            return '<h1> Error... this user is not exist! </hi>'
    except:
        return '<h1> Error... this user is not exist! </hi>'



if __name__ == '__main__':
    app.run()
