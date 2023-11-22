from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb+srv://naveenchandgadde:<password>@flask.0zcjxbr.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Example route to test the connection
@app.route('/test-mongo')
def test_mongo():
    collection = mongo.db.your_collection_name
    result = collection.find_one({'example_key': 'example_value'})
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
