from flask import Flask, jsonify
from .user import users


app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response" : "Hello World"})

@app.route('/users', methods=['GET'])
def usersHandler():
    print ('jijiji')
    return jsonify({"users" : users})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)





