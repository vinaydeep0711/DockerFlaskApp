from flask import Flask, request, jsonify
import json


app = Flask(__name__)

"""__name__  represents the name of the application package and it is used by Flask to identify resources"""

stores = [
    {
        'name': 'My Book Store',
        'items': [
            {'name': 'Book',
             'price': 15.99
             }
        ]
    }
]

@app.route('/')
def name_of_app():
    return 'The value of __name__ is {}'.format(__name__) #main

#GET Method url - /health returns health of application
@app.route('/health', methods=['GET'])
def health():
    return 'Server is up and running'

@app.route('/stores') #get all
def get_stores():
    return jsonify({'store':stores})

@app.route('/stores/<string:name>')  #http://172.0.0.1:5000/store/'some_name'
def get_store_by_name(name):
    for store in stores:
        if store.get('name')==str(name):
            return jsonify(store)
    return jsonify({'message', 'store not found'})

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()#get the json posted by POST
    new_store ={
        'name':request_data['name'],
        'items':request_data['items']
    }
    stores.append(new_store)
    return jsonify(stores)



"""run the application using port 5000"""
app.run(port=5000)















