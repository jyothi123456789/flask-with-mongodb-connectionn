from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    # Check user credentials (this is a simplified example)
    username = request.json.get('username')
    password = request.json.get('password')

    # If credentials are valid, generate a JWT
    if username == 'example' and password == 'password':
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({'user': username, 'exp': expiration}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token.decode('UTF-8')})

    return jsonify({'message': 'Invalid credentials'}), 401

# Protected endpoint
@app.route('/protected', methods=['GET'])
def protected():
    # Get the token from the request headers
    token = request.headers.get('Authorization')

    try:
        # Decode and verify the token
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': 'Welcome, ' + decoded_token['user']})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
        
if __name__ == '__main__':
    app.run(debug=True)
